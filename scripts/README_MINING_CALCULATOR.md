# Mining Calculator Enumeration Script

## Overview

`enumerate_mining_calculator.py` fetches blockchain mining calculator data from the CryptoCompare API for one or many symbols. It reports hashrate, block reward, block time, supply, launch date, and prices in one or more quote currencies.

## Features

- Single symbol via `--fsyms` (e.g., `XMR`)
- Multiple symbols via comma list or `--symbols-file` (one per line)
- Multiple quote currencies via `--tsyms` (e.g., `USD,EUR`)
- Output formats: JSON (full), CSV (tabular), Summary (human-readable)
- API key support via `CRYPTOCOMPARE_API_KEY` or `--api-key`

## Usage

### Single Symbol

```bash
export CRYPTOCOMPARE_API_KEY=your_api_key
python scripts/enumerate_mining_calculator.py --fsyms XMR --tsyms USD --verbose
```

### Multiple Symbols (inline)

```bash
python scripts/enumerate_mining_calculator.py --fsyms BTC,ETH,XMR --tsyms USD
```

### Symbols from File

Create `test_mining_symbols.txt`:
```
BTC
ETH
XMR
```

Run:
```bash
python scripts/enumerate_mining_calculator.py --symbols-file test_mining_symbols.txt --tsyms USD,EUR --format summary
```

### CSV Output

```bash
python scripts/enumerate_mining_calculator.py --fsyms BTC,ETH --tsyms USD --format csv -o mining_calc.csv
```

### Summary Output

```bash
python scripts/enumerate_mining_calculator.py --symbols-file test_mining_symbols.txt --tsyms USD,EUR --format summary -o mining_calc_summary.txt
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--fsyms` | Comma-separated symbols (e.g., `BTC,ETH,XMR`) | None |
| `--symbols-file` | File with symbols (one per line) | None |
| `--tsyms` | Comma-separated quote currencies | `USD` |
| `--format {json,csv,summary}` | Output format | `json` |
| `-o, --output` | Output file path | `mining_calc_<date>.<ext>` |
| `--api-key` | CryptoCompare API key | `CRYPTOCOMPARE_API_KEY` env var |
| `--pretty/--compact` | Pretty-print JSON or compact | Pretty on |
| `--verbose` | Print summary info | False |

## Output Formats

- **JSON**: Full API response
- **CSV**: Columns `symbol, full_name, block_height, block_time_seconds, block_reward, net_hashes_per_second, total_coins_mined, max_supply, asset_launch_date, price_<TSYM>...`
- **Summary**: Stats and first few symbols with prices

## Examples

- `mining_calc_inline_20260102.json` — XMR, USD
- `mining_calc.csv` — BTC/ETH/XMR in USD (tabular)
- `mining_calc_summary.txt` — BTC/ETH/XMR in USD/EUR (readable report)
- `test_mining_symbols.txt` — sample symbols file

## API Reference

Endpoint: `https://min-api.cryptocompare.com/data/blockchain/mining/calculator`

Parameters:
- `fsyms` (required): comma list of symbols
- `tsyms` (required): comma list of quote currencies

Auth: **API key required** (`authorization: Apikey {key}`)

## Notes

- Hashrate is reported in `NetHashesPerSecond`
- `BlockReward` and `BlockTime` give quick profitability context
- `MaxSupply` may be `-1` for uncapped assets
- File sizes: JSON (~few KB per symbol), CSV small, Summary small

## Use Cases

- Build mining dashboards (hashrate, block reward, price)
- Compare mining metrics across coins (e.g., BTC vs XMR)
- Feed profit calculators with current price + block data
- Track changes over time by scheduling daily snapshots
