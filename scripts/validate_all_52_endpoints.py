#!/usr/bin/env python3
"""
Complete validation of all 52 CryptoCompare MinAPI endpoints.
Single comprehensive test with robust error handling.
"""

import requests
import json
import time
from pathlib import Path
from collections import defaultdict
from datetime import datetime

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

def test_endpoint(endpoint_spec, retries=2):
    """Test a single endpoint and return result with retry logic."""
    endpoint = endpoint_spec["endpoint"]
    name = endpoint_spec["name"]
    category = endpoint_spec["category"]
    
    for attempt in range(retries):
        try:
            url = build_test_url(endpoint_spec)
            response = requests.get(url, timeout=10)
            
            result = {
                "endpoint": endpoint,
                "name": name,
                "category": category,
                "status_code": response.status_code,
                "url": url,
                "success": response.status_code == 200,
                "response_size": len(response.text),
                "timestamp": datetime.now().isoformat()
            }
            
            # Try to parse JSON response
            try:
                data = response.json()
                if isinstance(data, dict):
                    result["response_keys"] = list(data.keys())[:5]  # First 5 keys
                    result["response_type"] = "dict"
                elif isinstance(data, list):
                    result["response_type"] = "list"
                    result["list_length"] = len(data)
            except:
                result["response_type"] = "non-json"
            
            return result
            
        except requests.exceptions.Timeout as e:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            return {
                "endpoint": endpoint,
                "name": name,
                "category": category,
                "status_code": None,
                "success": False,
                "error": "Timeout (after retries)",
                "timestamp": datetime.now().isoformat()
            }
        
        except requests.exceptions.ConnectionError as e:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            return {
                "endpoint": endpoint,
                "name": name,
                "category": category,
                "status_code": None,
                "success": False,
                "error": f"Connection error",
                "timestamp": datetime.now().isoformat()
            }
        
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return {
                "endpoint": endpoint,
                "name": name,
                "category": category,
                "status_code": None,
                "success": False,
                "error": str(e)[:100],
                "timestamp": datetime.now().isoformat()
            }

def main():
    print("=" * 90)
    print("COMPREHENSIVE VALIDATION: All 52 CryptoCompare MinAPI Endpoints")
    print("=" * 90)
    print()
    
    # Load endpoints
    try:
        endpoints = load_endpoints()
        print(f"Loaded {len(endpoints)} endpoints from ALL_52_ENDPOINTS_FROM_ISSUE_12.json")
        print(f"Base URL: {BASE_URL}")
        print()
    except Exception as e:
        print(f"ERROR loading endpoints: {e}")
        return 1
    
    # Test each endpoint
    results = []
    category_stats = defaultdict(lambda: {"success": 0, "failed": 0, "endpoints": []})
    
    print(f"{'#':>3} {'Category':<18} {'Endpoint':<42} {'Status':<10} {'Code':<6}")
    print("-" * 90)
    
    start_time = time.time()
    
    for idx, endpoint_spec in enumerate(endpoints, 1):
        category = endpoint_spec.get("category", "Unknown")
        endpoint = endpoint_spec["endpoint"]
        
        # Test endpoint
        result = test_endpoint(endpoint_spec)
        results.append(result)
        
        # Update statistics
        if result["success"]:
            category_stats[category]["success"] += 1
            status_display = "OK"
        else:
            category_stats[category]["failed"] += 1
            status_display = "FAIL"
        
        category_stats[category]["endpoints"].append(result)
        
        # Display result
        code = result.get("status_code", "N/A")
        print(f"{idx:3d} {category:<18} {endpoint:<42} {status_display:<10} {str(code):<6}")
        
        # Rate limiting
        time.sleep(0.8)
    
    elapsed_time = time.time() - start_time
    
    # Print summary
    print()
    print("=" * 90)
    print("SUMMARY")
    print("=" * 90)
    print()
    
    total_success = 0
    total_failed = 0
    
    print(f"{'Category':<20} {'Success':<12} {'Failed':<12} {'Rate':<10}")
    print("-" * 54)
    
    for category in sorted(category_stats.keys()):
        stats = category_stats[category]
        success = stats["success"]
        failed = stats["failed"]
        total = success + failed
        percentage = (success / total * 100) if total > 0 else 0
        
        total_success += success
        total_failed += failed
        
        print(f"{category:<20} {success:<12} {failed:<12} {percentage:>6.1f}%")
    
    print("-" * 54)
    total = total_success + total_failed
    overall_rate = (total_success / total * 100) if total > 0 else 0
    print(f"{'TOTAL':<20} {total_success:<12} {total_failed:<12} {overall_rate:>6.1f}%")
    print()
    print(f"Time elapsed: {elapsed_time:.1f} seconds")
    print()
    
    # Save detailed results
    output_file = Path(__file__).parent.parent / "endpoint_validation_complete.json"
    with open(output_file, "w") as f:
        json.dump({
            "test_metadata": {
                "base_url": BASE_URL,
                "timestamp": datetime.now().isoformat(),
                "total_endpoints": len(endpoints),
                "successful": total_success,
                "failed": total_failed,
                "percentage_success": overall_rate,
                "elapsed_seconds": elapsed_time
            },
            "results_by_category": {
                cat: {
                    "success": stats["success"],
                    "failed": stats["failed"],
                    "endpoints": stats["endpoints"]
                }
                for cat, stats in category_stats.items()
            },
            "all_results": results
        }, f, indent=2)
    
    print(f"Complete results saved to: {output_file.name}")
    
    # Print any failed endpoints
    if total_failed > 0:
        print()
        print("=" * 90)
        print(f"FAILED ENDPOINTS ({total_failed})")
        print("=" * 90)
        print()
        for result in results:
            if not result["success"]:
                error = result.get("error", f"Status {result.get('status_code', 'Unknown')}")
                print(f"  [{result['category']:<18}] {result['endpoint']:<40} | {error}")
        print()
    
    # Success/failure summary
    print("=" * 90)
    if total_failed == 0:
        print(f"✅ SUCCESS: All {total_success} endpoints are working!")
    else:
        print(f"⚠️  {total_success} working, {total_failed} failed")
    print("=" * 90)
    
    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    exit(main())
