# CoinDesk Derivatives API

**Base Paths**: `/futures/v1/`, `/options/v1/`  
**Status**: ✅ 7/9 endpoints working

## Overview

The Derivatives API provides access to futures and options trading data from major crypto derivatives exchanges. Includes comprehensive OHLCV data with trade breakdowns, funding rates, and contract-specific metrics.

---

## Futures API ✅

### ✅ Working Endpoints

#### Markets List
**Path**: `/futures/v1/markets`  
**Method**: GET  
**Parameters**: None required

**Supported Markets** (22 futures exchanges):
- `binance`, `bybit`, `okex`, `deribit`, `kraken`
- `bitmex`, `bitfinex`, `bitget`, `gateio`, `kucoin`
- `huobipro`, `ftx`, `coinbase`, `coinbaseinternational`
- `cryptodotcom`, `dydxv4`, `hyperliquid`, `bullish`
- `bit`, `btcex`, `crosstower`, `mock`

**Example**:
```bash
GET /futures/v1/markets
# Returns: Full list of 22 futures exchanges
```

---

#### Markets Instruments
**Path**: `/futures/v1/markets/instruments`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name (e.g., `binance`)

**Response Structure**:
```json
{
  "Data": {
    "binance": {
      "BTCUSDT": {...},
      "ETHUSDT": {...}
    }
  }
}
```

**Example**:
```bash
GET /futures/v1/markets/instruments?market=binance
# Returns: All futures contracts on Binance
```

---

#### Latest Tick
**Path**: `/futures/v1/latest/tick`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instruments` (required): Comma-separated contracts

**Example**:
```bash
GET /futures/v1/latest/tick?market=binance&instruments=BTCUSDT,ETHUSDT
# Returns: Real-time tick data for BTC and ETH futures
```

---

#### Historical Hours
**Path**: `/futures/v1/historical/hours`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instrument` (required): Single contract
- `limit` (optional): Number of records

**Response Fields** (per record):
- `UNIT`, `TIMESTAMP`, `TYPE`, `MARKET`, `INSTRUMENT`, `MAPPED_INSTRUMENT`
- `INDEX_UNDERLYING`, `QUOTE_CURRENCY`, `SETTLEMENT_CURRENCY`, `CONTRACT_CURRENCY`
- `DENOMINATION_TYPE`
- `INDEX_UNDERLYING_ID`, `QUOTE_CURRENCY_ID`, `SETTLEMENT_CURRENCY_ID`, `CONTRACT_CURRENCY_ID`
- `TRANSFORM_FUNCTION`
- `OPEN`, `HIGH`, `LOW`, `CLOSE`
- `FIRST_TRADE_TIMESTAMP`, `LAST_TRADE_TIMESTAMP`
- `FIRST_TRADE_PRICE`, `HIGH_TRADE_PRICE`, `LOW_TRADE_PRICE`, `LAST_TRADE_PRICE`
- `HIGH_TRADE_TIMESTAMP`, `LOW_TRADE_TIMESTAMP`
- `TOTAL_TRADES`, `TOTAL_TRADES_BUY`, `TOTAL_TRADES_SELL`, `TOTAL_TRADES_UNKNOWN`
- `NUMBER_OF_CONTRACTS`
- `VOLUME`, `QUOTE_VOLUME`
- `VOLUME_BUY`, `QUOTE_VOLUME_BUY`, `VOLUME_SELL`, `QUOTE_VOLUME_SELL`
- `VOLUME_UNKNOWN`, `QUOTE_VOLUME_UNKNOWN`

**Example**:
```bash
GET /futures/v1/historical/hours?market=binance&instrument=BTCUSDT&limit=10
# Returns: 10 hourly OHLCV records with extensive trade metrics
```

---

#### Historical Days
**Path**: `/futures/v1/historical/days`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instrument` (required): Single contract
- `limit` (optional): Number of records

**Response**: Same structure as Historical Hours

**Example**:
```bash
GET /futures/v1/historical/days?market=binance&instrument=BTCUSDT&limit=10
# Returns: 10 daily OHLCV records
```

---

## Options API ✅

### ✅ Working Endpoints

#### Markets List
**Path**: `/options/v1/markets`  
**Method**: GET  
**Parameters**: None required

**Supported Markets** (3 options exchanges):
- `binance` — Binance Options
- `deribit` — Deribit (BTC, ETH options leader)
- `okex` — OKX Options

**Example**:
```bash
GET /options/v1/markets
# Returns: 3 options exchanges
```

---

#### Markets Instruments
**Path**: `/options/v1/markets/instruments`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name (e.g., `deribit`)

**Example**:
```bash
GET /options/v1/markets/instruments?market=deribit
# Returns: All options contracts on Deribit
```

---

### ❌ Not Available

#### Options Latest Tick
**Path**: `/options/v1/latest/tick` — ❌ 404  
**Error**: Instrument not found or not integrated yet

---

## ❌ Perpetuals API

### Not Available

#### Perpetuals Latest Tick
**Path**: `/perpetuals/v1/latest/tick` — ❌ 404  
**Note**: Path does not exist; perpetuals may be under futures endpoints

---

## Testing Results

**Date**: January 2, 2026  
**Status**: 7/9 endpoints working ✅

| Endpoint | Status | Notes |
|----------|--------|-------|
| **Futures** | | |
| Futures Markets | ✅ 200 | 22 exchanges supported |
| Futures Instruments | ✅ 200 | Full contract listings |
| Futures Latest Tick | ✅ 200 | Real-time data |
| Futures Historical Hours | ✅ 200 | 10 hourly records with detailed metrics |
| Futures Historical Days | ✅ 200 | 10 daily records |
| **Options** | | |
| Options Markets | ✅ 200 | 3 exchanges (Binance, Deribit, OKX) |
| Options Instruments | ✅ 200 | Contract listings |
| Options Latest Tick | ❌ 404 | Instrument not found/integrated |
| **Perpetuals** | | |
| Perpetuals Latest Tick | ❌ 404 | Path does not exist |

---

## Futures Markets (22 exchanges)

**Tier 1 (Major)**:
- Binance, Bybit, OKX, Deribit

**Tier 2 (Established)**:
- BitMEX, Bitfinex, Bitget, Gate.io, KuCoin
- Kraken, Huobi Pro

**Tier 3 (Regional/Specialized)**:
- Coinbase, Coinbase International
- Crypto.com, dYdX v4, Hyperliquid
- FTX (historical), Bullish

**Other**:
- Bit, BTC.EX, CrossTower, Mock

---

## Options Markets (3 exchanges)

- **Deribit** — Leading BTC/ETH options platform
- **Binance** — Binance Options
- **OKX** — OKX Options

---

## Key Features

### Futures Data
- **22 exchanges**: Comprehensive futures coverage
- **Contract metadata**: Settlement currency, denomination type
- **Trade breakdown**: Buy/sell/unknown volumes
- **Contract metrics**: Number of contracts traded
- **Index tracking**: Underlying index and currencies
- **Multiple timeframes**: Hour and day (check for minute endpoint)

### Options Data
- **3 major platforms**: Deribit, Binance, OKX
- **Contract listings**: Available via instruments endpoint
- **Limited tick data**: Not all instruments integrated yet

---

## Data Richness

Futures endpoints provide extensive metadata compared to spot:

**Additional Fields**:
- `INDEX_UNDERLYING` — Underlying index (e.g., BTC)
- `SETTLEMENT_CURRENCY` — Settlement asset
- `CONTRACT_CURRENCY` — Contract denomination
- `DENOMINATION_TYPE` — Linear vs inverse contracts
- `NUMBER_OF_CONTRACTS` — Contract count traded

**Same as Spot**:
- Full OHLCV with buy/sell breakdown
- Trade timestamps and prices
- Volume metrics in multiple currencies

---

## Notes

- **Perpetuals**: Not a separate endpoint; likely included in futures
- **Options tick data**: Limited integration; use instruments endpoint to check availability
- **Historical depth**: Both hour and day granularity available
- **Minute data**: Not tested yet; may be available

---

*Last Updated: January 2, 2026*
