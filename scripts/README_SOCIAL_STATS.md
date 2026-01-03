# Social Media Statistics Enumeration Script

## Overview

`enumerate_social_stats.py` fetches comprehensive social media statistics for cryptocurrencies from the CryptoCompare API, including metrics from Twitter, Reddit, Facebook, GitHub, and CryptoCompare platforms.

## Features

- **Single coin queries**: Get detailed social stats for a specific cryptocurrency by coin ID
- **Bulk queries**: Process multiple coins from a file
- **Comprehensive metrics**: Twitter followers, Reddit subscribers, GitHub stars, CryptoCompare page views, and more
- **Multiple output formats**: JSON (full API response), CSV (tabular), or Summary (human-readable)
- **Flexible input**: Command-line argument for quick queries or file-based input for batch processing
- **Rich data**: Includes engagement metrics like posts/day, comments/day, contributors, etc.

## Social Metrics Included

### Twitter
- Followers, Following, Lists, Favorites
- Tweet count (statuses)
- Account creation date
- Engagement points

### Reddit
- Subscribers, Active users
- Posts per hour/day
- Comments per hour/day
- Community creation date
- Engagement points

### GitHub
- Stars, Forks, Subscribers
- Contributors count
- Open/Closed issues and pull requests
- Repository size
- Fork status

### CryptoCompare
- Followers, Page views
- Comments, Posts
- Page view splits (Overview, Markets, Analysis, Charts, etc.)
- Cryptopian followers
- Engagement points

### General
- Total engagement points
- Coin name and symbol

## Usage

### Basic Usage (Single Coin)

```bash
# Requires API key
export CRYPTOCOMPARE_API_KEY=your_api_key_here

# Get social stats for Bitcoin (coin ID 1182)
python scripts/enumerate_social_stats.py --coin-id 1182 --verbose
```

PowerShell:
```powershell
$env:CRYPTOCOMPARE_API_KEY = "your_api_key_here"
python scripts/enumerate_social_stats.py --coin-id 1182 --verbose
```

Output:
```
Fetching social stats for coin ID: 1182

Response Status: Success
Coin: Bitcoin (BTC)
Twitter Followers: 8,231,389
Reddit Subscribers: 8,014,031
CryptoCompare PageViews: 74,312,755

✓ Saved JSON to: social_stats_1182_20260102.json
```

### Multiple Coins from File

Create a file with coin IDs (one per line):

**coin_ids.txt:**
```
# Bitcoin
1182
# Ethereum
7605
# Cardano
5038
```

Run the script:
```bash
python scripts/enumerate_social_stats.py --coins-file coin_ids.txt --verbose
```

### Output Formats

#### JSON Format (Default)
Full API response with all social metrics:

```bash
python scripts/enumerate_social_stats.py --coin-id 1182 --format json
```

Output structure includes:
- General (coin name, symbol, total points)
- CryptoCompare (followers, page views, comments, posts)
- Twitter (followers, tweets, lists)
- Reddit (subscribers, posts/day, comments/day)
- Facebook (points)
- CodeRepository (GitHub stars, forks, contributors)

#### CSV Format
Structured data for spreadsheet analysis:

```bash
# Single coin - vertical format (metric, value)
python scripts/enumerate_social_stats.py --coin-id 1182 --format csv -o btc_social.csv
```

Single coin CSV:
```csv
metric,value
"Coin Name","Bitcoin"
"Symbol","BTC"
"Total Points",22742668
"Twitter Followers",8231389
"Reddit Subscribers",8014031
"GitHub Stars",85575
"CryptoCompare PageViews",74312755
```

Multiple coins CSV:
```csv
coin_id,coin_name,symbol,twitter_followers,reddit_subscribers,github_stars,cryptocompare_followers,cryptocompare_pageviews
1182,"Bitcoin","BTC",8231389,8014031,85575,113045,74312749
7605,"Ethereum","ETH",4060523,3700610,13520,95434,32473640
```

#### Summary Format
Human-readable report with all metrics:

```bash
python scripts/enumerate_social_stats.py --coin-id 1182 --format summary
```

Output includes detailed breakdown of Twitter, Reddit, GitHub, and CryptoCompare metrics with proper formatting.

### Custom Output File

```bash
# Specify custom output filename
python scripts/enumerate_social_stats.py --coin-id 1182 -o my_social_stats.json

# With different format
python scripts/enumerate_social_stats.py --coin-id 1182 --format csv -o my_data.csv
```

### Compact JSON Output

```bash
# Remove pretty-printing for smaller file size
python scripts/enumerate_social_stats.py --coin-id 1182 --compact
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--coin-id ID` | Cryptocurrency coin ID (e.g., 1182 for BTC) | None (required unless using --coins-file) |
| `--coins-file FILE` | File with coin IDs (one per line) | None |
| `--format {json,csv,summary}` | Output format | `json` |
| `-o, --output FILE` | Output file path | Auto-generated |
| `--api-key KEY` | CryptoCompare API key | `CRYPTOCOMPARE_API_KEY` env var |
| `--pretty` | Pretty-print JSON (enabled by default) | `True` |
| `--compact` | Compact JSON (no pretty-printing) | `False` |
| `--verbose` | Print detailed progress information | `False` |

## Output Files

### Default Naming Convention

Files are automatically named based on query type and date:

```
social_stats_1182_20260102.json      # Single coin (BTC)
social_stats_multi_20260102.json     # Multiple coins from file
```

Extensions change based on format:
- `.json` for JSON format
- `.csv` for CSV format
- `.txt` for summary format

## API Reference

**Endpoint**: `https://min-api.cryptocompare.com/data/social/coin/latest`

**Authentication**: **Required** - Must provide API key via `authorization: Apikey {key}` header

**Query Parameters**:
- `coinId` (required): Cryptocurrency coin ID

**Response Structure**: Complex nested object with General, CryptoCompare, Twitter, Reddit, Facebook, and CodeRepository sections

## Common Coin IDs

| Coin | Symbol | Coin ID |
|------|--------|---------|
| Bitcoin | BTC | 1182 |
| Ethereum | ETH | 7605 |
| Cardano | ADA | 5038 |
| Monero | XMR | 5038 |
| Litecoin | LTC | 3808 |
| Ripple | XRP | 5031 |

## Use Cases

### 1. Compare Social Engagement Across Cryptocurrencies

```bash
# Create list of top coins
cat > top_coins.txt << EOF
1182
7605
5038
3808
EOF

# Get social stats for all
python scripts/enumerate_social_stats.py --coins-file top_coins.txt --format csv -o top_coins_social.csv

# Analyze in spreadsheet - sort by Twitter followers, Reddit subscribers, etc.
```

### 2. Monitor Social Growth Over Time

```bash
#!/bin/bash
# Daily social stats snapshot
DATE=$(date +%Y%m%d)
python scripts/enumerate_social_stats.py --coin-id 1182 --format csv -o "snapshots/btc_social_$DATE.csv"

# Compare with previous day
diff snapshots/btc_social_yesterday.csv snapshots/btc_social_$DATE.csv
```

### 3. Identify Most Active Communities

```bash
# Get stats for multiple coins
python scripts/enumerate_social_stats.py --coins-file all_coins.txt --format csv -o social_comparison.csv

# Sort by Reddit activity
sort -t',' -k5 -nr social_comparison.csv | head -10
```

### 4. GitHub Repository Analysis

```bash
# Extract GitHub metrics for development activity analysis
python scripts/enumerate_social_stats.py --coin-id 1182 --format json -o btc_social.json

# Parse GitHub stars, forks, contributors
jq '.Data.CodeRepository.List[0] | {stars, forks, contributors}' btc_social.json
```

### 5. Social Sentiment Dashboard Data

```bash
# Collect data for dashboard
python scripts/enumerate_social_stats.py --coins-file dashboard_coins.txt --format json -o social_dashboard_data.json

# Extract key metrics for visualization
jq '.[] | {coin: .Data.General.Name, twitter: .Data.Twitter.followers, reddit: .Data.Reddit.subscribers}' social_dashboard_data.json
```

## Requirements

```
requests>=2.31.0
```

Install with:

```bash
pip install requests
```

## Error Handling

- **Authentication errors**: Script exits if API key is invalid or missing
- **Invalid coin IDs**: Returns error in output for that specific coin
- **Network errors**: HTTP request failures are caught and reported
- **File not found**: Returns clear error message if coins file doesn't exist

## API Key Setup

1. Get your free API key from: https://www.cryptocompare.com/cryptopian/api-keys
2. Set environment variable:
   ```bash
   # Linux/macOS
   export CRYPTOCOMPARE_API_KEY=your_key_here
   
   # Windows PowerShell
   $env:CRYPTOCOMPARE_API_KEY = "your_key_here"
   ```
3. Or add to your `config/cryptocompare.env` file

## Coin IDs File Format

Create a text file with one coin ID per line:

```
# Lines starting with # are ignored (comments)
1182  # Bitcoin
7605  # Ethereum

# Empty lines are also ignored
5038  # Cardano
```

The script automatically:
- Strips whitespace from each line
- Ignores empty lines
- Ignores lines starting with `#`
- Extracts just the coin ID (ignores inline comments)

## Notes

- ⚠️ **API Key Required**: This endpoint requires authentication
- 📊 **Comprehensive Data**: Returns 10+ categories of social metrics
- 🔄 **Real-time Data**: Social stats are updated regularly by CryptoCompare
- 💾 **File Sizes**: JSON output is ~5-10KB per coin
- ⏱️ **Rate Limits**: Be mindful of API rate limits when querying many coins

## Example Social Stats (Bitcoin as of Jan 2026)

```
Coin: Bitcoin (BTC)
Total Points: 22,742,668

Twitter Followers: 8,231,389
Twitter Tweets: 29,751

Reddit Subscribers: 8,014,031
Reddit Posts/Day: 140.99
Reddit Comments/Day: 6,088.79

GitHub Stars: 85,575
GitHub Forks: 37,812
GitHub Contributors: 1,259

CryptoCompare Page Views: 74,312,755
CryptoCompare Followers: 113,045
CryptoCompare Comments: 651,489
```

## Troubleshooting

### "You need a valid auth key or api key"

You haven't set your API key. Set the `CRYPTOCOMPARE_API_KEY` environment variable or use `--api-key` parameter.

### Invalid coin ID errors

Verify the coin ID is correct. You can find coin IDs in the CryptoCompare API documentation or by inspecting network requests on cryptocompare.com.

### Missing data in response

Some coins may not have complete social data (e.g., no GitHub repository, limited Twitter presence). The script handles missing data gracefully by using 0 or N/A values.

## Examples

### Quick Bitcoin Social Stats

```bash
python scripts/enumerate_social_stats.py --coin-id 1182 --format summary --verbose
```

### Daily Social Monitoring Report

```powershell
# PowerShell script for Windows Task Scheduler
$env:CRYPTOCOMPARE_API_KEY = "your_key_here"
$date = Get-Date -Format "yyyyMMdd"

# Top 10 coins by market cap
$coins = @(1182, 7605, 5038, 3808, 5031)

foreach ($coinId in $coins) {
    python scripts/enumerate_social_stats.py --coin-id $coinId --format summary -o "reports\social_${coinId}_$date.txt"
}
```

### Comparative Analysis

```bash
# Get social stats for DeFi coins
cat > defi_coins.txt << EOF
7605  # Ethereum
5031  # Ripple/XRP
4614  # Polkadot
EOF

python scripts/enumerate_social_stats.py --coins-file defi_coins.txt --format csv -o defi_social_comparison.csv

# Analyze the data
column -t -s',' defi_social_comparison.csv
```

## Integration with Other Scripts

### Find Coins with Strong Social Presence

```python
# analyze_social_strength.py
import csv

def calculate_social_score(row):
    twitter = int(row['twitter_followers'])
    reddit = int(row['reddit_subscribers'])
    github = int(row['github_stars'])
    return twitter * 0.3 + reddit * 0.4 + github * 0.3

with open('multi_social.csv', 'r') as f:
    reader = csv.DictReader(f)
    coins = [(row['coin_name'], calculate_social_score(row)) for row in reader]

for name, score in sorted(coins, key=lambda x: x[1], reverse=True):
    print(f"{name}: {score:,.0f}")
```

### Social Growth Tracking

```bash
# Track social metrics over time
COIN_ID=1182
DATE=$(date +%Y%m%d)

python scripts/enumerate_social_stats.py --coin-id $COIN_ID --format csv -o "history/social_${COIN_ID}_$DATE.csv"

# Compare with last week
LAST_WEEK=$(date -d '7 days ago' +%Y%m%d)
diff history/social_${COIN_ID}_$LAST_WEEK.csv history/social_${COIN_ID}_$DATE.csv
```
