"""
Check CoinDesk API Rate Limits
Queries the rate limit endpoint and displays current usage
"""
import sys
import json
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api_client import CoinDeskClient, DEFAULT_API_KEY


def display_rate_limits(rate_data: dict):
    """Display rate limit information in a readable format"""
    
    print("\n" + "="*80)
    print("COINDESK API RATE LIMITS")
    print("="*80)
    
    if rate_data.get("status_code") != 200:
        print(f"\n❌ Error: Status {rate_data.get('status_code')}")
        print(f"Error: {rate_data.get('error')}")
        return
    
    # Display rate limit headers
    rl_info = rate_data.get("rate_limit", {})
    print("\n📊 Rate Limit Headers:")
    print(f"  Limit: {rl_info.get('limit', 'N/A')}")
    print(f"  Remaining: {rl_info.get('remaining', 'N/A')}")
    print(f"  Reset: {rl_info.get('reset', 'N/A')} seconds")
    
    # Display response data
    data = rate_data.get("data", {})
    if data:
        print("\n📈 Rate Limit Details:")
        print(json.dumps(data, indent=2))
    
    # Check if deprecated
    if rate_data.get("deprecated"):
        print("\n⚠️  WARNING: This endpoint is deprecated!")
    
    print("\n" + "="*80)


def main():
    parser = argparse.ArgumentParser(
        description="Check CoinDesk API rate limits"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help=f"API key for authentication (default: {DEFAULT_API_KEY[:16]}...)"
    )
    
    args = parser.parse_args()
    
    # Initialize client
    client = CoinDeskClient(api_key=args.api_key)
    
    print(f"\n🔍 Checking rate limits for CoinDesk API...")
    print(f"   Base URL: {client.base_url}")
    print(f"   API Key: {client.api_key[:16]}...{client.api_key[-8:]}")
    
    # Get rate limits
    rate_data = client.get_rate_limits()
    
    # Display results
    display_rate_limits(rate_data)
    
    # Save to file
    output_file = Path(__file__).parent.parent / "docs" / "rate_limit_response.json"
    output_file.parent.mkdir(exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(rate_data, f, indent=2)
    
    print(f"\n💾 Full response saved to: {output_file}")


if __name__ == "__main__":
    main()
