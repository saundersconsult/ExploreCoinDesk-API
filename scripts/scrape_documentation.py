#!/usr/bin/env python3
"""
Scrape CoinDesk/CryptoCompare MinAPI documentation to extract endpoint specifications.
This script fetches all documentation URLs and extracts endpoint paths, parameters, and details.
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple
import re

# Documentation URLs from GitHub issue #12
DOCUMENTATION_URLS = {
    # Price
    "Price": [
        "https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/",
        "https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsPriceEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsFullPriceEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Price/generateAverageEndpoint",
    ],
    # Historical
    "Historical": [
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistoday",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistohour",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataHistominute",
        "https://developers.coindesk.com/documentation/legacy/Historical/dailyMarketClose",
        "https://developers.coindesk.com/documentation/legacy/Historical/DailyHistoMinute",
        "https://developers.coindesk.com/documentation/legacy/Historical/dataPriceHistorical",
    ],
    # Blockchain
    "Blockchain": [
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainListOfCoins",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainLatest",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainDay",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionLatest",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionDay",
        "https://developers.coindesk.com/documentation/legacy/Blockchain/dataStakingRateLatest",
    ],
    # Trading Signals
    "TradingSignals": [
        "https://developers.coindesk.com/documentation/legacy/TradingSignals/tradingSignalsIntoTheBlockLatest",
    ],
    # Pair Mapping
    "PairMapping": [
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingMappedSymbolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeSymbolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/PairMapping/plannedPairRemappingEndpoint",
    ],
    # Toplists
    "Toplists": [
        "https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalVolumeEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topTotalTopTierVolumeEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalMktCapEndpointFull",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesFullEndpoint",
    ],
    # Social Data
    "Social": [
        "https://developers.coindesk.com/documentation/legacy/Social/latestCoinSocialStats",
        "https://developers.coindesk.com/documentation/legacy/Social/historicalDaySocialStats",
        "https://developers.coindesk.com/documentation/legacy/Social/historicalHourSocialStats",
    ],
    # News
    "News": [
        "https://developers.coindesk.com/documentation/legacy/News/latestNewsArticlesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/ListNewsFeedsEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/newsArticleCategoriesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/News/newsFeedAndCategoriesEndpoint",
    ],
    # Order Book
    "OrderBook": [
        "https://developers.coindesk.com/documentation/legacy/Orderbook/exchangesWithOrdebookStaticInfoEndpointV2",
        "https://developers.coindesk.com/documentation/legacy/Orderbook/obL1TopEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Orderbook/obL2SnapshotEndpoint",
    ],
    # General Info
    "GeneralInfo": [
        "https://developers.coindesk.com/documentation/legacy/Other/allExchangesV4Endpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/allIncludedExchangesEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesV2Endpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesExcludedEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Other/cccaggPairsAndExchangesAbsentEndpoint",
    ],
    # Helper/Streaming
    "Helper": [
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalVolumeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/topTotalTopTierVolumeEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalMktCapEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopDirectVolEndpoint",
        "https://developers.coindesk.com/documentation/legacy/Streaming/TopPriceEndpoint",
    ],
    # Index
    "Index": [
        "https://developers.coindesk.com/documentation/legacy/Index/listOfIndices",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisIndexValue",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoMinute",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoHour",
        "https://developers.coindesk.com/documentation/legacy/Index/mvisHistoDay",
        "https://developers.coindesk.com/documentation/legacy/Index/listOfUnderlyingIndices",
    ],
}

def fetch_and_parse_doc(url: str) -> Dict:
    """Fetch a documentation page and extract endpoint details"""
    print(f"  Fetching: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract endpoint path (look for /data/... patterns)
        endpoint = None
        params = []
        description = ""
        method = "GET"
        
        # Look for endpoint path in code blocks or specific patterns
        for tag in soup.find_all(['code', 'pre']):
            text = tag.get_text()
            # Look for /data/ endpoints
            if '/data/' in text:
                # Extract endpoint path
                match = re.search(r'/data/[a-zA-Z0-9/]*', text)
                if match:
                    endpoint = match.group(0)
                    break
        
        # Try to extract from method signatures
        if not endpoint:
            for tag in soup.find_all('span', {'class': ['method-name', 'endpoint']}):
                text = tag.get_text()
                if '/data/' in text:
                    endpoint = text.strip()
                    break
        
        # Extract description/title
        title = soup.find('h1')
        if title:
            description = title.get_text().strip()
        else:
            # Try h2 or h3
            for tag in soup.find_all(['h2', 'h3']):
                text = tag.get_text().strip()
                if text and not text.startswith('Parameters') and not text.startswith('Response'):
                    description = text
                    break
        
        # Look for parameters
        for tag in soup.find_all(['li', 'div']):
            text = tag.get_text()
            if 'required' in text.lower() or 'param' in text.lower():
                params.append(text.strip()[:100])
        
        return {
            "url": url,
            "endpoint": endpoint,
            "description": description,
            "method": method,
            "params": params[:5],  # Keep first 5 params
            "success": endpoint is not None
        }
    
    except requests.RequestException as e:
        return {
            "url": url,
            "endpoint": None,
            "description": "",
            "method": "GET",
            "params": [],
            "success": False,
            "error": str(e)
        }

def main():
    """Main scraping function"""
    print("=" * 80)
    print("CoinDesk/CryptoCompare MinAPI Documentation Scraper")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)
    
    all_results = {}
    all_endpoints = []
    
    # Process each category
    for category, urls in DOCUMENTATION_URLS.items():
        print(f"\n{'='*80}")
        print(f"Category: {category}")
        print(f"{'='*80}")
        
        category_results = []
        for url in urls:
            result = fetch_and_parse_doc(url)
            category_results.append(result)
            
            if result['success']:
                print(f"  ✓ {result['endpoint']} - {result['description'][:50]}")
                all_endpoints.append(result['endpoint'])
            else:
                print(f"  ✗ Failed to extract endpoint from {url.split('/')[-1]}")
        
        all_results[category] = category_results
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total categories: {len(DOCUMENTATION_URLS)}")
    print(f"Total documentation URLs: {sum(len(urls) for urls in DOCUMENTATION_URLS.values())}")
    print(f"Endpoints extracted: {len([e for e in all_endpoints if e])}")
    print(f"Unique endpoints: {len(set(all_endpoints))}")
    
    # Save results
    results_file = Path(__file__).parent.parent / "documentation_scrape_results.json"
    with open(results_file, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nDetailed results saved to: {results_file}")
    
    # Generate endpoint list for testing
    endpoints_to_test = {}
    for endpoint in sorted(set(all_endpoints)):
        if endpoint:
            endpoints_to_test[endpoint] = {
                "description": "",
                "params": {}
            }
    
    endpoints_file = Path(__file__).parent.parent / "minapi_endpoints_to_test.json"
    with open(endpoints_file, "w") as f:
        json.dump(endpoints_to_test, f, indent=2)
    
    print(f"Endpoints for testing: {endpoints_file}")
    
    # Print unique endpoints found
    print("\n" + "=" * 80)
    print("ENDPOINTS EXTRACTED")
    print("=" * 80)
    for i, endpoint in enumerate(sorted(set(all_endpoints)), 1):
        if endpoint:
            print(f"{i}. {endpoint}")

if __name__ == "__main__":
    main()
