#!/usr/bin/env python3
"""
Scrape CoinDesk/CryptoCompare MinAPI documentation to extract endpoint specifications.
"""

import requests
import json
from pathlib import Path
from datetime import datetime
import re

DOCUMENTATION_URLS = {
    "Price": [
        "https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/",
        "https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsPriceEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsFullPriceEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Price/generateAverageEndpoint",
    ],
    "Historical": [
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistoday",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistohour",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistominute",
        "https://developers.coindesk.com/documentation/legacy/Historical/dailyMarketClose",
        "https://developers.coindesk.com/documentation/legacy/Historical/DailyHistoMinute",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataPriceHistorical",
    ],
    "Blockchain": [
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainListOfCoins",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainLatest",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainDay",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionLatest",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionDay",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/dataStakingRateLatest",
    ],
    "TradingSignals": [
        "https://developers.coindesk.com/documentation/legacy/TradingSignals/tradingSignalsIntoTheBlockLatest",
    ],
    "PairMapping": [
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingMappedSymbolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeSymbolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/plannedPairRemappingEndpoint",
    ],
    "Toplists": [
        "https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalVolumeEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topTotalTopTierVolumeEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalMktCapEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesFullEndpoint",
    ],
    "Social": [
        "https://developers.coindesk.com/documentation/legacy/Social/latestCoinSocialStats",
        "https://developers.coindesk.com/documentation/legacy/Social/historicalDaySocialStats",
        "https://developers.coindesk.com/documentation/legacy/Social/historicalHourSocialStats",
    ],
    "News": [
        "https://developers.coindesk.com/documentation/legacy/News/latestNewsArticlesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/ListNewsFeedsEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/newsArticleCategoriesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/newsFeedAndCategoriesEndpoint",
    ],
    "OrderBook": [
        "https://developers.coindesk.com/documentation/legacy/Orderbook/exchangesWithOrdebookStaticInfoEndpointV2",
        "https://developers.coindesk.com/documentation/legacy/Orderbook/obL1TopEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Orderbook/obL2SnapshotEndpoint",
    ],
    "GeneralInfo": [
        "https://developers.coindesk.com/documentation/legacy/Other/allExchangesV4Endpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/allIncludedExchangesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesV2Endpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesExcludedEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesAbsentEndpoint",
    ],
    "Helper": [
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalVolumeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/topTotalTopTierVolumeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalMktCapEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopDirectVolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopPriceEndpoint",
    ],
    "Index": [
        "https://developers.coindesk.com/documentation/legacy/Index/listOfIndices",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisIndexValue",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoMinute",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoHour",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoDay",
        "https://developers.coindesk.com/documentation/legacy/Index/listOfUnderlyingIndices",
    ],
}

def fetch_and_parse_doc(url):
    """Fetch documentation and extract endpoint"""
    try:
        print(f"  Fetching: {url.split('/')[-1]}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        text = response.text
        
        # Extract endpoint - look for /data/... patterns
        endpoint = None
        matches = re.findall(r'/data/[a-zA-Z0-9/?=&_-]*', text)
        if matches:
            # Get longest unique match (removes duplicates)
            unique_matches = list(dict.fromkeys(matches))
            endpoint = max(unique_matches, key=len)
            # Clean up query strings
            if '?' in endpoint:
                endpoint = endpoint.split('?')[0]
        
        # Extract title/description
        description = ""
        # Look for title pattern in the text
        title_match = re.search(r'# #([^\n]+)', text)
        if title_match:
            description = title_match.group(1).strip()
        
        # Extract parameter names
        params = []
        param_matches = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_]*)`\(', text)
        if param_matches:
            params = list(dict.fromkeys(param_matches))[:8]
        
        return {
            "url": url,
            "endpoint": endpoint,
            "description": description,
            "params": params,
            "success": endpoint is not None
        }
        
    except Exception as e:
        return {
            "url": url,
            "endpoint": None,
            "description": "",
            "params": [],
            "success": False,
            "error": str(e)
        }

def main():
    print("=" * 80)
    print("CoinDesk/CryptoCompare MinAPI Documentation Scraper")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)
    
    all_results = {}
    all_endpoints = {}
    
    for category, urls in DOCUMENTATION_URLS.items():
        print(f"\n{category}")
        print("-" * 40)
        
        category_results = []
        for url in urls:
            result = fetch_and_parse_doc(url)
            category_results.append(result)
            
            if result['success']:
                print(f"  ✓ {result['endpoint']} - {result['description'][:40]}")
                all_endpoints[result['endpoint']] = {
                    "category": category,
                    "description": result['description'],
                    "params": result['params']
                }
            else:
                print(f"  ✗ {url.split('/')[-1]} - No endpoint found")
        
        all_results[category] = category_results
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total categories: {len(DOCUMENTATION_URLS)}")
    print(f"Total URLs processed: {sum(len(urls) for urls in DOCUMENTATION_URLS.values())}")
    print(f"Endpoints extracted: {len(all_endpoints)}")
    
    # Save results
    results_file = Path(__file__).parent.parent / "documentation_scrape_results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nResults saved to: {results_file}")
    
    # Save endpoint list
    endpoints_file = Path(__file__).parent.parent / "MINAPI_ENUMERATED_ENDPOINTS.json"
    with open(endpoints_file, "w", encoding="utf-8") as f:
        json.dump({"endpoints": all_endpoints}, f, indent=2)
    
    print(f"Endpoints for testing: {endpoints_file}")
    
    # Print all endpoints
    print("\n" + "=" * 80)
    print("ALL ENDPOINTS EXTRACTED")
    print("=" * 80)
    for i, (endpoint, info) in enumerate(sorted(all_endpoints.items()), 1):
        print(f"{i:3}. {endpoint:45} ({info['category']})")
        if info['description']:
            print(f"     {info['description'][:60]}")

if __name__ == "__main__":
    main()
