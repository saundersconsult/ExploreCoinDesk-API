#!/usr/bin/env python3
"""
Extended probe script for CryptoCompare MinAPI - testing additional documented endpoints.
Based on navigation menu from https://developers.coindesk.com/documentation/legacy/
"""

import requests
import json
from pathlib import Path
from datetime import datetime

BASE_URL = "https://min-api.cryptocompare.com"

# Extended endpoint categories from documentation
ENDPOINTS = {
    # Blockchain Data
    "/data/blockchain/histo/day": {
        "desc": "Historical blockchain stats (daily)",
        "params": {"fsym": "BTC", "limit": 10}
    },
    "/data/blockchain/histo/hour": {
        "desc": "Historical blockchain stats (hourly)",
        "params": {"fsym": "BTC", "limit": 10}
    },
    "/data/blockchain/list": {
        "desc": "List of available blockchain data",
        "params": None
    },
    "/data/blockchain/latest": {
        "desc": "Latest blockchain data",
        "params": {"fsym": "BTC"}
    },
    
    # Social Stats
    "/data/social/coin/histo/day": {
        "desc": "Historical social stats (daily)",
        "params": {"coinId": "1182", "limit": 10}
    },
    "/data/social/coin/histo/hour": {
        "desc": "Historical social stats (hourly)",
        "params": {"coinId": "1182", "limit": 10}
    },
    "/data/social/coin/latest": {
        "desc": "Latest social stats",
        "params": {"coinId": "1182"}
    },
    "/data/social/stats/latest": {
        "desc": "Latest social statistics",
        "params": None
    },
    
    # News
    "/data/v2/news/": {
        "desc": "Crypto news feed (v2)",
        "params": {"lang": "EN"}
    },
    "/data/news/feeds": {
        "desc": "Available news feeds",
        "params": None
    },
    "/data/news/feedsandcategories": {
        "desc": "News feeds and categories",
        "params": None
    },
    "/data/news/categories": {
        "desc": "News categories",
        "params": None
    },
    
    # Trading Pairs & Exchanges
    "/data/top/pairs": {
        "desc": "Top trading pairs",
        "params": {"fsym": "BTC", "limit": 10}
    },
    "/data/top/exchanges/full": {
        "desc": "Full exchange data",
        "params": {"fsym": "BTC", "tsym": "USD", "limit": 10}
    },
    "/data/top/volumes": {
        "desc": "Top volumes by pair",
        "params": {"tsym": "USD", "limit": 10}
    },
    "/data/v2/pair/mapping/exchange": {
        "desc": "Exchange pair mapping",
        "params": {"e": "Coinbase"}
    },
    "/data/v2/pair/mapping/fsym": {
        "desc": "From symbol pair mapping",
        "params": {"fsym": "BTC"}
    },
    
    # Reference Data
    "/data/all/coinlist": {
        "desc": "All available coins",
        "params": None
    },
    "/data/all/exchanges": {
        "desc": "All exchanges and trading pairs",
        "params": None
    },
    "/data/blockchain/available_coins": {
        "desc": "Available blockchain coins",
        "params": None
    },
    "/data/coin/generalinfo": {
        "desc": "General coin information",
        "params": {"fsyms": "BTC,ETH", "tsym": "USD"}
    },
    "/data/coin/snapshot": {
        "desc": "Coin snapshot",
        "params": {"fsym": "BTC", "tsym": "USD"}
    },
    "/data/coin/snapshotfullbyid": {
        "desc": "Full coin snapshot by ID",
        "params": {"id": "1182"}
    },
    
    # Price History
    "/data/pricehistorical": {
        "desc": "Historical price at specific time",
        "params": {"fsym": "BTC", "tsyms": "USD", "ts": "1609459200"}
    },
    "/data/coinaverage": {
        "desc": "Coin average price",
        "params": {"fsym": "BTC", "tsym": "USD", "e": "Coinbase"}
    },
    "/data/generateavg": {
        "desc": "Generate weighted average",
        "params": {"fsym": "BTC", "tsym": "USD", "e": "Coinbase"}
    },
    
    # Exchange Data
    "/data/exchange/histoday": {
        "desc": "Exchange historical daily volume",
        "params": {"tsym": "USD", "limit": 10}
    },
    "/data/exchange/histohour": {
        "desc": "Exchange historical hourly volume",
        "params": {"tsym": "USD", "limit": 10}
    },
    
    # Mining
    "/data/mining/pools/general": {
        "desc": "General mining pools data",
        "params": None
    },
    "/data/mining/pools/coins": {
        "desc": "Mining pools by coin",
        "params": {"fsym": "BTC"}
    },
    "/data/mining/equipment": {
        "desc": "Mining equipment data",
        "params": None
    },
    "/data/mining/contracts": {
        "desc": "Mining contracts data",
        "params": None
    },
    
    # Rate Limits & Status
    "/data/stats/rate/limit": {
        "desc": "Rate limit status",
        "params": None
    },
    "/data/stats/rate/hour/limit": {
        "desc": "Hourly rate limit",
        "params": None
    },
    
    # Symbols & Pairs
    "/data/pair/mapping/exchange": {
        "desc": "Pair mapping by exchange",
        "params": {"e": "Coinbase"}
    },
    "/data/trading/pairs": {
        "desc": "Trading pairs",
        "params": None
    },
    
    # Order Book (Snapshot)
    "/data/ob/l1/top": {
        "desc": "Level 1 order book top",
        "params": {"fsyms": "BTC", "tsyms": "USD"}
    },
    "/data/ob/l2/snapshot": {
        "desc": "Level 2 order book snapshot",
        "params": {"fsym": "BTC", "tsym": "USD"}
    },
    
    # Alternative endpoints
    "/data/v2/histo/day": {
        "desc": "Alternative historical daily (v2)",
        "params": {"fsym": "BTC", "tsym": "USD", "limit": 10}
    },
    "/data/v2/histo/hour": {
        "desc": "Alternative historical hourly (v2)",
        "params": {"fsym": "BTC", "tsym": "USD", "limit": 10}
    },
    "/data/v2/histo/minute": {
        "desc": "Alternative historical minute (v2)",
        "params": {"fsym": "BTC", "tsym": "USD", "limit": 10}
    },
}

def test_endpoint(path, params=None):
    """Test a single endpoint"""
    url = BASE_URL + path
    try:
        response = requests.get(url, params=params, timeout=10)
        
        # Try to parse JSON
        try:
            json_data = response.json()
            
            # Check for CryptoCompare error responses
            if isinstance(json_data, dict):
                if json_data.get("Response") == "Error":
                    error_msg = json_data.get("Message", "Unknown error")
                    return {
                        "status_code": response.status_code,
                        "success": False,
                        "error_type": "api_error",
                        "error": error_msg,
                        "response_preview": str(json_data)[:200]
                    }
                elif json_data.get("Response") == "Success" or "Data" in json_data:
                    return {
                        "status_code": response.status_code,
                        "success": True,
                        "error": None,
                        "error_type": None,
                        "response_preview": str(json_data)[:200]
                    }
            
            # Valid JSON but unknown structure
            return {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "error": None,
                "error_type": None,
                "response_preview": str(json_data)[:200]
            }
            
        except json.JSONDecodeError:
            return {
                "status_code": response.status_code,
                "success": False,
                "error": "Invalid JSON response",
                "error_type": "json_error",
                "response_preview": response.text[:200]
            }
            
    except requests.RequestException as e:
        return {
            "status_code": None,
            "success": False,
            "error": str(e),
            "error_type": "connection_error",
            "response_preview": None
        }

def main():
    """Main probe function"""
    print("=" * 80)
    print("CryptoCompare MinAPI Extended Endpoint Exploration")
    print(f"Base URL: {BASE_URL}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Total Endpoints: {len(ENDPOINTS)}")
    print("=" * 80)
    
    results = {}
    categories = {
        "working": [],
        "api_error": [],
        "auth_required": [],
        "path_not_found": [],
        "param_required": [],
        "other_error": []
    }
    
    for endpoint, config in ENDPOINTS.items():
        print(f"\nTesting: {endpoint}")
        print(f"  Description: {config['desc']}")
        
        result = test_endpoint(endpoint, params=config['params'])
        results[endpoint] = {
            "description": config['desc'],
            "params": config['params'],
            "result": result
        }
        
        # Categorize results
        if result["success"]:
            categories["working"].append(endpoint)
            print(f"  ✓ Status: {result['status_code']} - SUCCESS")
            if result['response_preview']:
                print(f"  Preview: {result['response_preview'][:150]}...")
        else:
            error = result.get("error", "").lower()
            
            if "auth" in error or "api key" in error:
                categories["auth_required"].append(endpoint)
                print(f"  🔒 Auth Required: {result['error']}")
            elif "path does not exist" in error:
                categories["path_not_found"].append(endpoint)
                print(f"  ✗ Path Not Found")
            elif "required param" in error or "missing" in error:
                categories["param_required"].append(endpoint)
                print(f"  ⚠ Missing Required Param: {result['error']}")
            elif result["error_type"] == "api_error":
                categories["api_error"].append(endpoint)
                print(f"  ✗ API Error: {result['error']}")
            else:
                categories["other_error"].append(endpoint)
                print(f"  ✗ Error: {result['error']}")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY BY CATEGORY")
    print("=" * 80)
    print(f"Total endpoints tested: {len(ENDPOINTS)}")
    print(f"✓ Working (accessible): {len(categories['working'])}")
    print(f"🔒 Auth required: {len(categories['auth_required'])}")
    print(f"✗ Path not found: {len(categories['path_not_found'])}")
    print(f"⚠ Missing params: {len(categories['param_required'])}")
    print(f"✗ API errors: {len(categories['api_error'])}")
    print(f"✗ Other errors: {len(categories['other_error'])}")
    
    if categories["working"]:
        print("\n" + "=" * 80)
        print("WORKING ENDPOINTS")
        print("=" * 80)
        for endpoint in categories["working"]:
            print(f"  ✓ {endpoint}")
            print(f"    {ENDPOINTS[endpoint]['desc']}")
    
    if categories["auth_required"]:
        print("\n" + "=" * 80)
        print("AUTHENTICATION REQUIRED")
        print("=" * 80)
        for endpoint in categories["auth_required"]:
            print(f"  🔒 {endpoint}")
    
    if categories["path_not_found"]:
        print("\n" + "=" * 80)
        print("PATH NOT FOUND (Not Available)")
        print("=" * 80)
        for endpoint in categories["path_not_found"][:10]:
            print(f"  ✗ {endpoint}")
        if len(categories["path_not_found"]) > 10:
            print(f"  ... and {len(categories['path_not_found']) - 10} more")
    
    # Save detailed results
    results_file = Path(__file__).parent.parent / "cryptocompare_extended_results.json"
    with open(results_file, "w") as f:
        json.dump({
            "summary": {
                "total": len(ENDPOINTS),
                "working": len(categories["working"]),
                "auth_required": len(categories["auth_required"]),
                "path_not_found": len(categories["path_not_found"]),
                "param_required": len(categories["param_required"]),
                "api_errors": len(categories["api_error"]),
                "other_errors": len(categories["other_error"])
            },
            "categories": categories,
            "results": results
        }, f, indent=2)
    
    print(f"\nDetailed results saved to: {results_file}")
    print("\n" + "=" * 80)
    print("EXPLORATION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
