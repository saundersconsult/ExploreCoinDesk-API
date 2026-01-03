# List of Indices

**Endpoint**: `/data/index/list`  
**Category**: Index  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Index/listOfIndices](https://developers.coindesk.com/documentation/legacy/Index/listOfIndices)

## Description

List of available crypto indices

## Parameters

No parameters required.

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/index/list"
```

### Python

```python
import requests

# Endpoint: /data/index/list
url = "https://min-api.cryptocompare.com/data/index/list"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/index/list
const url = "https://min-api.cryptocompare.com/data/index/list";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Success",
  "Message": "",
  "HasWarning": false,
  "Type": 100,
  "RateLimit": {},
  "Data": {
    "BVIN": {
      "name": "CryptoCompare Bitcoin Volatility Index",
      "description": "",
      "quote_currency": "USD",
      "index_market_name": "CCMVDA_VIX",
      "index_market_underlying_name": "CCMVDA_VIX",
      "day_close_in_seconds": 36000
    },
    "CCBYDOT": {
      "name": "CCData Blockdaemon Polkadot Staking Yield Index",
      "description": "",
      "quote_currency": "DOT",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    },
    "CCBYSOL": {
      "name": "CCData Blockdaemon Solana Staking Yield Index",
      "description": "",
      "quote_currency": "SOL",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    },
    "CCBYADA": {
      "name": "CCData Blockdaemon Cardano Staking Yield Index",
      "description": "",
      "quote_currency": "ADA",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    },
    "CCBYAVAX": {
      "name": "CCData Blockdaemon Avalanche Staking Yield Index",
      "description": "",
      "quote_currency": "AVAX",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    },
    "CCBYATOM": {
      "name": "CCData Blockdaemon Cosmos Staking Yield Index",
      "description": "",
      "quote_currency": "ATOM",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    },
    "CCBYETH": {
      "name": "CCData Blockdaemon Ethereum Staking Yield Index",
      "description": "",
      "quote_currency": "ETH",
      "index_market_name": "CCB_YIELD",
      "index_market_underlying_name": "CCB_YIELD",
      "day_close_in_seconds": 57600
    }
  }
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

**Data object keys**: `BVIN`, `CCBYDOT`, `CCBYSOL`, `CCBYADA`, `CCBYAVAX`, `CCBYATOM`, `CCBYETH`

## Performance

**Average Response Time**: 1966.03ms  
**Min Response Time**: 1966.03ms  
**Max Response Time**: 1966.03ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 1966.03ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
