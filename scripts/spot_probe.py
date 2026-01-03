"""
CoinDesk Spot Market Probe  
Tests spot market data endpoints
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


def test_spot_endpoints(client: CoinDeskClient, instruments: list):
    """Test spot market endpoints"""
    
    print("\n" + "="*80)
    print("COINDESK SPOT MARKET API EXPLORATION")
    print("="*80)
    
    endpoints = [
        {
            "name": "Spot Instruments",
            "path": "/spot/v1/markets/instruments",
            "params": {"market": "coinbase", "instruments": ",".join(instruments)},
            "description": "Get spot instruments for market"
        },
        {
            "name": "Spot Latest Tick",
            "path": "/spot/v1/latest/tick",
            "params": {"market": "coinbase", "instruments": ",".join(instruments)},
            "description": "Latest tick data for spot instruments"
        },
        {
            "name": "Spot Latest Trade",
            "path": "/spot/v1/latest/trade",
            "params": {"market": "coinbase", "instruments": ",".join(instruments)},
            "description": "Latest trade for spot instruments"
        },
        {
            "name": "Spot Historical Hours",
            "path": "/spot/v1/historical/hours",
            "params": {"market": "coinbase", "instrument": instruments[0], "limit": 10},
            "description": "Historical hourly spot data"
        },
        {
            "name": "Spot Historical Days",
            "path": "/spot/v1/historical/days",
            "params": {"market": "coinbase", "instrument": instruments[0], "limit": 10},
            "description": "Historical daily spot data"
        },
        {
            "name": "Spot Markets List",
            "path": "/spot/v1/markets",
            "params": {},
            "description": "List of available spot markets"
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
            
            # Display data summary
            if 'Data' in data:
                print(f"    {summarize_response(data['Data'], 'Data')}")
            else:
                print(f"    {summarize_response(data, 'Full Response')}")
            
            # Check for errors or warnings
            if data.get('Err'):
                print(f"    ⚠️  Error: {data['Err']}")
            if data.get('Warn'):
                print(f"    ⚠️  Warning: {data['Warn']}")
            
            # Rate limit info
            rl = response.get('rate_limit', {})
            if rl.get('remaining'):
                print(f"    Rate Limit: {rl['remaining']} remaining")
        else:
            error_msg = response.get('error', 'Unknown error')
            # Truncate long errors
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
        description="Probe CoinDesk Spot Market API endpoints"
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
        default=["BTC-USD", "ETH-USD"],
        help="Instruments to test (default: BTC-USD ETH-USD)"
    )
    parser.add_argument(
        "--market",
        type=str,
        default="coinbase",
        help="Market to test (default: coinbase)"
    )
    
    args = parser.parse_args()
    
    # Initialize client (polls rate limits once)
    print("\n🔄 Initializing CoinDesk API client...")
    client = CoinDeskClient(api_key=args.api_key)
    
    print(f"\n🔍 Exploring CoinDesk Spot Market API")
    print(f"   Base URL: {client.base_url}")
    print(f"   Market: {args.market}")
    print(f"   Instruments: {', '.join(args.instruments)}")
    
    # Show initial rate limit status (no API call)
    status = client.get_rate_limit_status()
    limits = status["limits"]
    print(f"\n📊 Rate limits (locally tracked, no API call):")
    print(f"   Monthly: {limits['MONTH']['remaining']}/{limits['MONTH']['max']} remaining")
    
    # Test endpoints
    results = test_spot_endpoints(client, args.instruments)
    
    # Show final rate limit status (no API call)
    final_status = client.get_rate_limit_status()
    final_limits = final_status["limits"]
    print(f"\n📊 Final rate limits (locally tracked):")
    print(f"   Monthly: {final_limits['MONTH']['remaining']}/{final_limits['MONTH']['max']} remaining")
    print(f"   API calls used: {limits['MONTH']['remaining'] - final_limits['MONTH']['remaining']} data calls")
    print(f"   💡 Old method would have used: {(limits['MONTH']['remaining'] - final_limits['MONTH']['remaining']) * 2} total calls")
    print(f"   🎯 Saved: {limits['MONTH']['remaining'] - final_limits['MONTH']['remaining']} API calls!")
    
    # Save results
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "spot_probe_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to: {output_file}")
    
    # Summary
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
