#!/usr/bin/env python3
"""
Poll CryptoCompare Trading Signals endpoint and log results.
Logs to CSV or JSON format with date-based filenames.
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests


def get_log_filename(script_name: str, log_format: str = "csv") -> Path:
    """Generate log filename with date: scriptname-YYYY-MMDD-apis.log"""
    today = datetime.now().strftime("%Y-%m%d")
    base_name = Path(script_name).stem
    filename = f"{base_name}-{today}-apis.log"
    return Path(__file__).parent / filename


def poll_endpoint(api_key: str = None) -> dict:
    """
    Poll the IntoTheBlock trading signals endpoint.
    
    Args:
        api_key: Optional API key for authentication
        
    Returns:
        dict: API response data
    """
    url = "https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest"
    
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key
    
    params = {
        "fsym": "BTC",  # Default to Bitcoin, can be parameterized
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat(),
            "success": False
        }


def log_as_csv(data: dict, log_file: Path):
    """
    Log data to CSV format.
    
    Args:
        data: Response data to log
        log_file: Path to log file
    """
    # Flatten the data structure for CSV
    timestamp = datetime.now().isoformat()
    
    # Extract relevant fields from response
    row = {
        "timestamp": timestamp,
        "success": data.get("Response") != "Error",
        "message": data.get("Message", ""),
    }
    
    # If there's actual data, extract it
    if "Data" in data:
        signal_data = data["Data"]
        if isinstance(signal_data, dict):
            # Flatten nested structure
            for key, value in signal_data.items():
                if isinstance(value, (dict, list)):
                    row[key] = json.dumps(value)
                else:
                    row[key] = value
    
    # If there's an error
    if "error" in data:
        row["error"] = data["error"]
    
    # Check if file exists to determine if we need headers
    file_exists = log_file.exists()
    
    # Write to CSV
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
    
    print(f"✓ Logged to CSV: {log_file}")


def log_as_json(data: dict, log_file: Path):
    """
    Log data to JSON format (JSONL - one JSON object per line).
    
    Args:
        data: Response data to log
        log_file: Path to log file
    """
    timestamp = datetime.now().isoformat()
    
    # Create log entry with timestamp
    log_entry = {
        "timestamp": timestamp,
        "data": data
    }
    
    # Append as JSONL (one JSON object per line)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    print(f"✓ Logged to JSON: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Poll CryptoCompare Trading Signals endpoint and log results"
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Output format (default: csv)"
    )
    parser.add_argument(
        "--api-key",
        help="API key for authentication (or set CRYPTOCOMPARE_API_KEY env var)"
    )
    parser.add_argument(
        "--fsym",
        default="BTC",
        help="From symbol (default: BTC)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print response data"
    )
    
    args = parser.parse_args()
    
    # Get API key from args or environment
    api_key = args.api_key or os.getenv("CRYPTOCOMPARE_API_KEY")
    
    if not api_key:
        print("⚠ Warning: No API key provided. Request may fail or be rate-limited.")
        print("  Set CRYPTOCOMPARE_API_KEY environment variable or use --api-key")
        print()
    
    # Generate log filename
    log_file = get_log_filename(__file__, args.format)
    
    print(f"Polling: https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest")
    print(f"Symbol: {args.fsym}")
    print(f"Log file: {log_file}")
    print()
    
    # Poll the endpoint
    data = poll_endpoint(api_key)
    
    # Display response if verbose
    if args.verbose:
        print("Response:")
        print(json.dumps(data, indent=2))
        print()
    
    # Log based on format
    if args.format == "csv":
        log_as_csv(data, log_file)
    else:
        log_as_json(data, log_file)
    
    # Check for errors
    if data.get("Response") == "Error" or "error" in data:
        print(f"✗ Error: {data.get('Message') or data.get('error')}")
        sys.exit(1)
    else:
        print("✓ Success")


if __name__ == "__main__":
    main()
