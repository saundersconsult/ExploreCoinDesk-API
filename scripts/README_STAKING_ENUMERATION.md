# Staking Data Enumeration Script

## Overview

`enumerate_staking.py` fetches blockchain staking data from the CryptoCompare API and saves it in multiple formats for use in comparisons or as input to other scripts. The script supports querying staking rates for specific cryptocurrencies or multiple symbols from a file.

## Features

- **Single symbol queries**: Get staking data for a specific cryptocurrency (e.g., ETH)
- **Bulk queries**: Process multiple symbols from a file
- **Multiple output formats**: JSON (full API response), CSV (tabular), or Summary (human-readable)
- **Flexible input**: Command-line argument for quick queries or file-based input for batch processing
- **Error handling**: Gracefully handles invalid symbols and API errors
- **Verbose mode**: Optional detailed output showing staking rates and dates

## Important Note

⚠️ **Limited Symbol Support**: As of January 2026, this endpoint only supports **ETH (Ethereum)** for staking data queries. Other symbols will return an error message indicating the allowed values.

## Usage

### Basic Usage (All Staking Data)

```bash
# Requires API key - set via environment variable
export CRYPTOCOMPARE_API_KEY=your_api_key_here
python scripts/enumerate_staking.py --verbose
```

PowerShell:
```powershell
$env:CRYPTOCOMPARE_API_KEY = "your_api_key_here"
python scripts/enumerate_staking.py --verbose
```

### Single Symbol Query

```bash
# Get ETH staking data
python scripts/enumerate_staking.py --fsym ETH --verbose
```

Output:
```
Fetching staking data for: ETH

Response Status: Success
Message:

Staking Information:
  Rate: 2.3306%
  Issued: 2026-01-02T11:00:00Z

✓ Saved JSON to: staking_eth_20260102.json
```

### Multiple Symbols from File

Create a file with symbols (one per line):

**symbols.txt:**
```
ETH
BTC
ADA
DOT
SOL
```

Run the script:
```bash
python scripts/enumerate_staking.py --symbols-file symbols.txt --verbose
```

Output shows staking data for ETH and errors for unsupported symbols.

### Output Formats

#### JSON Format (Default)
Full API response with all metadata:

```bash
python scripts/enumerate_staking.py --fsym ETH --format json
```

Output: `staking_eth_20260102.json`
```json
{
  "Response": "Success",
  "Message": "",
  "HasWarning": false,
  "Type": 100,
  "RateLimit": {},
  "Data": {
    "rate": 2.3306,
    "issued_ts": 1767351600,
    "issued_date": "2026-01-02T11:00:00Z",
    "notes": []
  }
}
```

#### CSV Format
Structured data for spreadsheet analysis:

```bash
python scripts/enumerate_staking.py --fsym ETH --format csv -o eth_staking.csv
```

Single symbol output:
```csv
rate,issued_ts,issued_date,notes
2.3306,1767351600,"2026-01-02T11:00:00Z",""
```

Multiple symbols output:
```csv
symbol,response_status,message,rate,issued_date
ETH,Success,"",2.3306,"2026-01-02T11:00:00Z"
BTC,Error,"fsym param with value: BTC is invalid. (fsym allowed values: ETH)",,""
```

#### Summary Format
Human-readable text format:

```bash
python scripts/enumerate_staking.py --fsym ETH --format summary
```

Output: `staking_eth_20260102.txt`
```
================================================================================
BLOCKCHAIN STAKING DATA SUMMARY
Generated: 2026-01-02 20:15:30
================================================================================

Response: Success
Message: N/A

Staking Information:
--------------------------------------------------------------------------------
Staking Rate: 2.3306%
Issued Date: 2026-01-02T11:00:00Z
Issued Timestamp: 1767351600
```

### Custom Output File

```bash
# Specify custom output filename
python scripts/enumerate_staking.py --fsym ETH -o my_staking_data.json

# With different format
python scripts/enumerate_staking.py --fsym ETH --format csv -o my_data.csv
```

### With API Key

```bash
# Via command-line argument
python scripts/enumerate_staking.py --fsym ETH --api-key YOUR_API_KEY

# Via environment variable (recommended)
export CRYPTOCOMPARE_API_KEY=YOUR_API_KEY
python scripts/enumerate_staking.py --fsym ETH
```

### Compact JSON Output

```bash
# Remove pretty-printing for smaller file size
python scripts/enumerate_staking.py --fsym ETH --compact
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--fsym SYMBOL` | Cryptocurrency symbol to query (e.g., ETH) | None (all data) |
| `--symbols-file FILE` | File with symbols (one per line) | None |
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
staking_eth_20260102.json        # Single symbol (ETH)
staking_all_20260102.json        # All staking data
staking_multi_20260102.json      # Multiple symbols from file
```

Extensions change based on format:
- `.json` for JSON format
- `.csv` for CSV format
- `.txt` for summary format

### File Contents

**JSON**: Complete API response including rate, timestamp, date, and notes
**CSV**: Structured rows with rate, issued_ts, issued_date, and notes columns
**Summary**: Human-readable text with formatted staking information

## API Reference

**Endpoint**: `https://min-api.cryptocompare.com/data/blockchain/staking/latest`

**Authentication**: **Required** - Must provide API key via `authorization: Apikey {key}` header

**Query Parameters**:
- `fsym` (optional): Cryptocurrency symbol filter (currently only supports ETH)

**Response Structure**:
```json
{
  "Response": "Success|Error",
  "Message": "error message if any",
  "Data": {
    "rate": 2.3306,
    "issued_ts": 1767351600,
    "issued_date": "2026-01-02T11:00:00Z",
    "notes": []
  }
}
```

## Use Cases

### 1. Monitor ETH Staking Rates Over Time

```bash
# Daily snapshot
python scripts/enumerate_staking.py --fsym ETH --format csv -o "snapshots/eth_staking_$(date +%Y%m%d).csv"

# Compare rates across days
cat snapshots/eth_staking_*.csv
```

### 2. Validate Symbol Support

```bash
# Create test file with various symbols
cat > test_symbols.txt << EOF
ETH
BTC
ADA
DOT
SOL
EOF

# Test which symbols are supported
python scripts/enumerate_staking.py --symbols-file test_symbols.txt --format csv -o symbol_validation.csv

# Review results
cat symbol_validation.csv
```

### 3. Automated Monitoring

```bash
#!/bin/bash
# monitor_eth_staking.sh - Run hourly to track ETH staking rate changes

export CRYPTOCOMPARE_API_KEY=your_key_here
DATE=$(date +%Y%m%d_%H%M)

python scripts/enumerate_staking.py --fsym ETH --format csv -o "logs/eth_staking_$DATE.csv"

# Send alert if rate changed significantly
# ... (add your alert logic here)
```

### 4. Integration with Other Scripts

```bash
# Generate symbols to test from blockchain list
python scripts/enumerate_blockchains.py --format list -o blockchain_symbols.txt

# Test staking support for each blockchain
python scripts/enumerate_staking.py --symbols-file blockchain_symbols.txt --format csv -o staking_support_matrix.csv

# Analyze results
grep "Success" staking_support_matrix.csv > supported_staking.csv
grep "Error" staking_support_matrix.csv > unsupported_staking.csv
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
- **Invalid symbols**: Returns error message in output indicating allowed values
- **Network errors**: HTTP request failures are caught and reported
- **File not found**: Returns clear error message if symbols file doesn't exist

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

## Symbols File Format

Create a text file with one symbol per line:

```
# Lines starting with # are ignored (comments)
ETH
BTC
ADA

# Empty lines are also ignored
DOT
SOL
```

The script automatically:
- Strips whitespace from each line
- Ignores empty lines
- Ignores lines starting with `#`

## Notes

- ⚠️ **API Key Required**: This endpoint requires authentication
- 📊 **Limited Symbol Support**: Currently only **ETH** returns staking data
- 🔄 **Rate Information**: Returns current staking rate as a percentage
- ⏰ **Timestamp**: Includes both Unix timestamp and ISO 8601 date format
- 💾 **File Size**: JSON output is typically < 1KB per query

## Troubleshooting

### "fsym param with value: X is invalid"

This means the symbol you requested doesn't have staking data available. Currently, only ETH is supported. Use `--fsym ETH` or check the error message for allowed values.

### "You need a valid auth key or api key"

You haven't set your API key. Set the `CRYPTOCOMPARE_API_KEY` environment variable or use `--api-key` parameter.

### Network timeout errors

The default timeout is 30 seconds. If you're experiencing timeouts:
- Check your internet connection
- Verify the API endpoint is accessible
- Try again after a few moments

## Examples

### Quick ETH Staking Rate Check

```bash
python scripts/enumerate_staking.py --fsym ETH --verbose
```

### Daily Staking Report

```powershell
# PowerShell script for Windows Task Scheduler
$env:CRYPTOCOMPARE_API_KEY = "your_key_here"
$date = Get-Date -Format "yyyyMMdd"

python scripts/enumerate_staking.py --fsym ETH --format summary -o "reports\staking_$date.txt"
```

### Bulk Symbol Testing

```bash
# Test all blockchain symbols for staking support
python scripts/enumerate_blockchains.py --format list -o all_symbols.txt
python scripts/enumerate_staking.py --symbols-file all_symbols.txt --format csv -o staking_availability.csv

# Find which ones support staking
grep "Success" staking_availability.csv
```
