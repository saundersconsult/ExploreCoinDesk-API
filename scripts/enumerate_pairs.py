#!/usr/bin/env python3
"""
Enumerate trading pairs from CryptoCompare CCCAGG API.

This script fetches the list of trading pairs and their available markets
from the CryptoCompare API and saves it to a file for use in comparisons
or as input to other scripts.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional

import requests


def fetch_pairs_data(api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch trading pairs data from CryptoCompare API.
    
    Args:
        api_key: Optional API key for authentication
        
    Returns:
        API response as dictionary
        
    Raises:
        requests.RequestException: On network or API errors
    """
    url = "https://min-api.cryptocompare.com/data/cccagg/pairs"
    headers = {}
    
    if api_key:
        headers['authorization'] = f'Apikey {api_key}'
    
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    
    return response.json()


def save_as_json(data: Dict[str, Any], output_file: str, pretty: bool = True) -> None:
    """
    Save data as JSON file.
    
    Args:
        data: Data to save
        output_file: Output file path
        pretty: Whether to pretty-print the JSON
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(data, f, ensure_ascii=False)
    print(f"✓ Saved JSON to: {output_file}")


def save_as_csv(data: Dict[str, Any], output_file: str) -> None:
    """
    Save pairs data as CSV file.
    
    Args:
        data: API response data
        output_file: Output file path
    """
    if 'Data' not in data:
        print("Warning: No 'Data' field in response")
        return
    
    pairs_data = data['Data']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("base_symbol,quote_symbol,markets_count,markets\n")
        
        # Process each base symbol
        for base_symbol, quote_data in pairs_data.items():
            for quote_symbol, info in quote_data.items():
                markets = info.get('markets', [])
                markets_str = ';'.join(markets)  # Use semicolon to avoid CSV conflicts
                f.write(f'"{base_symbol}","{quote_symbol}",{len(markets)},"{markets_str}"\n')
    
    print(f"✓ Saved trading pairs to CSV: {output_file}")


def save_as_summary(data: Dict[str, Any], output_file: str) -> None:
    """
    Save a human-readable summary of pairs data.
    
    Args:
        data: API response data
        output_file: Output file path
    """
    if 'Data' not in data:
        print("Warning: No 'Data' field in response")
        return
    
    pairs_data = data['Data']
    
    # Calculate statistics
    total_base_symbols = len(pairs_data)
    total_pairs = sum(len(quote_data) for quote_data in pairs_data.values())
    all_markets = set()
    
    for base_symbol, quote_data in pairs_data.items():
        for quote_symbol, info in quote_data.items():
            all_markets.update(info.get('markets', []))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("TRADING PAIRS SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Total Base Symbols: {total_base_symbols}\n")
        f.write(f"Total Trading Pairs: {total_pairs}\n")
        f.write(f"Total Unique Markets: {len(all_markets)}\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("AVAILABLE MARKETS\n")
        f.write("=" * 80 + "\n")
        for market in sorted(all_markets):
            f.write(f"  - {market}\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("SAMPLE TRADING PAIRS (First 20)\n")
        f.write("=" * 80 + "\n\n")
        
        count = 0
        for base_symbol in sorted(pairs_data.keys())[:20]:
            quote_data = pairs_data[base_symbol]
            f.write(f"\n{base_symbol}:\n")
            for quote_symbol, info in quote_data.items():
                markets = info.get('markets', [])
                f.write(f"  → {quote_symbol}: {len(markets)} market(s) - {', '.join(markets[:5])}")
                if len(markets) > 5:
                    f.write(f" ... and {len(markets) - 5} more")
                f.write("\n")
            count += 1
        
        if total_base_symbols > 20:
            f.write(f"\n... and {total_base_symbols - 20} more base symbols\n")
    
    print(f"✓ Saved summary to: {output_file}")


def save_markets_list(data: Dict[str, Any], output_file: str) -> None:
    """
    Save unique list of markets (exchanges).
    
    Args:
        data: API response data
        output_file: Output file path
    """
    if 'Data' not in data:
        print("Warning: No 'Data' field in response")
        return
    
    pairs_data = data['Data']
    all_markets = set()
    
    for base_symbol, quote_data in pairs_data.items():
        for quote_symbol, info in quote_data.items():
            all_markets.update(info.get('markets', []))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for market in sorted(all_markets):
            f.write(f"{market}\n")
    
    print(f"✓ Saved {len(all_markets)} unique markets to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Enumerate trading pairs from CryptoCompare CCCAGG API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Save as JSON (default)
  python scripts/enumerate_pairs.py --verbose
  
  # Save as CSV
  python scripts/enumerate_pairs.py --format csv
  
  # Generate summary report
  python scripts/enumerate_pairs.py --format summary
  
  # Extract unique markets list
  python scripts/enumerate_pairs.py --markets-only -o markets.txt
  
  # Custom output file
  python scripts/enumerate_pairs.py -o my_pairs.json
  
  # With API key
  python scripts/enumerate_pairs.py --api-key YOUR_KEY
        """
    )
    
    parser.add_argument(
        '--format',
        choices=['json', 'csv', 'summary'],
        default='json',
        help='Output format (default: json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: pairs_YYYYMMDD.{ext})'
    )
    parser.add_argument(
        '--api-key',
        help='CryptoCompare API key (or set CRYPTOCOMPARE_API_KEY env var)'
    )
    parser.add_argument(
        '--pretty',
        action='store_true',
        default=True,
        help='Pretty-print JSON output (default: True)'
    )
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Compact JSON output (no pretty-printing)'
    )
    parser.add_argument(
        '--markets-only',
        action='store_true',
        help='Save only unique market names (one per line)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print summary information'
    )
    
    args = parser.parse_args()
    
    # Get API key from args or environment
    api_key = args.api_key or os.environ.get('CRYPTOCOMPARE_API_KEY')
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        date_str = datetime.now().strftime('%Y%m%d')
        if args.markets_only:
            output_file = f"markets_list_{date_str}.txt"
        else:
            ext_map = {'json': 'json', 'csv': 'csv', 'summary': 'txt'}
            ext = ext_map[args.format]
            output_file = f"pairs_{date_str}.{ext}"
    
    try:
        # Fetch data
        print(f"Fetching trading pairs from CryptoCompare API...")
        data = fetch_pairs_data(api_key)
        
        # Display summary if verbose
        if args.verbose:
            print(f"\nResponse Status: {data.get('Response', 'Unknown')}")
            print(f"Message: {data.get('Message', 'N/A')}")
            if 'Data' in data:
                pairs_data = data['Data']
                total_base = len(pairs_data)
                total_pairs = sum(len(quote_data) for quote_data in pairs_data.values())
                
                # Count unique markets
                all_markets = set()
                for base_symbol, quote_data in pairs_data.items():
                    for quote_symbol, info in quote_data.items():
                        all_markets.update(info.get('markets', []))
                
                print(f"Total Base Symbols: {total_base}")
                print(f"Total Trading Pairs: {total_pairs}")
                print(f"Unique Markets: {len(all_markets)}")
                
                print(f"\nSample pairs:")
                count = 0
                for base in sorted(pairs_data.keys())[:3]:
                    for quote in list(pairs_data[base].keys())[:2]:
                        markets = pairs_data[base][quote].get('markets', [])
                        print(f"  {base}/{quote}: {len(markets)} market(s)")
                        count += 1
                        if count >= 5:
                            break
                    if count >= 5:
                        break
                print(f"  ... and {total_pairs - count} more pairs")
            print()
        
        # Save in requested format
        if args.markets_only:
            save_markets_list(data, output_file)
        elif args.format == 'json':
            pretty = not args.compact
            save_as_json(data, output_file, pretty=pretty)
        elif args.format == 'csv':
            save_as_csv(data, output_file)
        elif args.format == 'summary':
            save_as_summary(data, output_file)
        
        print(f"\n✓ Success! Trading pairs data enumerated and saved.")
        
    except requests.RequestException as e:
        print(f"✗ Error fetching trading pairs: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
