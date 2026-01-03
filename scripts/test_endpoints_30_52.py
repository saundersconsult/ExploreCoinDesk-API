#!/usr/bin/env python3
"""
Test remaining CryptoCompare MinAPI endpoints (30-52).
Completes validation after initial test failed at endpoint 29.
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
        
        # Try with shorter timeout and retry logic
        for attempt in range(2):
            try:
                response = requests.get(url, timeout=8)
                
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
                if attempt == 0:
                    time.sleep(2)  # Wait before retry
                    continue
                else:
                    raise
        
    except requests.exceptions.ConnectionError as e:
        return {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": None,
            "success": False,
            "error": f"Connection error: {str(e)[:50]}"
        }
    except requests.exceptions.Timeout:
        return {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": None,
            "success": False,
            "error": "Timeout (retried twice)"
        }
    except Exception as e:
        return {
            "endpoint": endpoint_spec["endpoint"],
            "name": endpoint_spec["name"],
            "category": endpoint_spec["category"],
            "status_code": None,
            "success": False,
            "error": str(e)[:100]
        }

def main():
    print("=" * 80)
    print("Testing Remaining CryptoCompare MinAPI Endpoints (30-52)")
    print("=" * 80)
    print()
    
    # Load endpoints
    try:
        all_endpoints = load_endpoints()
        # Test endpoints 30-52 (indices 29-51)
        endpoints = all_endpoints[29:]
        print(f"Loaded {len(endpoints)} remaining endpoints (30-52)")
    except Exception as e:
        print(f"Error loading endpoints: {e}")
        return
    
    print(f"Testing against: {BASE_URL}")
    print()
    
    # Test each endpoint
    results = []
    category_results = defaultdict(lambda: {"success": 0, "failed": 0, "endpoints": []})
    
    for idx, endpoint_spec in enumerate(endpoints, 30):  # Start from 30
        category = endpoint_spec.get("category", "Unknown")
        print(f"[{idx:2d}/52] {category:15s} | {endpoint_spec['endpoint']:40s} ", end="", flush=True)
        
        result = test_endpoint(endpoint_spec)
        results.append(result)
        
        if result["success"]:
            print("[OK]")
            category_results[category]["success"] += 1
        else:
            print(f"[{result.get('status_code', 'FAIL')}]")
            category_results[category]["failed"] += 1
        
        category_results[category]["endpoints"].append(result)
        
        # Rate limiting
        time.sleep(1)
    
    # Print summary
    print()
    print("=" * 80)
    print("SUMMARY - Endpoints 30-52")
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
    print(f"TOTAL (30-52): {total_success}/{len(endpoints)} ({total_success/len(endpoints)*100:.1f}%)")
    print()
    
    # Save detailed results for this batch
    output_file = Path(__file__).parent.parent / "endpoint_test_results_30_52.json"
    with open(output_file, "w") as f:
        json.dump({
            "base_url": BASE_URL,
            "endpoints_tested": "30-52",
            "total_endpoints": len(endpoints),
            "successful": total_success,
            "failed": total_failed,
            "percentage_success": total_success / len(endpoints) * 100 if len(endpoints) > 0 else 0,
            "results": results
        }, f, indent=2)
    
    print(f"Detailed results saved to: {output_file.name}")
    
    # Print failed endpoints if any
    if total_failed > 0:
        print()
        print("Failed Endpoints:")
        for result in results:
            if not result["success"]:
                error = result.get("error", result.get("status_code", "Unknown"))
                print(f"  - {result['endpoint']:40s} ({error})")

if __name__ == "__main__":
    main()
