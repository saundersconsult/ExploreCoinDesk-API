# Additional Data Endpoints - Exploration Results

## Summary

Explored 60 potential additional endpoints in the CoinDesk API beyond the initial documented categories. Found **2 new working endpoints** for minute-level historical data.

**Date:** January 2, 2026  
**API Calls Used:** 60 (1 init + 31 generic + 29 extended tests)  
**Success Rate:** 3.3% (2 working / 60 tested)

---

## ✅ New Working Endpoints (2)

### Spot Minute Historical ✅
- **Path:** `/spot/v1/historical/minutes`
- **Method:** GET
- **Parameters:**
  - `market` (required): Exchange name (e.g., "coinbase")
  - `instrument` (required): Trading pair (e.g., "BTC-USD")
  - `limit` (optional): Number of records (default: varies)
- **Response:** 10 items with full OHLCV+ data
- **Fields:** Same as hourly/daily (OHLC, volume, trades, buy/sell breakdown)

**Example:**
```python
response = client.get("/spot/v1/historical/minutes", params={
    "market": "coinbase",
    "instrument": "BTC-USD",
    "limit": 10
})
```

### Futures Minute Historical ✅
- **Path:** `/futures/v1/historical/minutes`
- **Method:** GET
- **Parameters:**
  - `market` (required): Exchange name (e.g., "binance")
  - `instrument` (required): Contract name (e.g., "BTCUSDT")
  - `limit` (optional): Number of records
- **Response:** 10 items with full contract OHLCV+ data
- **Fields:** Same as hourly/daily (OHLC, volume, contracts, settlements)

**Example:**
```python
response = client.get("/futures/v1/historical/minutes", params={
    "market": "binance",
    "instrument": "BTCUSDT",
    "limit": 10
})
```

---

## ❌ Not Available (58 endpoints)

### Generic Data Paths (31 tested - all 404)

#### Market Aggregates
- ❌ `/data/v1/overview` - Overall market overview
- ❌ `/data/v1/summary` - Market summary data
- ❌ `/data/v1/stats` - Market statistics
- ❌ `/data/v1/global` - Global market metrics
- ❌ `/data/v1/rankings` - Asset rankings
- ❌ `/data/v1/movers` - Top movers/gainers/losers

#### Trading Data
- ❌ `/data/v1/orderbook/snapshot` - Order book depth
- ❌ `/data/v1/trades` - Recent trades
- ❌ `/data/v1/volume` - Volume across exchanges
- ❌ `/data/v1/liquidity` - Liquidity metrics
- ❌ `/data/v1/spread` - Bid-ask spread data

#### Reference Data
- ❌ `/data/v1/assets` - All available assets
- ❌ `/data/v1/asset/info` - Asset information
- ❌ `/data/v1/exchanges` - All exchanges
- ❌ `/data/v1/exchange/info` - Exchange information
- ❌ `/data/v1/instruments` - All instruments
- ❌ `/data/v1/pairs` - Trading pairs mapping

#### Historical & Analytics
- ❌ `/data/v1/historical/snapshots` - Market snapshots
- ❌ `/data/v1/vwap` - Volume weighted average price
- ❌ `/data/v1/twap` - Time weighted average price
- ❌ `/data/v1/historical/volume` - Historical volume
- ❌ `/data/v1/candles` - OHLCV candles

#### Streaming
- ❌ `/data/v1/websocket/info` - WebSocket connection info
- ❌ `/data/v1/streaming/channels` - Available channels
- ❌ `/data/v1/streaming/subscriptions` - Subscription options

#### Alternative Paths
- ❌ `/v2/markets` - Markets list (v2)
- ❌ `/v2/assets` - Assets list (v2)
- ❌ `/data` - Root data endpoint
- ❌ `/api` - Root API endpoint
- ❌ `/status` - API status
- ❌ `/health` - API health check

### Extended Category Tests (27 tested)

#### Spot API
- ✅ `/spot/v1/historical/minutes` - **WORKING**
- ❌ `/spot/v1/historical/weeks` - Not available
- ❌ `/spot/v1/historical/months` - Not available
- ❌ `/spot/v1/orderbook/snapshot` - Not available
- ❌ `/spot/v1/trades` - Not available
- ❌ `/spot/v1/latest/aggregated` - Not available
- ❌ `/spot/v1/exchange/status` - Not available
- ❌ `/spot/v1/historical/orderbook` - Not available

#### Futures API
- ✅ `/futures/v1/historical/minutes` - **WORKING**
- ❌ `/futures/v1/historical/weeks` - Not available
- ❌ `/futures/v1/funding/rates` - Not available
- ❌ `/futures/v1/openinterest` - Not available
- ❌ `/futures/v1/historical/openinterest` - Not available
- ❌ `/futures/v1/orderbook/snapshot` - Not available
- ❌ `/futures/v1/trades` - Not available
- ❌ `/futures/v1/latest/aggregated` - Not available
- ❌ `/futures/v1/exchange/status` - Not available

#### Index API
- ❌ `/index/cc/v1/latest/all` - Not available
- ❌ `/index/cc/v1/constituents` - Not available
- ❌ `/index/cc/v1/methodology` - Not available

#### Options API
- ❌ `/options/v1/historical/hours` - Not available
- ❌ `/options/v1/greeks` - Not available
- ❌ `/options/v1/volatility` - Not available

#### Perpetuals API
- ❌ `/perpetuals/v1/markets` - Not available
- ❌ `/perpetuals/v1/markets/instruments` - Not available
- ❌ `/perpetuals/v1/historical/hours` - Not available
- ❌ `/perpetuals/v1/funding` - Not available

#### Metadata
- ❌ `/version` - Not available
- ❌ `/info` - Not available

---

## Key Findings

### 1. API Structure
The CoinDesk API uses **category-specific paths**, not generic `/data/v1/` endpoints:
- ✅ Works: `/spot/v1/...`, `/futures/v1/...`, `/index/cc/v1/...`
- ❌ Doesn't work: `/data/v1/...`, `/v2/...`, root paths

### 2. Historical Data Granularity
**Available timeframes:**
- ✅ Minutes (`/historical/minutes`)
- ✅ Hours (`/historical/hours`)
- ✅ Days (`/historical/days`)
- ❌ Weeks (`/historical/weeks`) - Not available
- ❌ Months (`/historical/months`) - Not available

### 3. Missing Features (Plan Limitation or Not Implemented)
- ❌ Order book snapshots
- ❌ Trade-level tick data
- ❌ Funding rates (futures)
- ❌ Open interest data
- ❌ Options Greeks
- ❌ Implied volatility
- ❌ WebSocket documentation endpoints
- ❌ Exchange status endpoints

### 4. Perpetuals
- No separate perpetuals category found
- Perpetuals likely included in futures category
- Test futures endpoints with perpetual contract instruments

---

## Updated Complete Endpoint List

### ✅ Working Endpoints (19 total)

#### Index API (5)
1. `/index/cc/v1/latest/tick` - Latest CCIX prices
2. `/index/cc/v1/historical/minutes` - Minute OHLCV
3. `/index/cc/v1/historical/hours` - Hourly OHLCV
4. `/index/cc/v1/historical/days` - Daily OHLCV
5. `/index/cc/v1/markets/instruments` - Instrument list

#### Spot API (6)
1. `/spot/v1/markets` - 170+ exchange list
2. `/spot/v1/markets/instruments` - Exchange instruments
3. `/spot/v1/latest/tick` - Real-time tick data
4. `/spot/v1/historical/minutes` - **NEW** Minute OHLCV ✨
5. `/spot/v1/historical/hours` - Hourly OHLCV
6. `/spot/v1/historical/days` - Daily OHLCV

#### Futures API (6)
1. `/futures/v1/markets` - 22 exchange list
2. `/futures/v1/markets/instruments` - Contract listings
3. `/futures/v1/latest/tick` - Real-time futures data
4. `/futures/v1/historical/minutes` - **NEW** Minute OHLCV ✨
5. `/futures/v1/historical/hours` - Hourly OHLCV
6. `/futures/v1/historical/days` - Daily OHLCV

#### Options API (2)
1. `/options/v1/markets` - 3 exchange list
2. `/options/v1/markets/instruments` - Contract listings

#### Administrative (1)
1. `/admin/v2/rate/limit` - Rate limit status

---

## Recommendations

### 1. Use Minute Data for High-Frequency Analysis
```python
# Get last 60 minutes of spot data
response = client.get("/spot/v1/historical/minutes", params={
    "market": "coinbase",
    "instrument": "BTC-USD",
    "limit": 60
})

# Get last 60 minutes of futures data
response = client.get("/futures/v1/historical/minutes", params={
    "market": "binance",
    "instrument": "BTCUSDT",
    "limit": 60
})
```

### 2. For Missing Features, Consider:
- **Order book:** Use WebSocket connections (not REST API)
- **Funding rates:** May require official documentation or support contact
- **Open interest:** Check if available via WebSocket or separate endpoint
- **Options Greeks:** May need to calculate client-side from price data

### 3. Perpetuals Data
Test futures endpoints with perpetual contract names:
```python
# Test if perpetuals work through futures API
response = client.get("/futures/v1/latest/tick", params={
    "market": "binance",
    "instrument": "BTCUSDT"  # This is a perpetual
})
```

---

## Data Coverage Summary

| Category | Endpoints | Minute | Hour | Day | Week | Month |
|----------|-----------|--------|------|-----|------|-------|
| Index | 5 | ✅ | ✅ | ✅ | ❌ | ❌ |
| Spot | 6 | ✅ | ✅ | ✅ | ❌ | ❌ |
| Futures | 6 | ✅ | ✅ | ✅ | ❌ | ❌ |
| Options | 2 | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## API Call Efficiency

**Total exploration cost:** 60 API calls  
**New features found:** 2 endpoints (minute-level data)  
**Remaining monthly limit:** 10,928 / 11,000 calls (99.3%)

**Value:** Minute-level historical data adds high-frequency analysis capability, useful for:
- Intraday trading analysis
- Short-term volatility studies
- Detailed price action examination
- Microstructure research

---

## Next Steps

### Immediate
- ✅ Document minute historical endpoints
- ⏳ Test minute data with various exchanges
- ⏳ Verify data quality and completeness
- ⏳ Update integration guide

### Future Research
- ⏳ Contact CoinDesk support for:
  - WebSocket endpoint documentation
  - Funding rates availability
  - Open interest data access
  - Order book REST endpoints
- ⏳ Test perpetual contracts via futures API
- ⏳ Explore CSV export capabilities

---

**Status:** Exploration Complete  
**New Discoveries:** 2 working endpoints (minute-level historical data)  
**Total Known Endpoints:** 19 working / 79 tested (24% success rate)
