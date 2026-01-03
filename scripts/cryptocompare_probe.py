#!/usr/bin/env python3
"""
Probe script to explore CryptoCompare MinAPI endpoints.
Exploring the /data endpoint structure at https://min-api.cryptocompare.com/data
"""

import requests
import json
from pathlib import Path
from datetime import datetime

BASE_URL = "https://min-api.cryptocompare.com/data"

# Common endpoint patterns to test
ENDPOINTS = {
    # Price endpoints
    "/price": "GET current price",
    "/pricemulti": "GET multiple prices at once",
    "/pricemultifull": "GET detailed price info",
    "/generateAvg": "GET weighted average price",
    "/dayAvg": "GET daily average price",
    
    # Historical data
    "/histoday": "GET daily historical data",
    "/histohour": "GET hourly historical data",
    "/histominute": "GET minute historical data",
    
    # Top data
    "/top/mktcapfull": "GET top coins by market cap",
    "/top/mktcap": "GET top coins by market cap (simple)",
    "/top/totalvolfull": "GET top coins by volume",
    "/top/totalvol": "GET top coins by volume (simple)",
    "/top/exchanges": "GET top exchanges",
    
    # News/Social
    "/news": "GET crypto news",
    "/social": "GET social stats",
    
    # Mining
    "/mining/pools": "GET mining pools",
    "/mining/equipment": "GET mining equipment",
    "/mining/contracts": "GET mining contracts",
    
    # Blockchain
    "/blockchain/latest": "GET latest blockchain data",
    
    # Rates
    "/rate": "GET exchange rates",
    "/ratelimit": "GET rate limit status",
    
    # Sentiment
    "/sentiment": "GET market sentiment",
    
    # Pairs
    "/pairs": "GET available trading pairs",
    
    # Other
    "/tradingpairs": "GET trading pairs",
    "/exchanges": "GET all exchanges",
    "/cryptocurrencies": "GET all cryptocurrencies",
    "/categories": "GET coin categories",
}

# Test parameters for different endpoint types
TEST_PARAMS = {
    "/price": {"fsym": "BTC", "tsyms": "USD,EUR"},
    "/pricemulti": {"fsyms": "BTC,ETH", "tsyms": "USD"},
    "/pricemultifull": {"fsyms": "BTC,ETH", "tsyms": "USD"},
    "/histoday": {"fsym": "BTC", "tsym": "USD", "limit": 10},
    "/histohour": {"fsym": "BTC", "tsym": "USD", "limit": 10},
    "/histominute": {"fsym": "BTC", "tsym": "USD", "limit": 10},
    "/top/mktcapfull": {"tsym": "USD", "limit": 5},
}

def test_endpoint(path, method="GET", params=None):
    """Test a single endpoint"""
    url = BASE_URL + path
    try:
        if method == "GET":
            response = requests.get(url, params=params, timeout=5)
        else:
            response = requests.post(url, params=params, timeout=5)
        
        return {
            "status_code": response.status_code,
            "success": response.status_code < 400,
            "error": None,
            "response_preview": response.text[:200] if response.text else None,
        }
    except requests.RequestException as e:
        return {
            "status_code": None,
            "success": False,
            "error": str(e),
            "response_preview": None,
        }

def main():
    """Main probe function"""
    print("=" * 80)
    print("CryptoCompare MinAPI Endpoint Exploration")
    print(f"Base URL: {BASE_URL}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)
    
    results = {}
    working_endpoints = []
    failed_endpoints = []
    
    for endpoint, description in ENDPOINTS.items():
        print(f"\nTesting: {endpoint}")
        print(f"  Description: {description}")
        
        # Use test params if available, otherwise None
        params = TEST_PARAMS.get(endpoint)
        
        result = test_endpoint(endpoint, params=params)
        results[endpoint] = {
            "description": description,
            "result": result,
            "params": params,
        }
        
        if result["success"]:
            working_endpoints.append(endpoint)
            print(f"  ✓ Status: {result['status_code']} - SUCCESS")
            if result['response_preview']:
                print(f"  Preview: {result['response_preview'][:150]}...")
        else:
            failed_endpoints.append(endpoint)
            print(f"  ✗ Status: {result['status_code']} - FAILED")
            if result["error"]:
                print(f"  Error: {result['error']}")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total endpoints tested: {len(ENDPOINTS)}")
    print(f"Working endpoints: {len(working_endpoints)}")
    print(f"Failed endpoints: {len(failed_endpoints)}")
    
    if working_endpoints:
        print("\nWorking Endpoints:")
        for endpoint in working_endpoints:
            print(f"  • {endpoint} - {ENDPOINTS[endpoint]}")
    
    if failed_endpoints:
        print("\nFailed Endpoints:")
        for endpoint in failed_endpoints[:10]:  # Show first 10
            print(f"  • {endpoint} - {ENDPOINTS[endpoint]}")
        if len(failed_endpoints) > 10:
            print(f"  ... and {len(failed_endpoints) - 10} more")
    
    # Save detailed results
    results_file = Path(__file__).parent.parent / "cryptocompare_probe_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDetailed results saved to: {results_file}")

if __name__ == "__main__":
    main()
