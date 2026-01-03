"""
CoinDesk Derivatives Probe
Tests futures, options, and perpetual swap endpoints
"""
import sys
import json
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api_client import CoinDeskClient, DEFAULT_API_KEY


def summarize_response(data, name="Response"):
    """Summarize API response data"""
    if not data:
        return f"{name}: None"
    
    if isinstance(data, dict):
        keys = list(data.keys())
        return f"{name}: dict with keys {keys}"
    elif isinstance(data, list):
        count = len(data)
        if count > 0 and isinstance(data[0], dict):
            sample_keys = list(data[0].keys())
            return f"{name}: list of {count} items, sample keys: {sample_keys}"
        return f"{name}: list of {count} items"
    else:
        return f"{name}: {type(data).__name__}"


def test_derivatives_endpoints(client: CoinDeskClient, instruments: list):
    """Test derivatives endpoints"""
    
    print("\n" + "="*80)
    print("COINDESK DERIVATIVES API EXPLORATION")
    print("="*80)
    
    endpoints = [
        # Futures
        {
            "name": "Futures Markets",
            "path": "/futures/v1/markets",
            "params": {},
            "description": "List of available futures markets"
        },
        {
            "name": "Futures Instruments",
            "path": "/futures/v1/markets/instruments",
            "params": {"market": "binance"},
            "description": "Futures instruments for market"
        },
        {
            "name": "Futures Latest Tick",
            "path": "/futures/v1/latest/tick",
            "params": {"market": "binance", "instruments": ",".join(instruments)},
            "description": "Latest futures tick data"
        },
        {
            "name": "Futures Historical Hours",
            "path": "/futures/v1/historical/hours",
            "params": {"market": "binance", "instrument": instruments[0], "limit": 10},
            "description": "Historical hourly futures data"
        },
        {
            "name": "Futures Historical Days",
            "path": "/futures/v1/historical/days",
            "params": {"market": "binance", "instrument": instruments[0], "limit": 10},
            "description": "Historical daily futures data"
        },
        # Options
        {
            "name": "Options Markets",
            "path": "/options/v1/markets",
            "params": {},
            "description": "List of available options markets"
        },
        {
            "name": "Options Instruments",
            "path": "/options/v1/markets/instruments",
            "params": {"market": "deribit"},
            "description": "Options instruments for market"
        },
        {
            "name": "Options Latest Tick",
            "path": "/options/v1/latest/tick",
            "params": {"market": "deribit", "instruments": "BTC-PERPETUAL"},
            "description": "Latest options tick data"
        },
        # Perpetuals
        {
            "name": "Perpetuals Latest Tick",
            "path": "/perpetuals/v1/latest/tick",
            "params": {"market": "binance", "instruments": "BTC-USDT-PERPETUAL"},
            "description": "Latest perpetual swap tick data"
        },
    ]
    
    results = []
    
    for i, endpoint in enumerate(endpoints, 1):
        print(f"\n[{i}/{len(endpoints)}] Testing: {endpoint['name']}")
        print(f"    Path: {endpoint['path']}")
        print(f"    Params: {endpoint['params']}")
        print(f"    Description: {endpoint['description']}")
        
        response = client.get(endpoint['path'], params=endpoint['params'])
        
        status = response['status_code']
        print(f"    Status: {status}")
        
        if status == 200:
            data = response.get('data', {})
            
            if 'Data' in data:
                print(f"    {summarize_response(data['Data'], 'Data')}")
            else:
                print(f"    {summarize_response(data, 'Full Response')}")
            
            if data.get('Err'):
                print(f"    ⚠️  Error: {data['Err']}")
            if data.get('Warn'):
                print(f"    ⚠️  Warning: {data['Warn']}")
            
            rl = response.get('rate_limit', {})
            if rl.get('remaining'):
                print(f"    Rate Limit: {rl['remaining']} remaining")
        else:
            error_msg = response.get('error', 'Unknown error')
            if len(error_msg) > 200:
                error_msg = error_msg[:200] + "..."
            print(f"    ❌ Error: {error_msg}")
        
        results.append({
            "endpoint": endpoint['name'],
            "path": endpoint['path'],
            "status": status,
            "response": response
        })
        
        print(f"    ⏱️  Waiting for rate limit...")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Probe CoinDesk Derivatives API endpoints"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help=f"API key for authentication (default: {DEFAULT_API_KEY[:16]}...)"
    )
    parser.add_argument(
        "--instruments",
        type=str,
        nargs="+",
        default=["BTCUSDT", "ETHUSDT"],
        help="Instruments to test (default: BTCUSDT ETHUSDT)"
    )
    
    args = parser.parse_args()
    
    client = CoinDeskClient(api_key=args.api_key)
    
    print(f"\n🔍 Exploring CoinDesk Derivatives API")
    print(f"   Base URL: {client.base_url}")
    print(f"   Instruments: {', '.join(args.instruments)}")
    
    results = test_derivatives_endpoints(client, args.instruments)
    
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "derivatives_probe_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_file}")
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    success_count = sum(1 for r in results if r['status'] == 200)
    total_count = len(results)
    
    print(f"\n✅ Working: {success_count}/{total_count}")
    print(f"❌ Failed: {total_count - success_count}/{total_count}")
    
    for result in results:
        status_icon = "✅" if result['status'] == 200 else "❌"
        print(f"  {status_icon} {result['endpoint']}: {result['status']}")


if __name__ == "__main__":
    main()
