"""
CoinDesk Additional Data Endpoints Probe
Explores other potential data endpoints beyond the main categories
"""
import sys
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api_client import CoinDeskClient


def test_endpoint(client, name, path, params=None, description=""):
    """Test a single endpoint"""
    print(f"\n{'='*80}")
    print(f"Testing: {name}")
    print(f"Path: {path}")
    if params:
        print(f"Params: {params}")
    if description:
        print(f"Description: {description}")
    print(f"{'='*80}")
    
    response = client.get(path, params=params)
    
    result = {
        "name": name,
        "path": path,
        "params": params or {},
        "description": description,
        "status": response["status_code"],
        "success": response["status_code"] == 200
    }
    
    if response["status_code"] == 200:
        data = response.get("data", {})
        if isinstance(data, dict):
            result["data_type"] = "dict"
            result["keys"] = list(data.get("Data", {}).keys()) if "Data" in data else list(data.keys())
            
            # Check for market/instrument lists
            if "Data" in data:
                data_content = data["Data"]
                if isinstance(data_content, dict):
                    # Count items
                    result["count"] = len(data_content)
                    # Get sample keys
                    if data_content:
                        first_key = list(data_content.keys())[0]
                        result["sample_key"] = first_key
                        if isinstance(data_content[first_key], dict):
                            result["sample_fields"] = list(data_content[first_key].keys())[:10]
                elif isinstance(data_content, list):
                    result["count"] = len(data_content)
                    if data_content and isinstance(data_content[0], dict):
                        result["sample_fields"] = list(data_content[0].keys())[:10]
        
        print(f"✅ SUCCESS (200)")
        print(f"   Data type: {result.get('data_type', 'unknown')}")
        if 'count' in result:
            print(f"   Items: {result['count']}")
        if 'keys' in result:
            print(f"   Keys: {result['keys'][:5]}")
        if 'sample_fields' in result:
            print(f"   Sample fields: {result['sample_fields']}")
    else:
        error_text = response.get("error", "")
        result["error"] = error_text
        print(f"❌ FAILED ({response['status_code']})")
        if error_text:
            # Truncate long error messages
            error_preview = error_text[:200] if len(error_text) > 200 else error_text
            print(f"   Error: {error_preview}")
    
    return result


def main():
    print("\n" + "="*80)
    print("COINDESK ADDITIONAL DATA ENDPOINTS EXPLORATION")
    print("="*80)
    
    client = CoinDeskClient()
    
    # Show initial limits
    status = client.get_rate_limit_status()
    print(f"\n📊 Starting limits: {status['limits']['MONTH']['remaining']}/{status['limits']['MONTH']['max']} monthly calls")
    
    results = []
    
    # Category 1: Market Data Aggregates
    print("\n" + "="*80)
    print("CATEGORY 1: MARKET DATA AGGREGATES")
    print("="*80)
    
    endpoints_aggregates = [
        ("Market Overview", "/data/v1/overview", {}, "Overall market overview"),
        ("Market Summary", "/data/v1/summary", {}, "Market summary data"),
        ("Market Stats", "/data/v1/stats", {}, "Market statistics"),
        ("Global Metrics", "/data/v1/global", {}, "Global market metrics"),
        ("Asset Rankings", "/data/v1/rankings", {}, "Asset rankings by various metrics"),
        ("Market Movers", "/data/v1/movers", {}, "Top movers/gainers/losers"),
    ]
    
    for name, path, params, desc in endpoints_aggregates:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Category 2: Trading Data
    print("\n" + "="*80)
    print("CATEGORY 2: TRADING DATA")
    print("="*80)
    
    endpoints_trading = [
        ("Order Book Snapshot", "/data/v1/orderbook/snapshot", {"market": "binance", "instrument": "BTC-USD"}, "Order book depth"),
        ("Trade History", "/data/v1/trades", {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}, "Recent trades"),
        ("Volume Data", "/data/v1/volume", {"instrument": "BTC-USD"}, "Volume across exchanges"),
        ("Liquidity Metrics", "/data/v1/liquidity", {"instrument": "BTC-USD"}, "Liquidity metrics"),
        ("Spread Data", "/data/v1/spread", {"instrument": "BTC-USD"}, "Bid-ask spread data"),
    ]
    
    for name, path, params, desc in endpoints_trading:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Category 3: Reference Data
    print("\n" + "="*80)
    print("CATEGORY 3: REFERENCE DATA")
    print("="*80)
    
    endpoints_reference = [
        ("Assets List", "/data/v1/assets", {}, "All available assets"),
        ("Asset Metadata", "/data/v1/asset/info", {"asset": "BTC"}, "Asset information"),
        ("Exchanges List", "/data/v1/exchanges", {}, "All exchanges"),
        ("Exchange Info", "/data/v1/exchange/info", {"exchange": "binance"}, "Exchange information"),
        ("Instruments List", "/data/v1/instruments", {}, "All available instruments"),
        ("Pairs Mapping", "/data/v1/pairs", {}, "Trading pairs across exchanges"),
    ]
    
    for name, path, params, desc in endpoints_reference:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Category 4: Historical & Analytics
    print("\n" + "="*80)
    print("CATEGORY 4: HISTORICAL & ANALYTICS")
    print("="*80)
    
    endpoints_historical = [
        ("Historical Snapshots", "/data/v1/historical/snapshots", {"instrument": "BTC-USD", "interval": "1h"}, "Market snapshots"),
        ("VWAP Data", "/data/v1/vwap", {"instrument": "BTC-USD"}, "Volume weighted average price"),
        ("TWAP Data", "/data/v1/twap", {"instrument": "BTC-USD"}, "Time weighted average price"),
        ("Historical Volume", "/data/v1/historical/volume", {"instrument": "BTC-USD", "limit": 10}, "Historical volume"),
        ("Candles", "/data/v1/candles", {"market": "coinbase", "instrument": "BTC-USD", "interval": "1h", "limit": 10}, "OHLCV candles"),
    ]
    
    for name, path, params, desc in endpoints_historical:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Category 5: WebSocket & Streaming Info
    print("\n" + "="*80)
    print("CATEGORY 5: STREAMING & WEBSOCKET INFO")
    print("="*80)
    
    endpoints_streaming = [
        ("WebSocket Info", "/data/v1/websocket/info", {}, "WebSocket connection info"),
        ("Streaming Channels", "/data/v1/streaming/channels", {}, "Available streaming channels"),
        ("Subscription Info", "/data/v1/streaming/subscriptions", {}, "Subscription options"),
    ]
    
    for name, path, params, desc in endpoints_streaming:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Category 6: Alternative paths
    print("\n" + "="*80)
    print("CATEGORY 6: ALTERNATIVE API PATHS")
    print("="*80)
    
    endpoints_alternative = [
        ("API v2 Markets", "/v2/markets", {}, "Markets list (v2)"),
        ("API v2 Assets", "/v2/assets", {}, "Assets list (v2)"),
        ("Root Data", "/data", {}, "Root data endpoint"),
        ("Root API", "/api", {}, "Root API endpoint"),
        ("Status", "/status", {}, "API status"),
        ("Health", "/health", {}, "API health check"),
    ]
    
    for name, path, params, desc in endpoints_alternative:
        results.append(test_endpoint(client, name, path, params, desc))
    
    # Final summary
    print("\n" + "="*80)
    print("EXPLORATION SUMMARY")
    print("="*80)
    
    final_status = client.get_rate_limit_status()
    total_tested = len(results)
    total_working = sum(1 for r in results if r['success'])
    total_failed = total_tested - total_working
    
    print(f"\n📊 Results:")
    print(f"   Total endpoints tested: {total_tested}")
    print(f"   ✅ Working: {total_working} ({100*total_working/total_tested:.1f}%)")
    print(f"   ❌ Failed: {total_failed} ({100*total_failed/total_tested:.1f}%)")
    
    print(f"\n📊 Rate limits:")
    print(f"   Initial: {status['limits']['MONTH']['remaining']}/{status['limits']['MONTH']['max']}")
    print(f"   Final: {final_status['limits']['MONTH']['remaining']}/{final_status['limits']['MONTH']['max']}")
    print(f"   API calls used: {status['limits']['MONTH']['remaining'] - final_status['limits']['MONTH']['remaining']}")
    
    # Show working endpoints
    if total_working > 0:
        print(f"\n✅ WORKING ENDPOINTS ({total_working}):")
        for r in results:
            if r['success']:
                count_str = f" ({r['count']} items)" if 'count' in r else ""
                print(f"   ✅ {r['name']}: {r['path']}{count_str}")
    
    # Show failed endpoints by category
    print(f"\n❌ FAILED ENDPOINTS ({total_failed}):")
    for r in results:
        if not r['success']:
            print(f"   ❌ {r['name']}: {r['path']} → {r['status']}")
    
    # Save results
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "additional_data_probe_results.json"
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Full results saved to: {output_file}")


if __name__ == "__main__":
    main()
