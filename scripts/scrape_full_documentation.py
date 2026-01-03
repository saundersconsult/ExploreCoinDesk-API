#!/usr/bin/env python3
"""
Scrape complete documentation from CoinDesk/CryptoCompare developer site.
Extracts detailed parameter descriptions, response schemas, rate limits, etc.
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path
from datetime import datetime
import re

# Load our validated endpoints
ENDPOINTS_FILE = Path(__file__).parent.parent / "docs" / "ALL_52_ENDPOINTS_FROM_ISSUE_12.json"
OUTPUT_FILE = Path(__file__).parent.parent / "full_api_documentation.json"

def load_endpoints():
    """Load endpoint specifications with doc URLs."""
    with open(ENDPOINTS_FILE, "r") as f:
        data = json.load(f)
    
    endpoints = []
    for category, items in data.items():
        if category in ["metadata", "summary"]:
            continue
        
        if isinstance(items, list):
            for endpoint_spec in items:
                endpoint_spec["category"] = category
                endpoints.append(endpoint_spec)
    
    return endpoints

def extract_text_content(element):
    """Extract clean text from HTML element."""
    if not element:
        return ""
    return element.get_text(strip=True, separator=" ")

def extract_parameter_details(soup):
    """Extract detailed parameter information from documentation."""
    parameters = []
    
    # Look for parameter tables or lists
    # Pattern 1: Table with parameter descriptions
    tables = soup.find_all('table')
    for table in tables:
        headers = [th.get_text(strip=True).lower() for th in table.find_all('th')]
        if 'parameter' in ' '.join(headers) or 'name' in headers:
            for row in table.find_all('tr')[1:]:  # Skip header
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    param = {
                        'name': cols[0].get_text(strip=True),
                        'description': cols[1].get_text(strip=True) if len(cols) > 1 else '',
                        'type': cols[2].get_text(strip=True) if len(cols) > 2 else '',
                        'required': 'required' in extract_text_content(row).lower()
                    }
                    parameters.append(param)
    
    # Pattern 2: Definition lists
    dls = soup.find_all('dl')
    for dl in dls:
        terms = dl.find_all('dt')
        descriptions = dl.find_all('dd')
        for term, desc in zip(terms, descriptions):
            param_name = extract_text_content(term)
            if param_name and not param_name.startswith('Response'):
                parameters.append({
                    'name': param_name,
                    'description': extract_text_content(desc),
                    'required': 'required' in extract_text_content(desc).lower()
                })
    
    # Pattern 3: Look for parameter documentation in paragraphs
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        text = extract_text_content(p)
        # Look for patterns like "fsym (required): description"
        matches = re.findall(r'`?([a-zA-Z_][a-zA-Z0-9_]*)`?\s*\(([^)]+)\)\s*[:-]\s*([^.]+)', text)
        for match in matches:
            parameters.append({
                'name': match[0],
                'type': match[1],
                'description': match[2].strip(),
                'required': 'required' in match[1].lower()
            })
    
    return parameters

def extract_response_schema(soup):
    """Extract response schema information."""
    schema = {
        'description': '',
        'fields': [],
        'example': None
    }
    
    # Look for response documentation
    response_headers = soup.find_all(['h2', 'h3', 'h4'], string=re.compile(r'response', re.I))
    
    for header in response_headers:
        # Get content after this header
        current = header.find_next_sibling()
        while current and current.name not in ['h1', 'h2', 'h3']:
            if current.name == 'table':
                # Extract field descriptions from table
                for row in current.find_all('tr')[1:]:
                    cols = row.find_all(['td', 'th'])
                    if len(cols) >= 2:
                        schema['fields'].append({
                            'name': cols[0].get_text(strip=True),
                            'description': cols[1].get_text(strip=True) if len(cols) > 1 else '',
                            'type': cols[2].get_text(strip=True) if len(cols) > 2 else ''
                        })
            
            elif current.name == 'pre' or current.name == 'code':
                # JSON example
                code_text = extract_text_content(current)
                try:
                    schema['example'] = json.loads(code_text)
                except:
                    schema['example'] = code_text[:500]
            
            current = current.find_next_sibling()
    
    return schema

def extract_rate_limit_info(soup):
    """Extract rate limiting information."""
    rate_info = {
        'limits': [],
        'description': ''
    }
    
    text = soup.get_text()
    
    # Look for rate limit mentions
    rate_patterns = [
        r'(\d+)\s*requests?\s*per\s*(second|minute|hour|day)',
        r'rate\s*limit[:\s]+(\d+)',
        r'(\d+)\s*calls?\s*per\s*(second|minute|hour)'
    ]
    
    for pattern in rate_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            rate_info['limits'].append(' '.join(str(m) for m in match))
    
    return rate_info

def extract_authentication_info(soup):
    """Extract authentication requirements."""
    auth_info = {
        'required': False,
        'type': None,
        'description': ''
    }
    
    text = soup.get_text().lower()
    
    # Check for authentication mentions
    if 'api key' in text or 'api_key' in text or 'x-api-key' in text:
        auth_info['required'] = True
        auth_info['type'] = 'API Key'
        
        # Look for header name
        if 'x-api-key' in text:
            auth_info['header'] = 'x-api-key'
        elif 'authorization' in text:
            auth_info['header'] = 'Authorization'
    
    if 'bearer' in text:
        auth_info['type'] = 'Bearer Token'
    
    return auth_info

def scrape_endpoint_documentation(endpoint_spec):
    """Scrape complete documentation for a single endpoint."""
    doc_url = endpoint_spec.get('doc_url')
    
    if not doc_url:
        return {
            'endpoint': endpoint_spec['endpoint'],
            'error': 'No documentation URL available'
        }
    
    print(f"  Scraping: {endpoint_spec['name']}")
    print(f"    URL: {doc_url}")
    
    try:
        response = requests.get(doc_url, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title/description
        title = soup.find('h1')
        description = extract_text_content(title) if title else endpoint_spec.get('name', '')
        
        # Look for main description
        main_desc = ""
        first_p = soup.find('p')
        if first_p:
            main_desc = extract_text_content(first_p)
        
        # Extract all documentation components
        doc_data = {
            'endpoint': endpoint_spec['endpoint'],
            'name': endpoint_spec['name'],
            'category': endpoint_spec['category'],
            'doc_url': doc_url,
            'title': description,
            'description': main_desc,
            'parameters': extract_parameter_details(soup),
            'response_schema': extract_response_schema(soup),
            'rate_limits': extract_rate_limit_info(soup),
            'authentication': extract_authentication_info(soup),
            'scraped_at': datetime.now().isoformat(),
            'success': True
        }
        
        # Extract any code examples
        code_blocks = soup.find_all(['pre', 'code'])
        examples = []
        for code in code_blocks[:3]:  # First 3 examples
            example_text = extract_text_content(code)
            if example_text and len(example_text) > 10:
                examples.append(example_text[:500])
        
        if examples:
            doc_data['examples'] = examples
        
        print(f"    ✓ Found {len(doc_data['parameters'])} parameters")
        print(f"    ✓ Found {len(doc_data['response_schema']['fields'])} response fields")
        
        return doc_data
        
    except requests.exceptions.Timeout:
        return {
            'endpoint': endpoint_spec['endpoint'],
            'doc_url': doc_url,
            'error': 'Timeout',
            'success': False
        }
    except Exception as e:
        return {
            'endpoint': endpoint_spec['endpoint'],
            'doc_url': doc_url,
            'error': str(e)[:200],
            'success': False
        }

def main():
    print("=" * 80)
    print("Full Documentation Scraper - CryptoCompare MinAPI")
    print("=" * 80)
    print()
    
    # Load endpoints
    endpoints = load_endpoints()
    print(f"Loaded {len(endpoints)} endpoints")
    print()
    
    # Scrape documentation for each endpoint
    results = {
        'metadata': {
            'scraped_at': datetime.now().isoformat(),
            'total_endpoints': len(endpoints),
            'successful': 0,
            'failed': 0
        },
        'endpoints': {}
    }
    
    for idx, endpoint_spec in enumerate(endpoints, 1):
        print(f"[{idx}/{len(endpoints)}] {endpoint_spec['category']}")
        
        doc_data = scrape_endpoint_documentation(endpoint_spec)
        results['endpoints'][endpoint_spec['endpoint']] = doc_data
        
        if doc_data.get('success'):
            results['metadata']['successful'] += 1
        else:
            results['metadata']['failed'] += 1
            print(f"    ✗ {doc_data.get('error', 'Unknown error')}")
        
        # Rate limiting - be respectful
        time.sleep(1.5)
        print()
    
    # Save results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total endpoints: {results['metadata']['total_endpoints']}")
    print(f"Successfully scraped: {results['metadata']['successful']}")
    print(f"Failed: {results['metadata']['failed']}")
    print(f"\nResults saved to: {OUTPUT_FILE}")
    
    # Print statistics
    total_params = sum(len(ep.get('parameters', [])) for ep in results['endpoints'].values() if ep.get('success'))
    total_fields = sum(len(ep.get('response_schema', {}).get('fields', [])) for ep in results['endpoints'].values() if ep.get('success'))
    
    print(f"\nExtracted:")
    print(f"  - {total_params} parameter descriptions")
    print(f"  - {total_fields} response field descriptions")

if __name__ == "__main__":
    main()
