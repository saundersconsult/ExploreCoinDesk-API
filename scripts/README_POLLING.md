# Trading Signals Polling Script

## Overview

`poll_trading_signals.py` is a simple script to poll the CryptoCompare IntoTheBlock Trading Signals endpoint and log the results to a file.

## Features

- **Date-based log files**: Automatically creates log files with pattern `scriptname-YYYY-MMDD-apis.log`
- **Multiple formats**: Supports CSV (default) and JSON (JSONL) logging
- **Append mode**: Appends to existing log files, creates new ones if needed
- **Error handling**: Captures and logs errors gracefully
- **Flexible authentication**: Supports API key via command-line or environment variable

## Usage

### Basic Usage (CSV format)

```bash
python scripts/poll_trading_signals.py
```

### JSON Format

```bash
python scripts/poll_trading_signals.py --format json
```

### With API Key

```bash
# Via command-line
python scripts/poll_trading_signals.py --api-key YOUR_API_KEY

# Via environment variable (recommended)
export CRYPTOCOMPARE_API_KEY=YOUR_API_KEY
python scripts/poll_trading_signals.py
```

### Verbose Output

```bash
python scripts/poll_trading_signals.py --verbose
```

### Different Symbol

```bash
python scripts/poll_trading_signals.py --fsym ETH
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--format {csv,json}` | Output format | `csv` |
| `--api-key API_KEY` | API key for authentication | None |
| `--fsym FSYM` | From symbol (cryptocurrency) | `BTC` |
| `--verbose` | Print response data to console | False |

## Log File Format

### CSV Format

Creates a CSV file with headers and one row per poll:

```csv
timestamp,success,message,id,time,symbol,partner_symbol,inOutVar,addressesNetGrowth,concentrationVar,largetxsVar
2026-01-02T20:48:38.009400,True,,1182,1755129600,BTC,BTC,"{""category"": ""on_chain"", ...}","...","...","..."
```

- Nested objects are JSON-stringified within the CSV
- File includes headers on first write
- Subsequent runs append without re-writing headers

### JSON Format (JSONL)

Creates a JSONL (JSON Lines) file with one JSON object per line:

```json
{"timestamp": "2026-01-02T20:48:53.130672", "data": {"Response": "Success", ...}}
{"timestamp": "2026-01-02T20:49:15.234567", "data": {"Response": "Success", ...}}
```

Each line is a complete JSON object that can be parsed independently.

## Example Workflow

### Scheduled Polling

Use with cron (Linux/macOS) or Task Scheduler (Windows) for automated polling:

```bash
# Poll every hour and log to CSV
0 * * * * cd /path/to/repo && python scripts/poll_trading_signals.py

# Poll every 15 minutes and log to JSON
*/15 * * * * cd /path/to/repo && python scripts/poll_trading_signals.py --format json
```

### Log Rotation

Log files are automatically separated by date (YYYY-MMDD), so each day gets its own file:

```
poll_trading_signals-2026-0102-apis.log
poll_trading_signals-2026-0103-apis.log
poll_trading_signals-2026-0104-apis.log
```

## Error Handling

- Network errors are captured and logged with error details
- API errors (rate limits, authentication failures) are logged
- Script exits with code 1 on error, 0 on success

## Requirements

```python
requests>=2.31.0
```

Install with:

```bash
pip install requests
```

## API Reference

**Endpoint**: `https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest`

**Authentication**: Requires `x-api-key` header (recommended) or works with rate limits without key

**Documentation**: See `full_api_documentation_selenium.json` for complete endpoint details

## Notes

- ⚠️ **API Key Recommended**: While the endpoint works without an API key, you'll be subject to strict rate limits
- The IntoTheBlock trading signals endpoint provides on-chain metrics including:
  - In/Out Variance (inOutVar)
  - Address Network Growth (addressesNetGrowth)
  - Concentration Variance (concentrationVar)
  - Large Transaction Variance (largetxsVar)
- Each metric includes sentiment (bullish/bearish), value, and score
