#!/usr/bin/env python3
"""
Scrape complete documentation from CoinDesk/CryptoCompare developer site using Selenium.
This handles JavaScript-rendered pages that BeautifulSoup alone cannot parse.
Outputs rich parameter/response metadata into full_api_documentation_selenium.json.
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

ENDPOINTS_FILE = Path(__file__).parent.parent / "docs" / "ALL_52_ENDPOINTS_FROM_ISSUE_12.json"
OUTPUT_FILE = Path(__file__).parent.parent / "full_api_documentation_selenium.json"

# ---------- Helpers ----------

def load_endpoints():
    with open(ENDPOINTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    endpoints = []
    for category, items in data.items():
        if category in {"metadata", "summary"}:
            continue
        for spec in items:
            spec["category"] = category
            endpoints.append(spec)
    return endpoints


def build_driver(headless: bool = True) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Silence logs
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def extract_text(element):
    return element.get_text(strip=True, separator=" ") if element else ""


def extract_parameters(soup: BeautifulSoup):
    params = []

    # Tables
    for table in soup.find_all("table"):
        headers = [extract_text(h).lower() for h in table.find_all("th")]
        if any("param" in h or "name" == h for h in headers):
            for row in table.find_all("tr")[1:]:
                cells = row.find_all(["td", "th"])
                if not cells:
                    continue
                params.append({
                    "name": extract_text(cells[0]),
                    "description": extract_text(cells[1]) if len(cells) > 1 else "",
                    "type": extract_text(cells[2]) if len(cells) > 2 else "",
                    "required": "required" in extract_text(row).lower(),
                })

    # Definition lists
    for dl in soup.find_all("dl"):
        dts = dl.find_all("dt")
        dds = dl.find_all("dd")
        for dt, dd in zip(dts, dds):
            name = extract_text(dt)
            if not name:
                continue
            params.append({
                "name": name,
                "description": extract_text(dd),
                "required": "required" in extract_text(dd).lower(),
            })

    # Inline patterns
    for p in soup.find_all("p"):
        text = extract_text(p)
        matches = re.findall(r"`?([a-zA-Z_][a-zA-Z0-9_]*)`?\s*\(([^)]+)\)\s*[:-]\s*([^.]*)", text)
        for name, typ, desc in matches:
            params.append({
                "name": name,
                "type": typ,
                "description": desc.strip(),
                "required": "required" in typ.lower(),
            })

    return params


def extract_response_schema(soup: BeautifulSoup):
    schema = {"fields": [], "example": None}

    response_headers = soup.find_all(["h2", "h3", "h4"], string=re.compile(r"response", re.I))
    for header in response_headers:
        node = header.find_next_sibling()
        while node and node.name not in ["h1", "h2", "h3"]:
            if node.name == "table":
                for row in node.find_all("tr")[1:]:
                    cells = row.find_all(["td", "th"])
                    if not cells:
                        continue
                    schema["fields"].append({
                        "name": extract_text(cells[0]),
                        "description": extract_text(cells[1]) if len(cells) > 1 else "",
                        "type": extract_text(cells[2]) if len(cells) > 2 else "",
                    })
            elif node.name in {"pre", "code"}:
                raw = extract_text(node)
                try:
                    schema["example"] = json.loads(raw)
                except Exception:
                    schema["example"] = raw[:800]
            node = node.find_next_sibling()
    return schema


def extract_rate_limit(soup: BeautifulSoup):
    text = soup.get_text(" ").lower()
    limits = re.findall(r"(\d+)\s*(requests|calls)\s*per\s*(second|minute|hour|day)", text)
    return [" ".join(match) for match in limits]


def extract_auth(soup: BeautifulSoup):
    text = soup.get_text(" ").lower()
    auth = {"required": False, "type": None, "header": None}
    if "api key" in text or "x-api-key" in text:
        auth.update({"required": True, "type": "API Key", "header": "x-api-key"})
    if "authorization" in text and "bearer" in text:
        auth.update({"required": True, "type": "Bearer", "header": "Authorization"})
    return auth


def scrape_endpoint(driver: webdriver.Chrome, spec: dict):
    doc_url = spec.get("doc_url")
    if not doc_url:
        return {"endpoint": spec["endpoint"], "success": False, "error": "No doc_url"}

    print(f"  Navigating {doc_url}")
    try:
        driver.get(doc_url)
        # Wait for body content to load; fallback to simple sleep if needed
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(1.0)  # allow JS rendering
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        title = extract_text(soup.find("h1")) or spec.get("name", "")
        description = extract_text(soup.find("p"))

        params = extract_parameters(soup)
        schema = extract_response_schema(soup)
        rate_limits = extract_rate_limit(soup)
        auth = extract_auth(soup)

        examples = []
        for code in soup.find_all(["pre", "code"])[:3]:
            text = extract_text(code)
            if text and len(text) > 10:
                examples.append(text[:800])

        return {
            "endpoint": spec["endpoint"],
            "name": spec.get("name"),
            "category": spec.get("category"),
            "doc_url": doc_url,
            "title": title,
            "description": description,
            "parameters": params,
            "response_schema": schema,
            "rate_limits": rate_limits,
            "authentication": auth,
            "examples": examples,
            "success": True,
            "scraped_at": datetime.now().isoformat(),
        }
    except Exception as exc:
        return {
            "endpoint": spec["endpoint"],
            "name": spec.get("name"),
            "category": spec.get("category"),
            "doc_url": doc_url,
            "success": False,
            "error": str(exc),
            "scraped_at": datetime.now().isoformat(),
        }


# ---------- Main ----------

def main():
    print("=" * 80)
    print("Selenium Documentation Scraper - CryptoCompare MinAPI")
    print("=" * 80)

    endpoints = load_endpoints()
    print(f"Loaded {len(endpoints)} endpoints")

    driver = build_driver(headless=True)

    results = {
        "metadata": {
            "scraped_at": datetime.now().isoformat(),
            "total_endpoints": len(endpoints),
            "successful": 0,
            "failed": 0,
        },
        "endpoints": {},
    }

    try:
        for idx, spec in enumerate(endpoints, 1):
            print(f"[{idx}/{len(endpoints)}] {spec.get('name')}")
            data = scrape_endpoint(driver, spec)
            results["endpoints"][spec["endpoint"]] = data
            if data.get("success"):
                results["metadata"]["successful"] += 1
            else:
                results["metadata"]["failed"] += 1
                print(f"    ✗ {data.get('error', 'unknown error')}")
            time.sleep(1.0)  # be polite to the site
    finally:
        driver.quit()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total: {results['metadata']['total_endpoints']}")
    print(f"Success: {results['metadata']['successful']}")
    print(f"Failed: {results['metadata']['failed']}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
