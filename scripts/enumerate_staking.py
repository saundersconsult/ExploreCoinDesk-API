#!/usr/bin/env python3
"""
Enumerate blockchain staking data from CryptoCompare API.

This script fetches staking information for cryptocurrencies and saves it
to a file for use in comparisons or as input to other scripts.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional, List

import requests


def fetch_staking_data(fsym: Optional[str] = None, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch staking data from CryptoCompare API.
    
    Args:
        fsym: Optional cryptocurrency symbol to filter by (e.g., 'BTC', 'ETH')
        api_key: Optional API key for authentication
        
    Returns:
        API response as dictionary
        
    Raises:
        requests.RequestException: On network or API errors
    """
    url = "https://min-api.cryptocompare.com/data/blockchain/staking/latest"
    headers = {}
    params = {}
    
    if api_key:
        headers['authorization'] = f'Apikey {api_key}'
    
    if fsym:
        params['fsym'] = fsym
    
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    
    return response.json()


def fetch_multiple_symbols(symbols: List[str], api_key: Optional[str] = None, verbose: bool = False) -> Dict[str, Any]:
    """
    Fetch staking data for multiple symbols.
    
    Args:
        symbols: List of cryptocurrency symbols
        api_key: Optional API key for authentication
        verbose: Whether to print progress
        
    Returns:
        Dictionary mapping symbols to their staking data
    """
    results = {}
    
    for i, symbol in enumerate(symbols, 1):
        if verbose:
            print(f"Fetching staking data for {symbol} ({i}/{len(symbols)})...")
        
        try:
            data = fetch_staking_data(fsym=symbol, api_key=api_key)
            results[symbol] = data
        except requests.RequestException as e:
            if verbose:
                print(f"  ✗ Error fetching {symbol}: {e}")
            results[symbol] = {"error": str(e)}
    
    return results


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


def save_as_csv(data: Dict[str, Any], output_file: str, multi_symbol: bool = False) -> None:
    """
    Save staking data as CSV file.
    
    Args:
        data: API response data
        output_file: Output file path
        multi_symbol: Whether data contains multiple symbols
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        if multi_symbol:
            # Multiple symbols - different structure
            f.write("symbol,response_status,message,rate,issued_date\n")
            for symbol, symbol_data in data.items():
                if 'error' in symbol_data:
                    f.write(f'{symbol},Error,"{symbol_data["error"]}","",""\n')
                else:
                    response = symbol_data.get('Response', 'Unknown')
                    message = symbol_data.get('Message', '')
                    staking_info = symbol_data.get('Data', {})
                    rate = staking_info.get('rate', '') if isinstance(staking_info, dict) else ''
                    issued_date = staking_info.get('issued_date', '') if isinstance(staking_info, dict) else ''
                    f.write(f'{symbol},{response},"{message}",{rate},"{issued_date}"\n')
        else:
            # Single query or general data
            if 'Data' not in data:
                f.write("rate,issued_ts,issued_date,notes\n")
                f.write('"","","","No staking data available"\n')
                return
            
            staking_info = data['Data']
            
            # Write header
            f.write("rate,issued_ts,issued_date,notes\n")
            
            # Write data
            rate = staking_info.get('rate', '')
            issued_ts = staking_info.get('issued_ts', '')
            issued_date = staking_info.get('issued_date', '')
            notes = '; '.join(staking_info.get('notes', []))
            
            f.write(f'{rate},{issued_ts},"{issued_date}","{notes}"\n')
    
    print(f"✓ Saved CSV to: {output_file}")


def save_as_summary(data: Dict[str, Any], output_file: str, multi_symbol: bool = False) -> None:
    """
    Save a human-readable summary of staking data.
    
    Args:
        data: API response data
        output_file: Output file path
        multi_symbol: Whether data contains multiple symbols
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BLOCKCHAIN STAKING DATA SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        if multi_symbol:
            for symbol, symbol_data in data.items():
                f.write(f"\n{'=' * 80}\n")
                f.write(f"Symbol: {symbol}\n")
                f.write(f"{'=' * 80}\n")
                
                if 'error' in symbol_data:
                    f.write(f"Error: {symbol_data['error']}\n")
                    continue
                
                f.write(f"Response: {symbol_data.get('Response', 'Unknown')}\n")
                f.write(f"Message: {symbol_data.get('Message', 'N/A')}\n")
                
                if 'Data' in symbol_data:
                    staking_info = symbol_data['Data']
                    if isinstance(staking_info, dict):
                        f.write(f"\nStaking Information:\n")
                        f.write(f"  Staking Rate: {staking_info.get('rate', 'N/A')}%\n")
                        f.write(f"  Issued Date: {staking_info.get('issued_date', 'N/A')}\n")
                        f.write(f"  Issued Timestamp: {staking_info.get('issued_ts', 'N/A')}\n")
                        notes = staking_info.get('notes', [])
                        if notes:
                            f.write(f"  Notes: {', '.join(notes)}\n")
        else:
            f.write(f"Response: {data.get('Response', 'Unknown')}\n")
            f.write(f"Message: {data.get('Message', 'N/A')}\n\n")
            
            if 'Data' in data:
                staking_info = data['Data']
                if isinstance(staking_info, dict):
                    f.write("Staking Information:\n")
                    f.write("-" * 80 + "\n")
                    f.write(f"Staking Rate: {staking_info.get('rate', 'N/A')}%\n")
                    f.write(f"Issued Date: {staking_info.get('issued_date', 'N/A')}\n")
                    f.write(f"Issued Timestamp: {staking_info.get('issued_ts', 'N/A')}\n")
                    notes = staking_info.get('notes', [])
                    if notes:
                        f.write(f"\nNotes:\n")
                        for note in notes:
                            f.write(f"  - {note}\n")
    
    print(f"✓ Saved summary to: {output_file}")


def read_symbols_from_file(filepath: str) -> List[str]:
    """
    Read cryptocurrency symbols from a file (one per line).
    
    Args:
        filepath: Path to file containing symbols
        
    Returns:
        List of symbols
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        symbols = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return symbols


def main():
    parser = argparse.ArgumentParser(
        description='Enumerate blockchain staking data from CryptoCompare API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get all staking data
  python scripts/enumerate_staking.py --verbose
  
  # Get staking data for a specific symbol
  python scripts/enumerate_staking.py --fsym BTC --verbose
  
  # Get staking data for multiple symbols from file
  python scripts/enumerate_staking.py --symbols-file blockchain_symbols.txt
  
  # Save as CSV
  python scripts/enumerate_staking.py --fsym ETH --format csv
  
  # Save as summary (human-readable)
  python scripts/enumerate_staking.py --fsym ADA --format summary
  
  # Custom output file
  python scripts/enumerate_staking.py --fsym BTC -o btc_staking.json
        """
    )
    
    parser.add_argument(
        '--fsym',
        help='Cryptocurrency symbol to query (e.g., BTC, ETH, ADA)'
    )
    parser.add_argument(
        '--symbols-file',
        help='File containing cryptocurrency symbols (one per line)'
    )
    parser.add_argument(
        '--format',
        choices=['json', 'csv', 'summary'],
        default='json',
        help='Output format (default: json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: staking_data_YYYYMMDD.{ext})'
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
        help='Print detailed progress information'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.fsym and args.symbols_file:
        print("Error: Cannot specify both --fsym and --symbols-file", file=sys.stderr)
        sys.exit(1)
    
    # Get API key from args or environment
    api_key = args.api_key or os.environ.get('CRYPTOCOMPARE_API_KEY')
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        date_str = datetime.now().strftime('%Y%m%d')
        ext_map = {'json': 'json', 'csv': 'csv', 'summary': 'txt'}
        ext = ext_map[args.format]
        if args.fsym:
            output_file = f"staking_{args.fsym.lower()}_{date_str}.{ext}"
        elif args.symbols_file:
            output_file = f"staking_multi_{date_str}.{ext}"
        else:
            output_file = f"staking_all_{date_str}.{ext}"
    
    try:
        # Fetch data based on input method
        if args.symbols_file:
            # Read symbols from file and fetch data for each
            print(f"Reading symbols from: {args.symbols_file}")
            symbols = read_symbols_from_file(args.symbols_file)
            print(f"Found {len(symbols)} symbols to query\n")
            
            data = fetch_multiple_symbols(symbols, api_key=api_key, verbose=args.verbose)
            multi_symbol = True
            
        elif args.fsym:
            # Single symbol query
            if args.verbose:
                print(f"Fetching staking data for: {args.fsym}")
            data = fetch_staking_data(fsym=args.fsym, api_key=api_key)
            multi_symbol = False
            
        else:
            # No symbol specified - get all staking data
            if args.verbose:
                print("Fetching all staking data...")
            data = fetch_staking_data(api_key=api_key)
            multi_symbol = False
        
        # Display summary if verbose
        if args.verbose and not args.symbols_file:
            print(f"\nResponse Status: {data.get('Response', 'Unknown')}")
            print(f"Message: {data.get('Message', 'N/A')}")
            if 'Data' in data:
                staking_info = data['Data']
                if isinstance(staking_info, dict):
                    print(f"\nStaking Information:")
                    print(f"  Rate: {staking_info.get('rate', 'N/A')}%")
                    print(f"  Issued: {staking_info.get('issued_date', 'N/A')}")
                    notes = staking_info.get('notes', [])
                    if notes:
                        print(f"  Notes: {', '.join(notes)}")
            print()
        
        # Save in requested format
        if args.format == 'json':
            pretty = not args.compact
            save_as_json(data, output_file, pretty=pretty)
        elif args.format == 'csv':
            save_as_csv(data, output_file, multi_symbol=multi_symbol)
        elif args.format == 'summary':
            save_as_summary(data, output_file, multi_symbol=multi_symbol)
        
        print(f"\n✓ Success! Staking data enumerated and saved.")
        
    except FileNotFoundError as e:
        print(f"✗ Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"✗ Error fetching staking data: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
