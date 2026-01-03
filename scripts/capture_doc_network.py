#!/usr/bin/env python3
"""
Capture network calls made by the CoinDesk docs page to discover JSON/XHR endpoints.
Outputs matching requests/responses hitting data-api.* domains.
"""
import json
import re
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DOC_URL = "https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/"
OUTPUT_FILE = Path(__file__).parent.parent / "doc_network_capture.json"
# Empty list means capture everything; otherwise filter by substrings
TARGET_PATTERNS = []


def build_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # Enable performance logging to capture network events
    opts.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    return driver


def main():
    driver = build_driver()
    try:
        print(f"Navigating to {DOC_URL}")
        driver.get(DOC_URL)
        # Allow time for XHRs (extended)
        time.sleep(10)

        raw_logs = driver.get_log("performance")
        matches = []
        for entry in raw_logs:
            try:
                msg = json.loads(entry["message"])["message"]
            except Exception:
                continue
            method = msg.get("method", "")
            params = msg.get("params", {})
            if method in {"Network.requestWillBeSent", "Network.responseReceived"}:
                req = params.get("request", {})
                url = req.get("url", "")
                if not url:
                    url = params.get("response", {}).get("url", "")
                if not url:
                    continue
                if TARGET_PATTERNS:
                    if any(pat in url for pat in TARGET_PATTERNS):
                        matches.append({"method": method, "url": url, "params": params})
                else:
                    matches.append({"method": method, "url": url, "params": params})

        # Deduplicate by URL
        seen = set()
        deduped = []
        for m in matches:
            if m["url"] in seen:
                continue
            seen.add(m["url"])
            deduped.append(m)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(deduped, f, indent=2)

        print(f"Captured {len(deduped)} matching requests.")
        if deduped:
            print("Top matches:")
            for m in deduped[:10]:
                print(m["url"])
        print(f"Saved to {OUTPUT_FILE}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
