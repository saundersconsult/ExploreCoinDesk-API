# CoinDesk Spot Market API

**Base Path**: `/spot/v1/`  
**Status**: ✅ 5/6 endpoints working

## Overview

The Spot Market API provides access to spot trading data from hundreds of exchanges including Coinbase, Binance, Kraken, and many more. Includes real-time tick data and historical OHLCV data.

---

## ✅ Working Endpoints

### Markets List
**Path**: `/spot/v1/markets`  
**Method**: GET  
**Parameters**: None required

**Response**: Dictionary of all available spot markets

**Supported Markets** (170+ exchanges):
- Major: `coinbase`, `binance`, `kraken`, `gemini`, `bitstamp`, `bitfinex`
- Regional: `coinbaseinternational`, `binanceusa`, `binanceus`
- DeFi: `uniswap`, `pancakeswap`
- Asian: `huobipro`, `okex`, `bybit`, `gateio`, `kucoin`
- European: `bitvavo`, `bitpanda`, `kraken`
- ...and 160+ more

**Example**:
```bash
GET /spot/v1/markets
# Returns: Full list of supported exchanges
```

---

### Markets Instruments
**Path**: `/spot/v1/markets/instruments`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name (e.g., `coinbase`)
- `instruments` (optional): Filter by specific instruments

**Response Structure**:
```json
{
  "Data": {
    "coinbase": {
      "BTC-USD": {...},
      "ETH-USD": {...}
    }
  }
}
```

**Example**:
```bash
GET /spot/v1/markets/instruments?market=coinbase&instruments=BTC-USD,ETH-USD
```

---

### Latest Tick
**Path**: `/spot/v1/latest/tick`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instruments` (required): Comma-separated instrument list

**Response Structure**:
```json
{
  "Data": {
    "BTC-USD": {...},
    "ETH-USD": {...}
  }
}
```

**Example**:
```bash
GET /spot/v1/latest/tick?market=coinbase&instruments=BTC-USD,ETH-USD
```

---

### Historical Hours
**Path**: `/spot/v1/historical/hours`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instrument` (required): Single instrument
- `limit` (optional): Number of records

**Response Fields** (per record):
- `UNIT`, `TIMESTAMP`, `TYPE`, `MARKET`, `INSTRUMENT`, `MAPPED_INSTRUMENT`
- `BASE`, `QUOTE`, `BASE_ID`, `QUOTE_ID`, `TRANSFORM_FUNCTION`
- `OPEN`, `HIGH`, `LOW`, `CLOSE`
- `FIRST_TRADE_TIMESTAMP`, `LAST_TRADE_TIMESTAMP`
- `FIRST_TRADE_PRICE`, `HIGH_TRADE_PRICE`, `LOW_TRADE_PRICE`, `LAST_TRADE_PRICE`
- `HIGH_TRADE_TIMESTAMP`, `LOW_TRADE_TIMESTAMP`
- `TOTAL_TRADES`, `TOTAL_TRADES_BUY`, `TOTAL_TRADES_SELL`, `TOTAL_TRADES_UNKNOWN`
- `VOLUME`, `QUOTE_VOLUME`
- `VOLUME_BUY`, `QUOTE_VOLUME_BUY`, `VOLUME_SELL`, `QUOTE_VOLUME_SELL`
- `VOLUME_UNKNOWN`, `QUOTE_VOLUME_UNKNOWN`

**Example**:
```bash
GET /spot/v1/historical/hours?market=coinbase&instrument=BTC-USD&limit=10
# Returns: 10 hourly OHLCV records with detailed trade metrics
```

---

### Historical Days
**Path**: `/spot/v1/historical/days`  
**Method**: GET  
**Parameters**:
- `market` (required): Exchange name
- `instrument` (required): Single instrument
- `limit` (optional): Number of records

**Response**: Same structure as Historical Hours

**Example**:
```bash
GET /spot/v1/historical/days?market=coinbase&instrument=BTC-USD&limit=10
# Returns: 10 daily OHLCV records
```

---

## ❌ Not Available

### Latest Trade
**Path**: `/spot/v1/latest/trade` — ❌ 404 Path does not exist

---

## Testing Results

**Date**: January 2, 2026  
**Market Tested**: Coinbase  
**Instruments Tested**: BTC-USD, ETH-USD  
**Status**: 5/6 endpoints working ✅

| Endpoint | Status | Notes |
|----------|--------|-------|
| Markets List | ✅ 200 | 170+ exchanges supported |
| Markets Instruments | ✅ 200 | Returns instrument metadata |
| Latest Tick | ✅ 200 | Real-time tick data |
| Latest Trade | ❌ 404 | Path does not exist |
| Historical Hours | ✅ 200 | 10 hourly records with detailed trade breakdown |
| Historical Days | ✅ 200 | 10 daily records with detailed trade breakdown |

---

## Supported Exchanges (Sample)

**Americas**:
- Coinbase, Coinbase International
- Gemini
- Kraken
- Bitstamp
- itBit
- Independent Reserve

**Asia**:
- Binance
- Bybit
- OKX (OKEx)
- Huobi Pro
- KuCoin
- Gate.io
- MEXC

**Europe**:
- Bitvavo
- Bitpanda
- Kraken

**DeFi**:
- Uniswap
- PancakeSwap

**Total**: 170+ spot exchanges

---

## Key Features

- **170+ exchanges**: Centralized and decentralized
- **Standardized mapping**: Consistent instrument naming across exchanges
- **Buy/Sell breakdown**: Volume split by trade side
- **Mapped instruments**: Exchange-specific to standardized mapping
- **Trade metrics**: First/last/high/low trade prices and timestamps
- **Multiple timeframes**: Minute, hour, day (check for minute endpoint)

---

*Last Updated: January 2, 2026*
