"""
CoinDesk API - Explore actual documented endpoint patterns
Based on what we know works, test variations and additional features
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api_client import CoinDeskClient


def test_endpoint(client, name, path, params=None):
    """Test endpoint and return result"""
    response = client.get(path, params=params)
    
    success = response["status_code"] == 200
    result = {
        "name": name,
        "path": path,
        "params": params or {},
        "status": response["status_code"],
        "success": success
    }
    
    if success:
        data = response.get("data", {})
        if "Data" in data:
            content = data["Data"]
            if isinstance(content, dict):
                result["count"] = len(content)
                result["sample_keys"] = list(content.keys())[:5]
            elif isinstance(content, list):
                result["count"] = len(content)
                if content and isinstance(content[0], dict):
                    result["sample_fields"] = list(content[0].keys())[:10]
    
    status_icon = "✅" if success else "❌"
    print(f"{status_icon} {name}: {path} → {response['status_code']}", end="")
    if success and 'count' in result:
        print(f" ({result['count']} items)")
    else:
        print()
    
    return result


def main():
    print("\n" + "="*80)
    print("COINDESK API - EXTENDED EXPLORATION")
    print("="*80)
    
    client = CoinDeskClient()
    status = client.get_rate_limit_status()
    print(f"\n📊 Starting: {status['limits']['MONTH']['remaining']}/{status['limits']['MONTH']['max']} monthly calls\n")
    
    results = []
    
    # Test additional spot endpoints
    print("\n📍 SPOT API - Additional Endpoints:")
    print("-" * 80)
    results.append(test_endpoint(client, "Spot Minute Historical", "/spot/v1/historical/minutes", 
                                  {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}))
    results.append(test_endpoint(client, "Spot Week Historical", "/spot/v1/historical/weeks",
                                  {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}))
    results.append(test_endpoint(client, "Spot Month Historical", "/spot/v1/historical/months",
                                  {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}))
    
    # Test additional futures endpoints
    print("\n📍 FUTURES API - Additional Endpoints:")
    print("-" * 80)
    results.append(test_endpoint(client, "Futures Minute Historical", "/futures/v1/historical/minutes",
                                  {"market": "binance", "instrument": "BTCUSDT", "limit": 10}))
    results.append(test_endpoint(client, "Futures Week Historical", "/futures/v1/historical/weeks",
                                  {"market": "binance", "instrument": "BTCUSDT", "limit": 10}))
    results.append(test_endpoint(client, "Futures Funding Rates", "/futures/v1/funding/rates",
                                  {"market": "binance", "instrument": "BTCUSDT"}))
    results.append(test_endpoint(client, "Futures Open Interest", "/futures/v1/openinterest",
                                  {"market": "binance", "instrument": "BTCUSDT"}))
    results.append(test_endpoint(client, "Futures Open Interest Historical", "/futures/v1/historical/openinterest",
                                  {"market": "binance", "instrument": "BTCUSDT", "limit": 10}))
    
    # Test index variations
    print("\n📍 INDEX API - Additional Endpoints:")
    print("-" * 80)
    results.append(test_endpoint(client, "Index Latest All", "/index/cc/v1/latest/all", {}))
    results.append(test_endpoint(client, "Index Constituents", "/index/cc/v1/constituents",
                                  {"instrument": "BTC-USD"}))
    results.append(test_endpoint(client, "Index Methodology", "/index/cc/v1/methodology",
                                  {"instrument": "BTC-USD"}))
    
    # Test options variations
    print("\n📍 OPTIONS API - Additional Endpoints:")
    print("-" * 80)
    results.append(test_endpoint(client, "Options Historical Hours", "/options/v1/historical/hours",
                                  {"market": "deribit", "instrument": "BTC-25JAN26-100000-C", "limit": 10}))
    results.append(test_endpoint(client, "Options Greeks", "/options/v1/greeks",
                                  {"market": "deribit", "instrument": "BTC-25JAN26-100000-C"}))
    results.append(test_endpoint(client, "Options Volatility", "/options/v1/volatility",
                                  {"market": "deribit", "asset": "BTC"}))
    
    # Test perpetuals (separate from futures)
    print("\n📍 PERPETUALS API:")
    print("-" * 80)
    results.append(test_endpoint(client, "Perpetuals Markets", "/perpetuals/v1/markets", {}))
    results.append(test_endpoint(client, "Perpetuals Instruments", "/perpetuals/v1/markets/instruments",
                                  {"market": "binance"}))
    results.append(test_endpoint(client, "Perpetuals Historical Hours", "/perpetuals/v1/historical/hours",
                                  {"market": "binance", "instrument": "BTCUSDT", "limit": 10}))
    results.append(test_endpoint(client, "Perpetuals Funding", "/perpetuals/v1/funding",
                                  {"market": "binance", "instrument": "BTCUSDT"}))
    
    # Test orderbook endpoints
    print("\n📍 ORDERBOOK API:")
    print("-" * 80)
    results.append(test_endpoint(client, "Spot Orderbook", "/spot/v1/orderbook/snapshot",
                                  {"market": "coinbase", "instrument": "BTC-USD"}))
    results.append(test_endpoint(client, "Futures Orderbook", "/futures/v1/orderbook/snapshot",
                                  {"market": "binance", "instrument": "BTCUSDT"}))
    results.append(test_endpoint(client, "Orderbook Historical", "/spot/v1/historical/orderbook",
                                  {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}))
    
    # Test trade-level data
    print("\n📍 TRADE-LEVEL DATA:")
    print("-" * 80)
    results.append(test_endpoint(client, "Spot Trades", "/spot/v1/trades",
                                  {"market": "coinbase", "instrument": "BTC-USD", "limit": 10}))
    results.append(test_endpoint(client, "Futures Trades", "/futures/v1/trades",
                                  {"market": "binance", "instrument": "BTCUSDT", "limit": 10}))
    
    # Test aggregated data
    print("\n📍 AGGREGATED DATA:")
    print("-" * 80)
    results.append(test_endpoint(client, "Spot Aggregated Tick", "/spot/v1/latest/aggregated",
                                  {"instrument": "BTC-USD"}))
    results.append(test_endpoint(client, "Futures Aggregated Tick", "/futures/v1/latest/aggregated",
                                  {"instrument": "BTC-USD"}))
    
    # Test metadata endpoints
    print("\n📍 METADATA & INFO:")
    print("-" * 80)
    results.append(test_endpoint(client, "API Version", "/version", {}))
    results.append(test_endpoint(client, "API Info", "/info", {}))
    results.append(test_endpoint(client, "Spot Exchange Status", "/spot/v1/exchange/status",
                                  {"market": "coinbase"}))
    results.append(test_endpoint(client, "Futures Exchange Status", "/futures/v1/exchange/status",
                                  {"market": "binance"}))
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    final_status = client.get_rate_limit_status()
    total = len(results)
    working = sum(1 for r in results if r['success'])
    
    print(f"\n📊 Endpoints tested: {total}")
    print(f"   ✅ Working: {working} ({100*working/total:.1f}%)")
    print(f"   ❌ Failed: {total-working} ({100*(total-working)/total:.1f}%)")
    print(f"\n📊 Rate limits:")
    print(f"   Used: {status['limits']['MONTH']['remaining'] - final_status['limits']['MONTH']['remaining']} calls")
    print(f"   Remaining: {final_status['limits']['MONTH']['remaining']}/{final_status['limits']['MONTH']['max']}")
    
    # Show all working endpoints
    working_endpoints = [r for r in results if r['success']]
    if working_endpoints:
        print(f"\n✅ WORKING ENDPOINTS ({len(working_endpoints)}):")
        for r in working_endpoints:
            count = f" - {r['count']} items" if 'count' in r else ""
            print(f"   • {r['name']}: {r['path']}{count}")
    
    # Save results
    output_dir = Path(__file__).parent.parent / "docs"
    output_file = output_dir / "extended_endpoints_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Results saved to: {output_file}")


if __name__ == "__main__":
    main()
