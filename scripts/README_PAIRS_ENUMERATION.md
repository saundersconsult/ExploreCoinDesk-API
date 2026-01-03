# Trading Pairs Enumeration Script

## Overview

`enumerate_pairs.py` fetches the complete list of trading pairs from the CryptoCompare CCCAGG API and saves it in multiple formats for use in comparisons, market analysis, or as input to other scripts.

## Features

- **Comprehensive data**: Retrieves all 5,500+ base symbols and 12,000+ trading pairs
- **Market information**: Includes which exchanges (markets) support each pair
- **Multiple output formats**: JSON (full API response), CSV (tabular), or Summary (human-readable)
- **Markets extraction**: Can extract a unique list of all 93 exchanges/markets
- **Flexible output**: Custom filenames or automatic date-based naming
- **API authentication**: Supports API key via command-line or environment variable

## Data Overview

As of January 2026, the API returns:
- **5,511 base symbols** (cryptocurrencies)
- **12,243 trading pairs** (base/quote combinations)
- **93 unique markets** (exchanges)

## Usage

### Basic Usage (JSON format)

```bash
# Requires API key - set via environment variable
export CRYPTOCOMPARE_API_KEY=your_api_key_here
python scripts/enumerate_pairs.py --verbose
```

PowerShell:
```powershell
$env:CRYPTOCOMPARE_API_KEY = "your_api_key_here"
python scripts/enumerate_pairs.py --verbose
```

Output:
```
Fetching trading pairs from CryptoCompare API...

Response Status: Success
Total Base Symbols: 5511
Total Trading Pairs: 12243
Unique Markets: 93

Sample pairs:
  00/USD: 1 market(s)
  00/USDT: 1 market(s)
  0DOG/USDT: 1 market(s)
  ... and 12238 more pairs

✓ Saved JSON to: pairs_20260102.json
```

### Output Formats

#### JSON Format (Default)
Full API response with all pairs and market data:

```bash
python scripts/enumerate_pairs.py --format json --verbose
```

Output structure:
```json
{
  "Response": "Success",
  "Data": {
    "BTC": {
      "USDT": {
        "markets": ["Binance", "Coinbase", "Kraken", ...]
      },
      "USD": {
        "markets": ["Coinbase", "Kraken", "Gemini", ...]
      }
    },
    "ETH": {
      "USDT": {
        "markets": ["Binance", "Coinbase", ...]
      }
    }
  }
}
```

#### CSV Format
Structured data for spreadsheet analysis:

```bash
python scripts/enumerate_pairs.py --format csv -o pairs_data.csv
```

Output example:
```csv
base_symbol,quote_symbol,markets_count,markets
"BTC","USDT",45,"Binance;Coinbase;Kraken;Gemini;..."
"BTC","USD",28,"Coinbase;Kraken;Gemini;..."
"ETH","USDT",42,"Binance;Coinbase;Kraken;..."
"ETH","BTC",35,"Binance;Kraken;Poloniex;..."
```

#### Summary Format
Human-readable report with statistics:

```bash
python scripts/enumerate_pairs.py --format summary -o pairs_summary.txt
```

Output includes:
- Total counts (base symbols, pairs, markets)
- Complete list of all 93 exchanges
- Sample trading pairs with market counts

#### Markets Only
Extract unique list of all exchanges:

```bash
python scripts/enumerate_pairs.py --markets-only -o markets.txt
```

Output (one market per line):
```
Binance
Coinbase
Kraken
Gemini
Bitfinex
...
```

### Custom Output File

```bash
# Specify custom output filename
python scripts/enumerate_pairs.py -o my_pairs.json

# With different format
python scripts/enumerate_pairs.py --format csv -o my_data.csv
```

### With API Key

```bash
# Via command-line argument
python scripts/enumerate_pairs.py --api-key YOUR_API_KEY

# Via environment variable (recommended)
export CRYPTOCOMPARE_API_KEY=YOUR_API_KEY
python scripts/enumerate_pairs.py
```

### Compact JSON Output

```bash
# Remove pretty-printing for smaller file size
python scripts/enumerate_pairs.py --compact
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--format {json,csv,summary}` | Output format | `json` |
| `-o, --output FILE` | Output file path | `pairs_YYYYMMDD.{ext}` |
| `--api-key KEY` | CryptoCompare API key | `CRYPTOCOMPARE_API_KEY` env var |
| `--pretty` | Pretty-print JSON (enabled by default) | `True` |
| `--compact` | Compact JSON (no pretty-printing) | `False` |
| `--markets-only` | Save only unique market names | `False` |
| `--verbose` | Print summary information | `False` |

## Output Files

### Default Naming Convention

Files are automatically named with current date:

```
pairs_20260102.json         # JSON format
pairs_20260102.csv          # CSV format
pairs_20260102.txt          # Summary format
markets_list_20260102.txt   # Markets only mode
```

### File Contents

**JSON**: Complete API response with nested structure (base → quote → markets)
**CSV**: Flat table with one row per trading pair
**Summary**: Statistics + all markets + sample pairs
**Markets**: One exchange name per line (93 unique markets)

## API Reference

**Endpoint**: `https://min-api.cryptocompare.com/data/cccagg/pairs`

**Authentication**: **Required** - Must provide API key via `authorization: Apikey {key}` header

**Response Structure**:
```json
{
  "Response": "Success",
  "Message": "",
  "Data": {
    "<BASE_SYMBOL>": {
      "<QUOTE_SYMBOL>": {
        "markets": ["exchange1", "exchange2", ...]
      }
    }
  }
}
```

## Use Cases

### 1. Market Coverage Analysis

```bash
# Get all pairs
python scripts/enumerate_pairs.py --format csv -o pairs.csv

# Analyze in spreadsheet or with pandas
# - Which markets have the most pairs?
# - What are the most popular quote currencies?
# - Which base currencies have the widest market coverage?
```

### 2. Exchange Comparison

```bash
# Extract markets list
python scripts/enumerate_pairs.py --markets-only -o markets.txt

# Use in scripts to compare exchange offerings
while read market; do
  echo "Analyzing $market..."
  grep "\"$market\"" pairs_data.csv | wc -l
done < markets.txt
```

### 3. Trading Pair Discovery

```bash
# Find all pairs for a specific base currency
python scripts/enumerate_pairs.py --format csv -o all_pairs.csv
grep "^\"BTC\"," all_pairs.csv > btc_pairs.csv

# Or find pairs on specific exchanges
grep "Binance" all_pairs.csv > binance_pairs.csv
```

### 4. Data Pipeline Integration

```bash
# Daily snapshot for historical tracking
DATE=$(date +%Y%m%d)
python scripts/enumerate_pairs.py --format json -o "snapshots/pairs_$DATE.json"

# Compare with previous day to track new pairs
diff snapshots/pairs_yesterday.json snapshots/pairs_today.json
```

### 5. Market Selection for Trading Bot

```bash
# Get all markets
python scripts/enumerate_pairs.py --markets-only -o markets.txt

# Filter for specific requirements
# e.g., Find markets that support both BTC/USDT and ETH/USDT
python scripts/enumerate_pairs.py --format csv -o pairs.csv
grep "\"BTC\",\"USDT\"" pairs.csv | cut -d',' -f4 > btc_markets.txt
grep "\"ETH\",\"USDT\"" pairs.csv | cut -d',' -f4 > eth_markets.txt
comm -12 <(sort btc_markets.txt) <(sort eth_markets.txt)
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

- **Authentication errors**: Script exits with error if API key is invalid or missing
- **Network errors**: HTTP request failures are caught and reported
- **API errors**: Handles rate limits and other API-specific errors gracefully

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

## Notes

- ⚠️ **API Key Required**: This endpoint requires authentication
- 📊 **Large Dataset**: JSON output is ~15MB with all 12,000+ pairs
- 🔄 **Update Frequency**: New pairs are added regularly as exchanges list new tokens
- 💾 **File Sizes**: 
  - JSON: ~15MB (full data)
  - CSV: ~500KB (flat table)
  - Summary: ~10KB (statistics + sample)
  - Markets: ~1KB (93 exchanges)

## Available Markets (93 Exchanges)

The API currently supports 93 unique exchanges including:

- **Major Exchanges**: Binance, Coinbase, Kraken, Gemini, Bitfinex, Bitstamp
- **Asian Markets**: Huobi, OKEx, Upbit, Bithumb, Bitbank, Coincheck
- **Alternative Exchanges**: Kucoin, Gateio, BitMart, MEXC, Poloniex
- **Regional Platforms**: BTCMarkets (Australia), Mercado Bitcoin (Brazil), Bitkub (Thailand)
- **Derivatives**: Bitmex, Bybit, FTX (historical data)

See `--markets-only` output for the complete current list.

## Examples

### Daily Pairs Snapshot

```bash
#!/bin/bash
# daily_pairs_snapshot.sh

export CRYPTOCOMPARE_API_KEY=your_key_here
DATE=$(date +%Y%m%d)

# Generate all formats
python scripts/enumerate_pairs.py --format json -o "snapshots/pairs_$DATE.json"
python scripts/enumerate_pairs.py --format csv -o "snapshots/pairs_$DATE.csv"
python scripts/enumerate_pairs.py --format summary -o "snapshots/pairs_$DATE.txt"
python scripts/enumerate_pairs.py --markets-only -o "snapshots/markets_$DATE.txt"

echo "Snapshot complete for $DATE"
```

### Find Pairs for Specific Symbols

```bash
# Get all pairs in CSV format
python scripts/enumerate_pairs.py --format csv -o all_pairs.csv

# Find all ETH pairs
grep "^\"ETH\"," all_pairs.csv > eth_pairs.csv

# Find all USDT pairs (as quote currency)
grep ",\"USDT\"," all_pairs.csv > usdt_pairs.csv

# Count markets per pair
awk -F',' '{print $1","$2","$3}' all_pairs.csv | sort -t',' -k3 -nr | head -20
```

### Market Availability Matrix

```python
# analyze_market_coverage.py
import csv
from collections import defaultdict

markets_coverage = defaultdict(int)

with open('pairs_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for market in row['markets'].split(';'):
            markets_coverage[market.strip('"')] += 1

# Sort by pair count
for market, count in sorted(markets_coverage.items(), key=lambda x: x[1], reverse=True):
    print(f"{market}: {count} pairs")
```

## Integration with Other Scripts

### Combine with Blockchain Enumeration

```bash
# Get all blockchains
python scripts/enumerate_blockchains.py --format list -o blockchains.txt

# Get all trading pairs
python scripts/enumerate_pairs.py --format csv -o pairs.csv

# Find which blockchains have trading pairs
while read blockchain; do
  count=$(grep -c "^\"$blockchain\"," pairs.csv || echo "0")
  echo "$blockchain: $count pairs"
done < blockchains.txt
```

### Market-Specific Analysis

```bash
# Extract all Binance pairs
python scripts/enumerate_pairs.py --format csv -o all_pairs.csv
grep "Binance" all_pairs.csv > binance_pairs.csv

# Get unique base symbols on Binance
cut -d',' -f1 binance_pairs.csv | sort -u > binance_symbols.txt
```
