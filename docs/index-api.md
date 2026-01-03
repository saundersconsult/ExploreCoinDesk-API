# CoinDesk Index API

**Base Path**: `/index/cc/v1/`  
**Market**: `ccix` (CoinDesk Index)  
**Status**: ✅ All endpoints working

## Overview

The CoinDesk Index API provides access to CCIX (CoinDesk Index) data including real-time tick data and historical OHLCV data at various timeframes.

---

## ✅ Working Endpoints

### Latest Tick
**Path**: `/index/cc/v1/latest/tick`  
**Method**: GET  
**Parameters**:
- `market` (required): `ccix`
- `instruments` (required): Comma-separated list (e.g., `BTC-USD,ETH-USD`)

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
GET /index/cc/v1/latest/tick?market=ccix&instruments=BTC-USD,ETH-USD
```

---

### Historical Hours
**Path**: `/index/cc/v1/historical/hours`  
**Method**: GET  
**Parameters**:
- `market` (required): `ccix`
- `instrument` (required): Single instrument (e.g., `BTC-USD`)
- `limit` (optional): Number of records (default: 10)

**Response Fields** (per record):
- `UNIT`, `TIMESTAMP`, `TYPE`, `MARKET`, `INSTRUMENT`
- `OPEN`, `HIGH`, `LOW`, `CLOSE`
- `FIRST_MESSAGE_TIMESTAMP`, `LAST_MESSAGE_TIMESTAMP`
- `FIRST_MESSAGE_VALUE`, `HIGH_MESSAGE_VALUE`, `LOW_MESSAGE_VALUE`, `LAST_MESSAGE_VALUE`
- `HIGH_MESSAGE_TIMESTAMP`, `LOW_MESSAGE_TIMESTAMP`
- `TOTAL_INDEX_UPDATES`
- `VOLUME`, `QUOTE_VOLUME`

**Example**:
```bash
GET /index/cc/v1/historical/hours?market=ccix&instrument=BTC-USD&limit=10
# Returns: 10 hourly OHLCV records
```

---

### Historical Days
**Path**: `/index/cc/v1/historical/days`  
**Method**: GET  
**Parameters**:
- `market` (required): `ccix`
- `instrument` (required): Single instrument (e.g., `BTC-USD`)
- `limit` (optional): Number of records

**Response**: Same structure as Historical Hours

**Example**:
```bash
GET /index/cc/v1/historical/days?market=ccix&instrument=BTC-USD&limit=10
# Returns: 10 daily OHLCV records
```

---

### Historical Minutes
**Path**: `/index/cc/v1/historical/minutes`  
**Method**: GET  
**Parameters**:
- `market` (required): `ccix`
- `instrument` (required): Single instrument (e.g., `BTC-USD`)
- `limit` (optional): Number of records

**Response**: Same structure as Historical Hours

**Example**:
```bash
GET /index/cc/v1/historical/minutes?market=ccix&instrument=BTC-USD&limit=10
# Returns: 10 minute OHLCV records
```

---

### Markets/Instruments
**Path**: `/index/cc/v1/markets/instruments`  
**Method**: GET  
**Parameters**:
- `market` (required): `ccix`

**Response Structure**:
```json
{
  "Data": {
    "ccix": {
      "INSTRUMENT": {...}
    }
  }
}
```

**Example**:
```bash
GET /index/cc/v1/markets/instruments?market=ccix
# Returns: Available instruments for CCIX market
```

---

## Testing Results

**Date**: January 2, 2026  
**Status**: 5/5 endpoints working ✅

| Endpoint | Status | Notes |
|----------|--------|-------|
| Latest Tick | ✅ 200 | Real-time index data for multiple instruments |
| Historical Hours | ✅ 200 | 10 hourly records returned |
| Historical Days | ✅ 200 | 10 daily records returned |
| Historical Minutes | ✅ 200 | 10 minute records returned |
| Markets/Instruments | ✅ 200 | Full instrument list for CCIX |

---

## Notes

- **Parameter naming**: Historical endpoints use `instrument` (singular), while latest tick uses `instruments` (plural)
- **CCSEQ**: All data includes CoinDesk Sequence numbers for reliable ordering
- **Timeframes**: Minute, hour, and day granularity available
- **Data depth**: Extensive historical coverage with OHLCV+ metadata

---

*Last Updated: January 2, 2026*
