# Blockchain Enumeration Script

## Overview

`enumerate_blockchains.py` fetches the complete list of blockchains from the CryptoCompare API and saves it in multiple formats for use in comparisons or as input to other scripts.

## Features

- **Multiple output formats**: JSON (full API response), CSV (tabular), or simple list (one symbol per line)
- **Flexible output**: Custom filenames or automatic date-based naming
- **API authentication**: Supports API key via command-line or environment variable
- **Complete data**: Retrieves all 809+ blockchains supported by CryptoCompare
- **Verbose mode**: Optional detailed output showing response status and sample data

## Usage

### Basic Usage (JSON format)

```bash
# Requires API key - set via environment variable
export CRYPTOCOMPARE_API_KEY=your_api_key_here
python scripts/enumerate_blockchains.py
```

PowerShell:
```powershell
$env:CRYPTOCOMPARE_API_KEY = "your_api_key_here"
python scripts/enumerate_blockchains.py
```

### Output Formats

#### JSON Format (Default)
Full API response with all blockchain metadata:

```bash
python scripts/enumerate_blockchains.py --format json --verbose
```

Output: `blockchain_list_20260102.json`

#### Simple List Format
One blockchain symbol per line - perfect for piping to other scripts:

```bash
python scripts/enumerate_blockchains.py --format list -o blockchain_symbols.txt
```

Output example:
```
0XBTC
1ST
1WO
AAC
ABCC
ABT
...
```

#### CSV Format
Structured data for spreadsheet analysis and comparisons:

```bash
python scripts/enumerate_blockchains.py --format csv -o blockchain_list.csv
```

Output example:
```csv
symbol,name,blockchain_type
0XBTC,"",""
1ST,"",""
ADA,"Cardano","blockchain"
BTC,"Bitcoin","blockchain"
ETH,"Ethereum","blockchain"
...
```

### Custom Output File

```bash
# Specify custom output filename
python scripts/enumerate_blockchains.py -o my_blockchains.json

# With different format
python scripts/enumerate_blockchains.py --format csv -o my_data.csv
```

### With API Key

```bash
# Via command-line argument
python scripts/enumerate_blockchains.py --api-key YOUR_API_KEY

# Via environment variable (recommended)
export CRYPTOCOMPARE_API_KEY=YOUR_API_KEY
python scripts/enumerate_blockchains.py
```

### Verbose Output

```bash
python scripts/enumerate_blockchains.py --verbose
```

Shows:
- Response status
- Total blockchain count
- Sample of first 5 blockchains

### Compact JSON Output

```bash
# Remove pretty-printing for smaller file size
python scripts/enumerate_blockchains.py --compact
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--format {json,list,csv}` | Output format | `json` |
| `-o, --output FILE` | Output file path | `blockchain_list_YYYYMMDD.{ext}` |
| `--api-key KEY` | CryptoCompare API key | `CRYPTOCOMPARE_API_KEY` env var |
| `--pretty` | Pretty-print JSON (enabled by default) | `True` |
| `--compact` | Compact JSON (no pretty-printing) | `False` |
| `--verbose` | Print summary information | `False` |

## Output Files

### Default Naming Convention

Files are automatically named with current date:

```
blockchain_list_20260102.json    # JSON format
blockchain_list_20260102.txt     # List format
blockchain_list_20260102.csv     # CSV format
```

### File Contents

**JSON**: Complete API response including all metadata
**List**: One blockchain symbol per line (sorted alphabetically)
**CSV**: Three columns: symbol, name, blockchain_type

## API Reference

**Endpoint**: `https://min-api.cryptocompare.com/data/blockchain/list`

**Authentication**: **Required** - Must provide API key via `authorization: Apikey {key}` header

**Response**: Returns dictionary with blockchain symbols as keys and metadata as values

## Use Cases

### 1. Compare Available Blockchains

```bash
# Enumerate today's blockchain list
python scripts/enumerate_blockchains.py --format list -o blockchains_today.txt

# Compare with previous enumeration
diff blockchains_yesterday.txt blockchains_today.txt
```

### 2. Input to Other Scripts

```bash
# Generate list of blockchains
python scripts/enumerate_blockchains.py --format list -o blockchain_symbols.txt

# Use in another script
while read symbol; do
  echo "Processing $symbol..."
  python scripts/some_other_script.py --blockchain "$symbol"
done < blockchain_symbols.txt
```

### 3. Data Analysis

```bash
# Export to CSV for analysis
python scripts/enumerate_blockchains.py --format csv -o blockchains.csv

# Open in Excel, pandas, or other tools for analysis
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

- ⚠️ **API Key Required**: This endpoint requires authentication - it will not work without an API key
- 📊 **Data Count**: As of January 2026, the API returns **809 blockchains**
- 🔄 **Update Frequency**: Run periodically to track new blockchain additions
- 💾 **File Size**: JSON output is ~100KB, list is ~5KB, CSV is ~20KB

## Examples

### Daily Blockchain Snapshot

```bash
#!/bin/bash
# daily_blockchain_snapshot.sh

export CRYPTOCOMPARE_API_KEY=your_key_here
DATE=$(date +%Y%m%d)

# Generate all three formats
python scripts/enumerate_blockchains.py --format json -o "snapshots/blockchains_$DATE.json"
python scripts/enumerate_blockchains.py --format csv -o "snapshots/blockchains_$DATE.csv"
python scripts/enumerate_blockchains.py --format list -o "snapshots/blockchains_$DATE.txt"

echo "Snapshot complete for $DATE"
```

### Blockchain Discovery Workflow

```bash
# 1. Enumerate all blockchains
python scripts/enumerate_blockchains.py --format list -o all_blockchains.txt

# 2. Filter for specific criteria
grep -i "BTC" all_blockchains.txt > bitcoin_related.txt

# 3. Query detailed info for filtered list
while read symbol; do
  python scripts/query_blockchain_info.py --symbol "$symbol"
done < bitcoin_related.txt
```
