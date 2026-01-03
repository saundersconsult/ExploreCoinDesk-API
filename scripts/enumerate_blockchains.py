#!/usr/bin/env python3
"""
Enumerate blockchains from CryptoCompare API.

This script fetches the list of blockchains from the CryptoCompare API
and saves it to a file for use in comparisons or as input to other scripts.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional

import requests


def fetch_blockchain_list(api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch the blockchain list from CryptoCompare API.
    
    Args:
        api_key: Optional API key for authentication
        
    Returns:
        API response as dictionary
        
    Raises:
        requests.RequestException: On network or API errors
    """
    url = "https://min-api.cryptocompare.com/data/blockchain/list"
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


def save_as_list(data: Dict[str, Any], output_file: str) -> None:
    """
    Save blockchain symbols as a simple list file (one per line).
    
    Args:
        data: API response data
        output_file: Output file path
    """
    if 'Data' not in data:
        print("Warning: No 'Data' field in response")
        return
    
    blockchains = data['Data']
    symbols = sorted(blockchains.keys())
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for symbol in symbols:
            f.write(f"{symbol}\n")
    
    print(f"✓ Saved {len(symbols)} blockchain symbols to: {output_file}")


def save_as_csv(data: Dict[str, Any], output_file: str) -> None:
    """
    Save blockchain data as CSV file.
    
    Args:
        data: API response data
        output_file: Output file path
    """
    if 'Data' not in data:
        print("Warning: No 'Data' field in response")
        return
    
    blockchains = data['Data']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("symbol,name,blockchain_type\n")
        
        # Write data
        for symbol in sorted(blockchains.keys()):
            info = blockchains[symbol]
            name = info.get('name', '')
            blockchain_type = info.get('blockchain_type', '')
            # Escape commas in fields
            name = name.replace('"', '""')
            blockchain_type = blockchain_type.replace('"', '""')
            f.write(f'{symbol},"{name}","{blockchain_type}"\n')
    
    print(f"✓ Saved {len(blockchains)} blockchains to CSV: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Enumerate blockchains from CryptoCompare API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Save as JSON (default)
  python scripts/enumerate_blockchains.py
  
  # Save as simple list
  python scripts/enumerate_blockchains.py --format list
  
  # Save as CSV
  python scripts/enumerate_blockchains.py --format csv
  
  # Custom output file
  python scripts/enumerate_blockchains.py -o my_blockchains.json
  
  # With API key
  python scripts/enumerate_blockchains.py --api-key YOUR_KEY
        """
    )
    
    parser.add_argument(
        '--format',
        choices=['json', 'list', 'csv'],
        default='json',
        help='Output format (default: json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: blockchain_list_YYYYMMDD.{ext})'
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
        ext_map = {'json': 'json', 'list': 'txt', 'csv': 'csv'}
        ext = ext_map[args.format]
        output_file = f"blockchain_list_{date_str}.{ext}"
    
    try:
        # Fetch data
        print(f"Fetching blockchain list from CryptoCompare API...")
        data = fetch_blockchain_list(api_key)
        
        # Display summary if verbose
        if args.verbose:
            print(f"\nResponse Status: {data.get('Response', 'Unknown')}")
            print(f"Message: {data.get('Message', 'N/A')}")
            if 'Data' in data:
                print(f"Total Blockchains: {len(data['Data'])}")
                print(f"\nSample blockchains:")
                for i, symbol in enumerate(sorted(data['Data'].keys())[:5]):
                    info = data['Data'][symbol]
                    print(f"  {symbol}: {info.get('name', 'N/A')}")
                if len(data['Data']) > 5:
                    print(f"  ... and {len(data['Data']) - 5} more")
            print()
        
        # Save in requested format
        if args.format == 'json':
            pretty = not args.compact
            save_as_json(data, output_file, pretty=pretty)
        elif args.format == 'list':
            save_as_list(data, output_file)
        elif args.format == 'csv':
            save_as_csv(data, output_file)
        
        print(f"\n✓ Success! Blockchain list enumerated and saved.")
        
    except requests.RequestException as e:
        print(f"✗ Error fetching blockchain list: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
