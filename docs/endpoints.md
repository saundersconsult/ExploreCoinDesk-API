# CoinDesk API Endpoints

**Base URL**: https://data-api.coindesk.com  
**Documentation**: https://developers.coindesk.com/documentation/data-api/introduction

## Administrative Endpoints

### Rate Limits
- **Endpoint**: `/admin/v2/rate/limit`
- **Method**: GET
- **Description**: Get current rate limit status including remaining calls across all time windows
- **Authentication**: Required (x-api-key header)

**Response Headers**:
- `X-Ratelimit-Limit` — Maximum requests per time window
- `X-Ratelimit-Remaining` — Remaining requests in current window
- `X-Ratelimit-Remaining-All` — Remaining across all windows
- `X-Ratelimit-Reset` — Seconds until reset
- `X-Ratelimit-Reset-All` — Reset times for all windows

**Time Windows**:
- Per second (burst capability)
- Per minute
- Per hour
- Per day
- Per month (primary limit)

---

## Data Categories

According to the documentation, CoinDesk API provides:

### 1. **Index & Reference Prices**
- Latest reference prices
- Historical index data
- CCIX (CoinDesk Index) data

### 2. **Market Data**
- Spot markets (centralized & decentralized)
- Futures markets
- Options markets
- Order book snapshots

### 3. **OHLCV+ Data**
- Historical candlestick data
- Volume metrics
- Trade aggregates

### 4. **News & Social Data**
- Real-time crypto news
- Social metrics
- Market sentiment

### 5. **On-Chain Data**
- Blockchain metrics
- DeFi analytics
- Network statistics

### 6. **Instruments & Markets**
- Trading pair listings
- Exchange mappings
- Instrument metadata

---

## Exploration Status

### ✅ Completed
- ✅ **Rate Limit Endpoint** — Tested, 11,000/month confirmed
- ✅ **Index API** — 5/5 endpoints working ([docs](index-api.md))
- ✅ **Spot Market API** — 5/6 endpoints working, 170+ exchanges ([docs](spot-api.md))
- ✅ **Derivatives API** — 7/9 endpoints working, 22 futures + 3 options exchanges ([docs](derivatives-api.md))

### ❌ Not Available (Plan Limitation)
- ❌ **News & Social** — 0/6 endpoints (all 404)
- ❌ **On-Chain Data** — 0/6 endpoints (all 404)

### ⏳ Pending
- ⏳ **Order Book** — Snapshots, depth data
- ⏳ **WebSocket** — Streaming connections
- ⏳ **Funding Rates** — Futures funding rates
- ⏳ **Open Interest** — Futures OI data

---

## Quick Links

- **[Comprehensive Exploration Summary](EXPLORATION_SUMMARY.md)** — Full findings across all tested categories
- **[Index API Documentation](index-api.md)** — CCIX reference prices and historical data
- **[Spot Market API Documentation](spot-api.md)** — 170+ exchange spot trading data
- **[Derivatives API Documentation](derivatives-api.md)** — Futures and options markets (22 + 3 exchanges)
- **[Integration Guide](integration-guide.md)** — Authentication, rate limiting, best practices

---

## Tested Endpoints Summary

### Index API (CCIX) — 5/5 ✅
- `/index/cc/v1/latest/tick` — ✅ Real-time index prices
- `/index/cc/v1/historical/minutes` — ✅ Minute OHLCV
- `/index/cc/v1/historical/hours` — ✅ Hourly OHLCV
- `/index/cc/v1/historical/days` — ✅ Daily OHLCV
- `/index/cc/v1/markets/instruments` — ✅ Instrument list

### Spot Market API — 5/6
- `/spot/v1/markets` — ✅ 170+ exchange list
- `/spot/v1/markets/instruments` — ✅ Exchange instruments
- `/spot/v1/latest/tick` — ✅ Real-time tick data
- `/spot/v1/latest/trade` — ❌ 404 (path does not exist)
- `/spot/v1/historical/hours` — ✅ Hourly OHLCV
- `/spot/v1/historical/days` — ✅ Daily OHLCV

### Futures API — 5/5 ✅
- `/futures/v1/markets` — ✅ 22 futures exchanges
- `/futures/v1/markets/instruments` — ✅ Contract listings
- `/futures/v1/latest/tick` — ✅ Real-time futures data
- `/futures/v1/historical/hours` — ✅ Hourly OHLCV
- `/futures/v1/historical/days` — ✅ Daily OHLCV

### Options API — 2/3
- `/options/v1/markets` — ✅ 3 options exchanges
- `/options/v1/markets/instruments` — ✅ Contract listings
- `/options/v1/latest/tick` — ❌ 404 (instrument not integrated)

### News & Social API — 0/6 ❌
- `/news/v1/latest` — ❌ 404 (path does not exist)
- `/news/v1/category/{category}` — ❌ 404 (path does not exist)
- `/news/v1/asset/{asset}` — ❌ 404 (path does not exist)
- `/social/v1/latest` — ❌ 404 (path does not exist)
- `/social/v1/historical/days` — ❌ 404 (path does not exist)
- `/sentiment/v1/latest` — ❌ 404 (path does not exist)

### On-Chain Data API — 0/6 ❌
- `/onchain/v1/latest` — ❌ 404 (path does not exist)
- `/onchain/v1/historical/days` — ❌ 404 (path does not exist)
- `/onchain/v1/network/stats` — ❌ 404 (path does not exist)
- `/blockchain/v1/latest` — ❌ 404 (path does not exist)
- `/blockchain/v1/historical/days` — ❌ 404 (path does not exist)
- `/defi/v1/tvl/latest` — ❌ 404 (path does not exist)

### Administrative — 1/1 ✅
- `/admin/v2/rate/limit` — ✅ Rate limit status

**Total**: 33 endpoints tested, 17 working ✅ (51.5% success rate)

**By Category**:
- Index: 5/5 (100%)
- Spot: 5/6 (83.3%)
- Futures: 5/5 (100%)
- Options: 2/3 (66.7%)
- News: 0/6 (0% - not available)
- On-Chain: 0/6 (0% - not available)
- Admin: 1/1 (100%)

---

*Last Updated: January 2, 2026*  
*API Calls Used*: 19 of 11,000 monthly limit
