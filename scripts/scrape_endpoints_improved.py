#!/usr/bin/env python3
"""
Improved scraper for CoinDesk/CryptoCompare MinAPI documentation.
Extracts endpoints from the documented pages by looking for specific text patterns.
"""

import requests
import json
import re
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import time

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

def extract_endpoint_from_text(text):
    """
    Extract endpoint path from the documentation text.
    Looking for pattern: /data/... in various contexts
    """
    # Pattern 1: "URL /data/..." (most common in docs)
    match = re.search(r'URL\s+(/data/[^\s?&"\'\)]+)', text)
    if match:
        return match.group(1)
    
    # Pattern 2: Direct /data/ path at start of line
    match = re.search(r'^[ \t]*(/data/[^\s?&"\'\)]+)', text, re.MULTILINE)
    if match:
        return match.group(1)
    
    # Pattern 3: In backticks
    match = re.search(r'`(/data/[^\s`]+)`', text)
    if match:
        return match.group(1)
    
    # Pattern 4: In code block
    match = re.search(r'https://min-api\.cryptocompare\.com(/data/[^\s?&"\'\)]+)', text)
    if match:
        return match.group(1)
    
    # Pattern 5: Anywhere in /data/... form (greedy for endpoint)
    matches = re.findall(r'/data/[a-zA-Z0-9/_-]+', text)
    if matches:
        # Return longest match (most specific endpoint)
        return max(matches, key=len)
    
    return None

def extract_title(text):
    """Extract the endpoint title/description."""
    # Look for markdown headers
    match = re.search(r'# #([^\n]+)', text)
    if match:
        return match.group(1).strip()
    
    # Look for the first substantial text
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line and len(line) > 10 and not line.startswith('http'):
            return line
    
    return "Unknown"

def extract_method(text):
    """Extract HTTP method from documentation."""
    # Look for GET or POST
    if re.search(r'\bGET\b', text):
        return "GET"
    if re.search(r'\bPOST\b', text):
        return "POST"
    return "GET"  # Default

def extract_parameters(text):
    """Extract parameter names from documentation."""
    params = set()
    
    # Pattern 1: `param`(type)
    matches = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_]*)`\s*\(', text)
    params.update(matches)
    
    # Pattern 2: param(type)*required
    matches = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*\*', text)
    params.update(matches)
    
    # Pattern 3: In URL examples
    matches = re.findall(r'[?&]([a-zA-Z_][a-zA-Z0-9_]*)=', text)
    params.update(matches)
    
    return sorted(list(params))

def scrape_documentation():
    """Scrape all documentation URLs and extract endpoints."""
    results = {}
    total = sum(len(urls) for urls in DOCUMENTATION_URLS.values())
    current = 0
    
    for category, urls in DOCUMENTATION_URLS.items():
        print(f"\n{'='*60}")
        print(f"Category: {category}")
        print(f"{'='*60}")
        
        results[category] = []
        
        for url in urls:
            current += 1
            print(f"\n[{current}/{total}] Fetching: {url.split('/')[-2]}")
            
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                text = response.text
                
                # Extract components
                endpoint = extract_endpoint_from_text(text)
                title = extract_title(text)
                method = extract_method(text)
                params = extract_parameters(text)
                
                if endpoint:
                    result = {
                        "endpoint": endpoint,
                        "title": title,
                        "method": method,
                        "parameters": params,
                        "url": url,
                        "status": "[OK] Found"
                    }
                    results[category].append(result)
                    print(f"[OK] Found: {endpoint}")
                    print(f"   Title: {title}")
                    print(f"   Params: {', '.join(params[:5]) if params else 'None'}")
                else:
                    result = {
                        "endpoint": None,
                        "title": title,
                        "url": url,
                        "status": "[FAIL] Not found"
                    }
                    results[category].append(result)
                    print(f"[FAIL] Endpoint not found")
                
                time.sleep(0.5)  # Rate limiting
                
            except Exception as e:
                print(f"[ERROR] {str(e)}")
                results[category].append({
                    "url": url,
                    "status": f"[ERROR] {str(e)}"
                })
    
    return results

def main():
    print("CryptoCompare MinAPI Documentation Scraper")
    print("=" * 60)
    
    results = scrape_documentation()
    
    # Save results
    output_file = Path("documentation_scrape_results.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}\n")
    
    total_found = 0
    for category, endpoints in results.items():
        found = sum(1 for e in endpoints if e.get("endpoint"))
        total_found += found
        print(f"{category}: {found}/{len(endpoints)} endpoints found")
    
    print(f"\nTotal: {total_found}/{sum(len(u) for u in DOCUMENTATION_URLS.values())} endpoints found")
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()
