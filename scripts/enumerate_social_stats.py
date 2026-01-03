#!/usr/bin/env python3
"""
Enumerate social statistics from CryptoCompare API.

This script fetches social media statistics for cryptocurrencies including
Twitter, Reddit, Facebook, GitHub, and CryptoCompare metrics.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, Optional, List

import requests


def fetch_social_stats(coin_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Fetch latest social stats for a cryptocurrency.
    
    Args:
        coin_id: Cryptocurrency ID (e.g., '1182' for BTC)
        api_key: Optional API key for authentication
        
    Returns:
        API response as dictionary
        
    Raises:
        requests.RequestException: On network or API errors
    """
    url = "https://min-api.cryptocompare.com/data/social/coin/latest"
    headers = {}
    params = {'coinId': coin_id}
    
    if api_key:
        headers['authorization'] = f'Apikey {api_key}'
    
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    
    return response.json()


def fetch_multiple_coins(coin_ids: List[str], api_key: Optional[str] = None, verbose: bool = False) -> Dict[str, Any]:
    """
    Fetch social stats for multiple coins.
    
    Args:
        coin_ids: List of cryptocurrency IDs
        api_key: Optional API key for authentication
        verbose: Whether to print progress
        
    Returns:
        Dictionary mapping coin IDs to their social stats
    """
    results = {}
    
    for i, coin_id in enumerate(coin_ids, 1):
        if verbose:
            print(f"Fetching social stats for coin ID {coin_id} ({i}/{len(coin_ids)})...")
        
        try:
            data = fetch_social_stats(coin_id=coin_id, api_key=api_key)
            results[coin_id] = data
        except requests.RequestException as e:
            if verbose:
                print(f"  ✗ Error fetching {coin_id}: {e}")
            results[coin_id] = {"error": str(e)}
    
    return results


def save_as_json(data: Dict[str, Any], output_file: str, pretty: bool = True) -> None:
    """
    Save data as JSON file.
    
    Args:
        data: Data to save
        output_file: Output file path
        pretty: Whether to pretty-print the JSON
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(data, f, ensure_ascii=False)
    print(f"✓ Saved JSON to: {output_file}")


def save_as_csv(data: Dict[str, Any], output_file: str, multi_coin: bool = False) -> None:
    """
    Save social stats as CSV file.
    
    Args:
        data: API response data
        output_file: Output file path
        multi_coin: Whether data contains multiple coins
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        if multi_coin:
            # Multiple coins
            f.write("coin_id,coin_name,symbol,twitter_followers,reddit_subscribers,github_stars,cryptocompare_followers,cryptocompare_pageviews\n")
            for coin_id, coin_data in data.items():
                if 'error' in coin_data:
                    f.write(f'{coin_id},"Error","","","","","",""\n')
                elif 'Data' in coin_data and coin_data.get('Response') == 'Success':
                    general = coin_data['Data'].get('General', {})
                    twitter = coin_data['Data'].get('Twitter', {})
                    reddit = coin_data['Data'].get('Reddit', {})
                    github = coin_data['Data'].get('CodeRepository', {}).get('List', [{}])[0] if coin_data['Data'].get('CodeRepository', {}).get('List') else {}
                    cc = coin_data['Data'].get('CryptoCompare', {})
                    
                    name = general.get('CoinName', 'N/A')
                    symbol = general.get('Name', 'N/A')
                    twitter_followers = twitter.get('followers', 0)
                    reddit_subs = reddit.get('subscribers', 0)
                    github_stars = github.get('stars', 0) if isinstance(github, dict) else 0
                    cc_followers = cc.get('Followers', 0)
                    cc_pageviews = cc.get('PageViews', 0)
                    
                    f.write(f'{coin_id},"{name}","{symbol}",{twitter_followers},{reddit_subs},{github_stars},{cc_followers},{cc_pageviews}\n')
        else:
            # Single coin
            if 'Data' not in data or data.get('Response') != 'Success':
                f.write("metric,value\n")
                f.write('"error","No data available"\n')
                return
            
            social_data = data['Data']
            general = social_data.get('General', {})
            twitter = social_data.get('Twitter', {})
            reddit = social_data.get('Reddit', {})
            github = social_data.get('CodeRepository', {}).get('List', [{}])[0] if social_data.get('CodeRepository', {}).get('List') else {}
            cc = social_data.get('CryptoCompare', {})
            
            f.write("metric,value\n")
            f.write(f'"Coin Name","{general.get("CoinName", "N/A")}"\n')
            f.write(f'"Symbol","{general.get("Name", "N/A")}"\n')
            f.write(f'"Total Points",{general.get("Points", 0)}\n')
            f.write(f'"Twitter Followers",{twitter.get("followers", 0)}\n')
            f.write(f'"Twitter Statuses",{twitter.get("statuses", 0)}\n')
            f.write(f'"Reddit Subscribers",{reddit.get("subscribers", 0)}\n')
            f.write(f'"Reddit Posts/Day",{reddit.get("posts_per_day", 0)}\n')
            f.write(f'"Reddit Comments/Day",{reddit.get("comments_per_day", 0)}\n')
            if isinstance(github, dict):
                f.write(f'"GitHub Stars",{github.get("stars", 0)}\n')
                f.write(f'"GitHub Forks",{github.get("forks", 0)}\n')
                f.write(f'"GitHub Contributors",{github.get("contributors", 0)}\n')
            f.write(f'"CryptoCompare Followers",{cc.get("Followers", 0)}\n')
            f.write(f'"CryptoCompare PageViews",{cc.get("PageViews", 0)}\n')
            f.write(f'"CryptoCompare Comments",{cc.get("Comments", 0)}\n')
            f.write(f'"CryptoCompare Posts",{cc.get("Posts", 0)}\n')
    
    print(f"✓ Saved CSV to: {output_file}")


def save_as_summary(data: Dict[str, Any], output_file: str, multi_coin: bool = False) -> None:
    """
    Save a human-readable summary of social stats.
    
    Args:
        data: API response data
        output_file: Output file path
        multi_coin: Whether data contains multiple coins
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("SOCIAL MEDIA STATISTICS SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        if multi_coin:
            for coin_id, coin_data in data.items():
                f.write(f"\n{'=' * 80}\n")
                f.write(f"Coin ID: {coin_id}\n")
                f.write(f"{'=' * 80}\n")
                
                if 'error' in coin_data:
                    f.write(f"Error: {coin_data['error']}\n")
                    continue
                
                if 'Data' not in coin_data or coin_data.get('Response') != 'Success':
                    f.write("No data available\n")
                    continue
                
                write_social_summary(f, coin_data['Data'])
        else:
            if 'Data' in data and data.get('Response') == 'Success':
                write_social_summary(f, data['Data'])
            else:
                f.write("No data available\n")
    
    print(f"✓ Saved summary to: {output_file}")


def write_social_summary(f, social_data: Dict[str, Any]) -> None:
    """Helper to write social stats summary."""
    general = social_data.get('General', {})
    twitter = social_data.get('Twitter', {})
    reddit = social_data.get('Reddit', {})
    github_list = social_data.get('CodeRepository', {}).get('List', [])
    github = github_list[0] if github_list else {}
    cc = social_data.get('CryptoCompare', {})
    
    f.write(f"Coin: {general.get('CoinName', 'N/A')} ({general.get('Name', 'N/A')})\n")
    f.write(f"Total Points: {general.get('Points', 0):,}\n\n")
    
    f.write("TWITTER\n")
    f.write("-" * 80 + "\n")
    f.write(f"  Followers: {twitter.get('followers', 0):,}\n")
    f.write(f"  Tweets: {twitter.get('statuses', 0):,}\n")
    f.write(f"  Lists: {twitter.get('lists', 0):,}\n")
    f.write(f"  Points: {twitter.get('Points', 0):,}\n\n")
    
    f.write("REDDIT\n")
    f.write("-" * 80 + "\n")
    f.write(f"  Subscribers: {reddit.get('subscribers', 0):,}\n")
    f.write(f"  Posts/Day: {reddit.get('posts_per_day', 0):.2f}\n")
    f.write(f"  Comments/Day: {reddit.get('comments_per_day', 0):.2f}\n")
    f.write(f"  Active Users: {reddit.get('active_users', 0):,}\n")
    f.write(f"  Points: {reddit.get('Points', 0):,}\n\n")
    
    if github and isinstance(github, dict):
        f.write("GITHUB\n")
        f.write("-" * 80 + "\n")
        f.write(f"  Stars: {github.get('stars', 0):,}\n")
        f.write(f"  Forks: {github.get('forks', 0):,}\n")
        f.write(f"  Contributors: {github.get('contributors', 0):,}\n")
        f.write(f"  Subscribers: {github.get('subscribers', 0):,}\n")
        f.write(f"  Open Issues: {github.get('open_pull_issues', 0):,}\n\n")
    
    f.write("CRYPTOCOMPARE\n")
    f.write("-" * 80 + "\n")
    f.write(f"  Followers: {cc.get('Followers', 0):,}\n")
    f.write(f"  Page Views: {cc.get('PageViews', 0):,}\n")
    f.write(f"  Comments: {cc.get('Comments', 0):,}\n")
    f.write(f"  Posts: {cc.get('Posts', 0):,}\n")
    f.write(f"  Points: {cc.get('Points', 0):,}\n\n")


def read_coin_ids_from_file(filepath: str) -> List[str]:
    """
    Read coin IDs from a file (one per line).
    
    Args:
        filepath: Path to file containing coin IDs
        
    Returns:
        List of coin IDs
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        coin_ids = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return coin_ids


def main():
    parser = argparse.ArgumentParser(
        description='Enumerate social media statistics from CryptoCompare API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get social stats for BTC (coin ID 1182)
  python scripts/enumerate_social_stats.py --coin-id 1182 --verbose
  
  # Get stats for multiple coins from file
  python scripts/enumerate_social_stats.py --coins-file coin_ids.txt
  
  # Save as CSV
  python scripts/enumerate_social_stats.py --coin-id 1182 --format csv
  
  # Generate summary report
  python scripts/enumerate_social_stats.py --coin-id 1182 --format summary
  
  # Custom output file
  python scripts/enumerate_social_stats.py --coin-id 1182 -o btc_social.json
        """
    )
    
    parser.add_argument(
        '--coin-id',
        help='Cryptocurrency coin ID (e.g., 1182 for BTC)'
    )
    parser.add_argument(
        '--coins-file',
        help='File containing coin IDs (one per line)'
    )
    parser.add_argument(
        '--format',
        choices=['json', 'csv', 'summary'],
        default='json',
        help='Output format (default: json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: social_stats_YYYYMMDD.{ext})'
    )
    parser.add_argument(
        '--api-key',
        help='CryptoCompare API key (or set CRYPTOCOMPARE_API_KEY env var)'
    )
    parser.add_argument(
        '--pretty',
        action='store_true',
        default=True,
        help='Pretty-print JSON output (default: True)'
    )
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Compact JSON output (no pretty-printing)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed progress information'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.coin_id and not args.coins_file:
        print("Error: Must specify either --coin-id or --coins-file", file=sys.stderr)
        sys.exit(1)
    
    if args.coin_id and args.coins_file:
        print("Error: Cannot specify both --coin-id and --coins-file", file=sys.stderr)
        sys.exit(1)
    
    # Get API key from args or environment
    api_key = args.api_key or os.environ.get('CRYPTOCOMPARE_API_KEY')
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        date_str = datetime.now().strftime('%Y%m%d')
        ext_map = {'json': 'json', 'csv': 'csv', 'summary': 'txt'}
        ext = ext_map[args.format]
        if args.coin_id:
            output_file = f"social_stats_{args.coin_id}_{date_str}.{ext}"
        else:
            output_file = f"social_stats_multi_{date_str}.{ext}"
    
    try:
        # Fetch data based on input method
        if args.coins_file:
            # Read coin IDs from file and fetch data for each
            print(f"Reading coin IDs from: {args.coins_file}")
            coin_ids = read_coin_ids_from_file(args.coins_file)
            print(f"Found {len(coin_ids)} coin IDs to query\n")
            
            data = fetch_multiple_coins(coin_ids, api_key=api_key, verbose=args.verbose)
            multi_coin = True
            
        else:
            # Single coin query
            if args.verbose:
                print(f"Fetching social stats for coin ID: {args.coin_id}")
            data = fetch_social_stats(coin_id=args.coin_id, api_key=api_key)
            multi_coin = False
        
        # Display summary if verbose and single coin
        if args.verbose and not args.coins_file:
            print(f"\nResponse Status: {data.get('Response', 'Unknown')}")
            if 'Data' in data and data.get('Response') == 'Success':
                social_data = data['Data']
                general = social_data.get('General', {})
                twitter = social_data.get('Twitter', {})
                reddit = social_data.get('Reddit', {})
                cc = social_data.get('CryptoCompare', {})
                
                print(f"Coin: {general.get('CoinName', 'N/A')} ({general.get('Name', 'N/A')})")
                print(f"Twitter Followers: {twitter.get('followers', 0):,}")
                print(f"Reddit Subscribers: {reddit.get('subscribers', 0):,}")
                print(f"CryptoCompare PageViews: {cc.get('PageViews', 0):,}")
            print()
        
        # Save in requested format
        if args.format == 'json':
            pretty = not args.compact
            save_as_json(data, output_file, pretty=pretty)
        elif args.format == 'csv':
            save_as_csv(data, output_file, multi_coin=multi_coin)
        elif args.format == 'summary':
            save_as_summary(data, output_file, multi_coin=multi_coin)
        
        print(f"\n✓ Success! Social statistics enumerated and saved.")
        
    except FileNotFoundError as e:
        print(f"✗ Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"✗ Error fetching social stats: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
