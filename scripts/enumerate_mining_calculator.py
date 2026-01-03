#!/usr/bin/env python3
"""
Enumerate mining calculator data from CryptoCompare API.

Fetches blockchain mining calculator stats (hashrate, block reward, price, etc.)
for one or multiple cryptocurrencies and saves in JSON, CSV, or summary format.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, List, Optional

import requests


API_URL = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator"


def fetch_mining_data(fsyms: List[str], tsyms: List[str], api_key: Optional[str] = None) -> Dict[str, Any]:
    """Fetch mining calculator data for symbols and target currencies."""
    headers = {}
    if api_key:
        headers["authorization"] = f"Apikey {api_key}"

    params = {
        "fsyms": ",".join(fsyms),
        "tsyms": ",".join(tsyms),
    }

    response = requests.get(API_URL, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_as_json(data: Dict[str, Any], output_file: str, pretty: bool = True) -> None:
    with open(output_file, "w", encoding="utf-8") as f:
        if pretty:
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(data, f, ensure_ascii=False)
    print(f"✓ Saved JSON to: {output_file}")


def save_as_csv(data: Dict[str, Any], output_file: str, tsyms: List[str]) -> None:
    if "Data" not in data:
        print("Warning: No 'Data' field in response")
        return

    records = data["Data"]

    # Build header
    price_headers = [f"price_{tsym}" for tsym in tsyms]
    header = [
        "symbol",
        "full_name",
        "block_height",
        "block_time_seconds",
        "block_reward",
        "net_hashes_per_second",
        "total_coins_mined",
        "max_supply",
        "asset_launch_date",
    ] + price_headers

    lines = ["{}\n".format(",".join(header))]

    for symbol, info in records.items():
        coin_info = info.get("CoinInfo", {}) if isinstance(info, dict) else {}
        price_info = info.get("Price", {}) if isinstance(info, dict) else {}

        row = [
            coin_info.get("Name", symbol),
            coin_info.get("FullName", ""),
            str(coin_info.get("BlockNumber", "")),
            str(coin_info.get("BlockTime", "")),
            str(coin_info.get("BlockReward", "")),
            str(coin_info.get("NetHashesPerSecond", "")),
            str(coin_info.get("TotalCoinsMined", "")),
            str(coin_info.get("MaxSupply", "")),
            coin_info.get("AssetLaunchDate", ""),
        ]

        for tsym in tsyms:
            row.append(str(price_info.get(tsym, "")))

        # Escape commas in FullName
        row[1] = row[1].replace('"', '""')
        line = ",".join([f'"{cell}"' if "," in cell else cell for cell in row])
        lines.append(line + "\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"✓ Saved CSV to: {output_file}")


def save_as_summary(data: Dict[str, Any], output_file: str, tsyms: List[str]) -> None:
    if "Data" not in data:
        print("Warning: No 'Data' field in response")
        return

    records = data["Data"]
    total_symbols = len(records)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MINING CALCULATOR SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Total Symbols: {total_symbols}\n")
        f.write(f"Target Currencies: {', '.join(tsyms)}\n\n")

        f.write("Sample (first 5):\n")
        f.write("-" * 80 + "\n")

        for idx, (symbol, info) in enumerate(sorted(records.items())[:5]):
            coin_info = info.get("CoinInfo", {}) if isinstance(info, dict) else {}
            price_info = info.get("Price", {}) if isinstance(info, dict) else {}

            f.write(f"\n{symbol}: {coin_info.get('FullName', '')}\n")
            f.write(f"  Block Height: {coin_info.get('BlockNumber', 'N/A')}\n")
            f.write(f"  Block Time (s): {coin_info.get('BlockTime', 'N/A')}\n")
            f.write(f"  Block Reward: {coin_info.get('BlockReward', 'N/A')}\n")
            f.write(f"  Hashrate: {coin_info.get('NetHashesPerSecond', 'N/A')}\n")
            f.write(f"  Total Coins Mined: {coin_info.get('TotalCoinsMined', 'N/A')}\n")
            f.write(f"  Max Supply: {coin_info.get('MaxSupply', 'N/A')}\n")
            f.write(f"  Launch Date: {coin_info.get('AssetLaunchDate', 'N/A')}\n")
            for tsym in tsyms:
                f.write(f"  Price {tsym}: {price_info.get(tsym, 'N/A')}\n")

            if idx >= 4:
                break

        if total_symbols > 5:
            f.write(f"\n... and {total_symbols - 5} more symbols\n")

    print(f"✓ Saved summary to: {output_file}")


def read_symbols_from_file(filepath: str) -> List[str]:
    with open(filepath, "r", encoding="utf-8") as f:
        symbols = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return symbols


def main():
    parser = argparse.ArgumentParser(
        description="Enumerate mining calculator data from CryptoCompare API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single symbol
  python scripts/enumerate_mining_calculator.py --fsyms XMR --tsyms USD --verbose

  # Multiple symbols
  python scripts/enumerate_mining_calculator.py --fsyms BTC,ETH,XMR --tsyms USD

  # Symbols from file
  python scripts/enumerate_mining_calculator.py --symbols-file mining_symbols.txt --tsyms USD,EUR

  # CSV output
  python scripts/enumerate_mining_calculator.py --fsyms BTC,ETH --format csv

  # Summary report
  python scripts/enumerate_mining_calculator.py --symbols-file mining_symbols.txt --format summary
        """,
    )

    parser.add_argument(
        "--fsyms",
        help="Comma-separated list of from-symbols (e.g., BTC,ETH,XMR)",
    )
    parser.add_argument(
        "--symbols-file",
        help="File containing symbols (one per line)",
    )
    parser.add_argument(
        "--tsyms",
        default="USD",
        help="Comma-separated list of target currencies (default: USD)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv", "summary"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: mining_calc_YYYYMMDD.{ext})",
    )
    parser.add_argument(
        "--api-key",
        help="CryptoCompare API key (or set CRYPTOCOMPARE_API_KEY env var)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print JSON output (default: True)",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Compact JSON output (no pretty-printing)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print summary information",
    )

    args = parser.parse_args()

    # Validate symbol inputs
    if not args.fsyms and not args.symbols_file:
        print("Error: Must specify --fsyms or --symbols-file", file=sys.stderr)
        sys.exit(1)

    if args.fsyms and args.symbols_file:
        print("Error: Cannot specify both --fsyms and --symbols-file", file=sys.stderr)
        sys.exit(1)

    # Prepare symbol lists
    if args.symbols_file:
        symbols = read_symbols_from_file(args.symbols_file)
    else:
        symbols = [s.strip() for s in args.fsyms.split(",") if s.strip()]

    if not symbols:
        print("Error: No symbols provided", file=sys.stderr)
        sys.exit(1)

    # Prepare target currencies
    tsyms = [s.strip() for s in args.tsyms.split(",") if s.strip()]
    if not tsyms:
        print("Error: No target currencies provided", file=sys.stderr)
        sys.exit(1)

    # Determine output file
    if args.output:
        output_file = args.output
    else:
        date_str = datetime.now().strftime("%Y%m%d")
        ext_map = {"json": "json", "csv": "csv", "summary": "txt"}
        ext = ext_map[args.format]
        suffix = "file" if args.symbols_file else "inline"
        output_file = f"mining_calc_{suffix}_{date_str}.{ext}"

    # API key
    api_key = args.api_key or os.environ.get("CRYPTOCOMPARE_API_KEY")

    try:
        if args.verbose:
            print(f"Fetching mining calculator data for: {', '.join(symbols)}")
            print(f"Target currencies: {', '.join(tsyms)}")

        data = fetch_mining_data(symbols, tsyms, api_key=api_key)

        if args.verbose:
            print(f"\nResponse Status: {data.get('Response', 'Unknown')}")
            if "Data" in data:
                print(f"Total Symbols Returned: {len(data['Data'])}")
                sample_symbol = next(iter(data["Data"]), None)
                if sample_symbol:
                    info = data["Data"][sample_symbol]
                    coin_info = info.get("CoinInfo", {}) if isinstance(info, dict) else {}
                    price_info = info.get("Price", {}) if isinstance(info, dict) else {}
                    print(f"Sample: {sample_symbol} - {coin_info.get('FullName', '')}")
                    for tsym in tsyms:
                        print(f"  Price {tsym}: {price_info.get(tsym, 'N/A')}")
            print()

        # Save
        if args.format == "json":
            pretty = not args.compact
            save_as_json(data, output_file, pretty=pretty)
        elif args.format == "csv":
            save_as_csv(data, output_file, tsyms)
        elif args.format == "summary":
            save_as_summary(data, output_file, tsyms)

        print("\n✓ Success! Mining calculator data enumerated and saved.")

    except FileNotFoundError as e:
        print(f"✗ Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"✗ Error fetching mining calculator data: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
