#!/usr/bin/env python3
"""
Test all 52 CryptoCompare MinAPI endpoints from GitHub issue #12.
Validates endpoints against the live API and reports results.
"""

import requests
import json
import time
from pathlib import Path
from collections import defaultdict

BASE_URL = "https://min-api.cryptocompare.com"
ENDPOINTS_FILE = Path(__file__).parent.parent / "docs" / "ALL_52_ENDPOINTS_FROM_ISSUE_12.json"

def load_endpoints():
    """Load endpoint specifications from JSON file."""
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

def build_test_url(endpoint_spec):
    """Build a test URL with minimal required parameters."""
    endpoint = endpoint_spec["endpoint"]
    params = endpoint_spec.get("parameters", [])
    
    # Build params based on common parameter names
    query_params = {}
    
    if "fsym" in params:
        query_params["fsym"] = "BTC"
    if "tsym" in params or "tsyms" in params:
        query_params["tsyms" if "tsyms" in params else "tsym"] = "USD"
    if "fsyms" in params:
        query_params["fsyms"] = "BTC,ETH"
    if "limit" in params:
        query_params["limit"] = "10"
    if "coinId" in params:
        query_params["coinId"] = "1"
    if "index_id" in params:
        query_params["index_id"] = "1"
    if "e" in params:
        query_params["e"] = "CCCAGG"
    
    # Build URL
    url = f"{BASE_URL}{endpoint}"
    if query_params:
        query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
        url = f"{url}?{query_string}"
    
    return url

def test_endpoint(endpoint_spec):
    """Test a single endpoint and return result."""
    try:
        url = build_test_url(endpoint_spec)
        response = requests.get(url, timeout=5, verify=False)
        
        result = {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": response.status_code,
            "url": url,
            "success": response.status_code == 200
        }
        
        # Try to parse JSON response
        try:
            data = response.json()
            result["response_keys"] = list(data.keys()) if isinstance(data, dict) else "list"
        except:
            result["response_type"] = "non-json"
        
        return result
        
    except requests.exceptions.Timeout:
        return {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": None,
            "success": False,
            "error": "Timeout"
        }
    except Exception as e:
        return {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": None,
            "success": False,
            "error": str(e)
        }

def main():
    print("=" * 80)
    print("Testing All 52 CryptoCompare MinAPI Endpoints")
    print("=" * 80)
    print()
    
    # Load endpoints
    try:
        endpoints = load_endpoints()
        print(f"Loaded {len(endpoints)} endpoints from {ENDPOINTS_FILE.name}")
    except Exception as e:
        print(f"Error loading endpoints: {e}")
        return
    
    print()
    print(f"Testing against: {BASE_URL}")
    print()
    
    # Test each endpoint
    results = []
    category_results = defaultdict(lambda: {"success": 0, "failed": 0, "endpoints": []})
    
    for idx, endpoint_spec in enumerate(endpoints, 1):
        category = endpoint_spec.get("category", "Unknown")
        print(f"[{idx:2d}/52] {category:15s} | {endpoint_spec['endpoint']:40s} ", end="", flush=True)
        
        result = test_endpoint(endpoint_spec)
        results.append(result)
        
        if result["success"]:
            print("[OK]")
            category_results[category]["success"] += 1
        else:
            print(f"[FAIL] {result.get('status_code', 'Error')}")
            category_results[category]["failed"] += 1
        
        category_results[category]["endpoints"].append(result)
        
        # Rate limiting
        time.sleep(0.5)
    
    # Print summary
    print()
    print("=" * 80)
    print("SUMMARY BY CATEGORY")
    print("=" * 80)
    print()
    
    total_success = 0
    total_failed = 0
    
    for category in sorted(category_results.keys()):
        stats = category_results[category]
        success = stats["success"]
        failed = stats["failed"]
        total = success + failed
        percentage = (success / total * 100) if total > 0 else 0
        
        total_success += success
        total_failed += failed
        
        print(f"{category:20s}: {success:2d}/{total:2d} ({percentage:5.1f}%)")
    
    print()
    print(f"TOTAL: {total_success}/{len(endpoints)} ({total_success/len(endpoints)*100:.1f}%)")
    print()
    
    # Save detailed results
    output_file = Path(__file__).parent.parent / "endpoint_test_results.json"
    with open(output_file, "w") as f:
        json.dump({
            "base_url": BASE_URL,
            "total_endpoints": len(endpoints),
            "successful": total_success,
            "failed": total_failed,
            "percentage_success": total_success / len(endpoints) * 100,
            "results": results
        }, f, indent=2)
    
    print(f"Detailed results saved to: {output_file.name}")

if __name__ == "__main__":
    main()
