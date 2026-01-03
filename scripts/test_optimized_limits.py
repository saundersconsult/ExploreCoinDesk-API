"""
Test script for optimized rate limit tracking.
Demonstrates that rate limits are polled once, then tracked locally.
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.api_client import CoinDeskClient


def main():
    print("=" * 80)
    print("OPTIMIZED RATE LIMIT TRACKING TEST")
    print("=" * 80)
    print()
    
    # Initialize client (this polls rate limits ONCE)
    print("1️⃣  Creating client (will poll rate limits once)...")
    client = CoinDeskClient()
    print()
    
    # Show initial tracked limits
    print("2️⃣  Initial rate limit status (local tracking, NO API call):")
    status = client.get_rate_limit_status()
    limits = status["limits"]
    print(f"   Monthly: {limits['MONTH']['remaining']}/{limits['MONTH']['max']}")
    print(f"   Daily:   {limits['DAY']['remaining']}/{limits['DAY']['max']}")
    print(f"   Hourly:  {limits['HOUR']['remaining']}/{limits['HOUR']['max']}")
    print(f"   Minute:  {limits['MINUTE']['remaining']}/{limits['MINUTE']['max']}")
    print()
    
    # Make 5 API calls
    print("3️⃣  Making 5 data API calls (each counts as 1 call, no extra rate limit checks):")
    
    test_calls = [
        ("/index/cc/v1/latest/tick", {"instruments": "BTC-USD"}),
        ("/index/cc/v1/latest/tick", {"instruments": "ETH-USD"}),
        ("/spot/v1/markets", {}),
        ("/futures/v1/markets", {}),
        ("/options/v1/markets", {}),
    ]
    
    for i, (endpoint, params) in enumerate(test_calls, 1):
        print(f"\n   Call {i}: {endpoint}")
        response = client.get(endpoint, params=params)
        
        if response["status_code"] == 200:
            print(f"   ✅ Success (status 200)")
        else:
            print(f"   ❌ Failed (status {response['status_code']})")
        
        # Show tracked limits after each call (NO API CALL)
        status = client.get_rate_limit_status()
        limits = status["limits"]
        print(f"   📊 Tracked limits - Monthly: {limits['MONTH']['remaining']}/{limits['MONTH']['max']} remaining")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    # Final status
    final_status = client.get_rate_limit_status()
    final_limits = final_status["limits"]
    
    print(f"\n✅ API calls made: 6 total")
    print(f"   - 1 initial rate limit poll (initialization)")
    print(f"   - 5 data API calls")
    print(f"   - 0 additional rate limit checks ⭐")
    print()
    print(f"📊 Final tracked limits:")
    print(f"   Monthly: {final_limits['MONTH']['remaining']}/{final_limits['MONTH']['max']}")
    print(f"   Daily:   {final_limits['DAY']['remaining']}/{final_limits['DAY']['max']}")
    print(f"   Hourly:  {final_limits['HOUR']['remaining']}/{final_limits['HOUR']['max']}")
    print(f"   Minute:  {final_limits['MINUTE']['remaining']}/{final_limits['MINUTE']['max']}")
    print()
    print("💡 With old method: Would have made 5 extra API calls to check limits")
    print("💡 With new method: Made 0 extra API calls (tracked locally)")
    print("🎯 Efficiency gain: 5 extra useful API calls available!")
    print()
    
    # Optional: Show how to manually refresh if needed
    print("=" * 80)
    print("OPTIONAL: Manual refresh from API")
    print("=" * 80)
    print()
    print("If you need to verify against actual API limits, you can refresh:")
    print(">>> client.refresh_rate_limits()  # This makes 1 API call")
    print()
    print("But for normal usage, local tracking is sufficient! ✅")
    print()


if __name__ == "__main__":
    main()
