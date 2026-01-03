"""
CoinDesk Index Probe
Tests index and reference price endpoints
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

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


def test_index_endpoints(client: CoinDeskClient, instruments: list):
    """Test various index endpoints"""
    
    print("\n" + "="*80)
    print("COINDESK INDEX API EXPLORATION")
    print("="*80)
    
    endpoints = [
        {
            "name": "CCIX Latest Tick",
            "path": "/index/cc/v1/latest/tick",
            "params": {"market": "ccix", "instruments": ",".join(instruments)},
            "description": "Latest index tick for specified instruments"
        },
        {
            "name": "CCIX Historical Hour",
            "path": "/index/cc/v1/historical/hours",
            "params": {"market": "ccix", "instrument": instruments[0], "limit": 10},
            "description": "Historical hourly index data"
        },
        {
            "name": "CCIX Historical Day",
            "path": "/index/cc/v1/historical/days",
            "params": {"market": "ccix", "instrument": instruments[0], "limit": 10},
            "description": "Historical daily index data"
        },
        {
            "name": "CCIX Historical Minute",
            "path": "/index/cc/v1/historical/minutes",
            "params": {"market": "ccix", "instrument": instruments[0], "limit": 10},
            "description": "Historical minute index data"
        },
        {
            "name": "Index Instruments",
            "path": "/index/cc/v1/markets/instruments",
            "params": {"market": "ccix"},
            "description": "Available instruments for CCIX market"
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
            print(f"    ❌ Error: {response.get('error', 'Unknown error')}")
        
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
        description="Probe CoinDesk Index API endpoints"
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
    
    args = parser.parse_args()
    
    # Initialize client
    client = CoinDeskClient(api_key=args.api_key)
    
    print(f"\n🔍 Exploring CoinDesk Index API")
    print(f"   Base URL: {client.base_url}")
    print(f"   Instruments: {', '.join(args.instruments)}")
    
    # Test endpoints
    results = test_index_endpoints(client, args.instruments)
    
    # Save results
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "index_probe_results.json"
    
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
