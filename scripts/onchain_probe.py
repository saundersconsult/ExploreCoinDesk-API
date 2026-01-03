"""
CoinDesk On-Chain Probe
Tests blockchain metrics and on-chain data endpoints
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


def test_onchain_endpoints(client: CoinDeskClient, assets: list):
    """Test on-chain data endpoints"""
    
    print("\n" + "="*80)
    print("COINDESK ON-CHAIN API EXPLORATION")
    print("="*80)
    
    endpoints = [
        {
            "name": "On-Chain Latest",
            "path": "/onchain/v1/latest",
            "params": {"assets": ",".join(assets)},
            "description": "Latest on-chain metrics"
        },
        {
            "name": "On-Chain Historical Days",
            "path": "/onchain/v1/historical/days",
            "params": {"asset": assets[0], "limit": 10},
            "description": "Historical daily on-chain metrics"
        },
        {
            "name": "Network Stats",
            "path": "/onchain/v1/network/stats",
            "params": {"assets": ",".join(assets)},
            "description": "Network statistics (hash rate, difficulty, etc.)"
        },
        {
            "name": "Blockchain Latest",
            "path": "/blockchain/v1/latest",
            "params": {"blockchain": "bitcoin"},
            "description": "Latest blockchain data"
        },
        {
            "name": "Blockchain Historical",
            "path": "/blockchain/v1/historical/days",
            "params": {"blockchain": "bitcoin", "limit": 10},
            "description": "Historical blockchain metrics"
        },
        {
            "name": "DeFi TVL",
            "path": "/defi/v1/tvl/latest",
            "params": {"protocols": "uniswap,aave"},
            "description": "Total Value Locked in DeFi protocols"
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
        description="Probe CoinDesk On-Chain API endpoints"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help=f"API key for authentication (default: {DEFAULT_API_KEY[:16]}...)"
    )
    parser.add_argument(
        "--assets",
        type=str,
        nargs="+",
        default=["BTC", "ETH"],
        help="Assets to test (default: BTC ETH)"
    )
    
    args = parser.parse_args()
    
    client = CoinDeskClient(api_key=args.api_key)
    
    print(f"\n🔍 Exploring CoinDesk On-Chain API")
    print(f"   Base URL: {client.base_url}")
    print(f"   Assets: {', '.join(args.assets)}")
    
    results = test_onchain_endpoints(client, args.assets)
    
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "onchain_probe_results.json"
    
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
