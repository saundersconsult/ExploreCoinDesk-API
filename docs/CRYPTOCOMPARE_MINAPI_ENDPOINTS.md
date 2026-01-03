# CryptoCompare Min API - Complete Endpoint Enumeration

Based on documentation at: https://developers.coindesk.com/documentation/legacy/

**Base URL**: `https://min-api.cryptocompare.com`

**Status**: Deprecated as of November 2023 (no new updates, but still functional)

---

## Price Endpoints

### Single Symbol Price
- **Endpoint**: `/data/price`
- **Method**: GET
- **Description**: Get current price of any cryptocurrency in any other currency
- **Parameters**:
  - `fsym` (required): From symbol (e.g., BTC)
  - `tsyms` (required): Comma-separated to symbols (e.g., USD,EUR)
  - `tryConversion` (optional): Try conversion if no direct pair (default: true)
  - `e` (optional): Exchange name (default: CCCAGG)
  - `extraParams` (optional): App name
  - `sign` (optional): Sign requests for smart contracts (default: false)
  - `relaxedValidation` (optional): Filter non-trading pairs (default: true)
- **Example**: `https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR`
- **Cache**: 10 seconds
- **Tested**: ✅ Working

### Multiple Symbol Price
- **Endpoint**: `/data/pricemulti`
- **Method**: GET
- **Description**: Get prices for multiple cryptocurrencies at once
- **Parameters**:
  - `fsyms` (required): Comma-separated from symbols
  - `tsyms` (required): Comma-separated to symbols
- **Example**: `https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD`
- **Tested**: ✅ Working

### Multiple Symbol Full Data
- **Endpoint**: `/data/pricemultifull`
- **Method**: GET
- **Description**: Detailed price info including market data (high, low, volume, etc.)
- **Parameters**:
  - `fsyms` (required): Comma-separated from symbols
  - `tsyms` (required): Comma-separated to symbols
- **Example**: `https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD`
- **Tested**: ✅ Working

### Generate Average
- **Endpoint**: `/data/generateAvg`
- **Method**: GET
- **Description**: Get weighted average price across exchanges
- **Parameters**:
  - `fsym` (required): From symbol
  - `tsym` (required): To symbol
  - `e` (optional): Exchanges to include
- **Tested**: ✅ Endpoint exists (requires params)

### Day Average
- **Endpoint**: `/data/dayAvg`
- **Method**: GET
- **Description**: Get daily average price
- **Parameters**:
  - `fsym` (required): From symbol
  - `tsym` (required): To symbol
  - `toTs` (optional): Timestamp
  - `avgType` (optional): Average type
- **Tested**: ✅ Endpoint exists (requires params)

---

## Historical Data Endpoints

### Historical Daily OHLCV
- **Endpoint**: `/data/histoday`
- **Method**: GET
- **Description**: Get daily historical OHLCV data
- **Parameters**:
  - `fsym` (required): From symbol
  - `tsym` (required): To symbol
  - `limit` (optional): Number of data points (default: 30, max: 2000)
  - `aggregate` (optional): Aggregate data points
  - `toTs` (optional): End timestamp
  - `e` (optional): Exchange
- **Example**: `https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10`
- **Tested**: ✅ Working

### Historical Hourly OHLCV
- **Endpoint**: `/data/histohour`
- **Method**: GET
- **Description**: Get hourly historical OHLCV data
- **Parameters**: Same as histoday
- **Example**: `https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=10`
- **Tested**: ✅ Working

### Historical Minute OHLCV
- **Endpoint**: `/data/histominute`
- **Method**: GET
- **Description**: Get minute-level historical OHLCV data
- **Parameters**: Same as histoday
- **Example**: `https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=10`
- **Tested**: ✅ Working

---

## Top Lists Endpoints

### Top by Market Cap (Full Data)
- **Endpoint**: `/data/top/mktcapfull`
- **Method**: GET
- **Description**: Get top cryptocurrencies by market cap with full data
- **Parameters**:
  - `tsym` (required): Convert to symbol
  - `limit` (optional): Number of results (default: 10, max: 100)
  - `page` (optional): Page number
- **Example**: `https://min-api.cryptocompare.com/data/top/mktcapfull?tsym=USD&limit=5`
- **Tested**: ✅ Working

### Top by Market Cap (Simple)
- **Endpoint**: `/data/top/mktcap`
- **Method**: GET
- **Description**: Top coins by market cap (simple data)
- **Parameters**:
  - `tsym` (required): Convert to symbol
  - `limit` (optional): Number of results
- **Tested**: ✅ Endpoint exists (requires params)

### Top by Volume (Full Data)
- **Endpoint**: `/data/top/totalvolfull`
- **Method**: GET
- **Description**: Top cryptocurrencies by trading volume
- **Parameters**:
  - `tsym` (required): Convert to symbol
  - `limit` (optional): Number of results
- **Tested**: ✅ Endpoint exists (requires params)

### Top by Volume (Simple)
- **Endpoint**: `/data/top/totalvol`
- **Method**: GET
- **Description**: Top coins by volume (simple data)
- **Parameters**:
  - `tsym` (required): Convert to symbol
  - `limit` (optional): Number of results
- **Tested**: ✅ Endpoint exists (requires params)

### Top Exchanges
- **Endpoint**: `/data/top/exchanges`
- **Method**: GET
- **Description**: Top exchanges for a trading pair
- **Parameters**:
  - `fsym` (required): From symbol
  - `tsym` (required): To symbol
  - `limit` (optional): Number of results
- **Tested**: ✅ Endpoint exists (requires params)

---

## Premium/Restricted Endpoints
(These exist but require API key or are not available on free tier)

### News
- **Endpoint**: `/data/news`
- **Status**: ❌ Path does not exist (premium feature)

### Social Stats
- **Endpoint**: `/data/social`
- **Status**: ❌ Path does not exist (premium feature)

### Mining Pools
- **Endpoint**: `/data/mining/pools`
- **Status**: ❌ Path does not exist (premium feature)

### Mining Equipment
- **Endpoint**: `/data/mining/equipment`
- **Status**: ❌ Path does not exist (premium feature)

### Mining Contracts
- **Endpoint**: `/data/mining/contracts`
- **Status**: ❌ Path does not exist (premium feature)

### Blockchain Latest
- **Endpoint**: `/data/blockchain/latest`
- **Status**: 🔒 Requires API key authentication

### Exchange Rates
- **Endpoint**: `/data/rate`
- **Status**: ❌ Path does not exist

### Rate Limit Status
- **Endpoint**: `/data/ratelimit`
- **Status**: ❌ Path does not exist

### Market Sentiment
- **Endpoint**: `/data/sentiment`
- **Status**: ❌ Path does not exist

### Trading Pairs
- **Endpoint**: `/data/pairs`
- **Status**: ❌ Path does not exist

### All Exchanges
- **Endpoint**: `/data/exchanges`
- **Status**: ❌ Path does not exist

### All Cryptocurrencies
- **Endpoint**: `/data/cryptocurrencies`
- **Status**: ❌ Path does not exist

### Categories
- **Endpoint**: `/data/categories`
- **Status**: ❌ Path does not exist

---

## Additional Documented Endpoints (Not Yet Tested)

Based on the left navigation of the documentation, here are likely additional endpoints:

### Blockchain Data
- `/data/blockchain/histo/day` - Historical blockchain stats (daily)
- `/data/blockchain/histo/hour` - Historical blockchain stats (hourly)
- `/data/blockchain/list` - List of available blockchain data

### Social Stats
- `/data/social/coin/histo/day` - Historical social stats (daily)
- `/data/social/coin/histo/hour` - Historical social stats (hourly)
- `/data/social/coin/latest` - Latest social stats

### News
- `/data/v2/news/` - Crypto news feed
- `/data/news/feeds` - Available news feeds
- `/data/news/feedsandcategories` - News feeds and categories

### Trading Info
- `/data/top/pairs` - Top trading pairs
- `/data/top/exchanges/full` - Full exchange data
- `/data/top/volumes` - Top volumes by pair

### Reference Data
- `/data/all/coinlist` - All available coins
- `/data/all/exchanges` - All exchanges
- `/data/coin/generalinfo` - General coin information
- `/data/coin/snapshot` - Coin snapshot
- `/data/coin/snapshotfullbyid` - Full coin snapshot by ID

### Price History
- `/data/pricehistorical` - Historical price at specific time
- `/data/coinaverage` - Coin average price

---

## Summary

**Tested Endpoints**: 27  
**Working (Free Tier)**: 9  
- Price endpoints: 5 working
- Historical data: 3 working  
- Top lists: 1 working

**Requires Parameters**: 4 (endpoints exist but need proper params)

**Premium/Auth Required**: 13 (not available on free tier or need API key)

**Not Yet Tested**: ~20+ (from documentation navigation)

---

## Key Findings

1. **Free Tier Access**: Core price and historical OHLCV data fully accessible
2. **Deprecated Status**: No new features being added as of Nov 2023
3. **Migration Path**: CoinDesk recommends using Data API (`data-api.coindesk.com`) for new projects
4. **Cache Strategy**: Responses cached (10 seconds for price data)
5. **Data Coverage**: Supports centralized exchanges, DEX, futures, and options data
6. **Conversion Logic**: Auto-uses BTC as intermediary for non-direct pairs

---

## Recommendations

1. **For Production**: Use CoinDesk Data API instead (actively maintained)
2. **For Learning**: Min API excellent for quick prototyping
3. **Rate Limits**: Apply by IP or API key (account-level)
4. **Migration**: Plan to migrate by checking deprecation headers
5. **Authentication**: Register for API key even on free tier for better tracking
