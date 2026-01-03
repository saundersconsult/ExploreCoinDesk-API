# Multiple Symbols Price

**Endpoint**: `/data/pricemulti`  
**Category**: Price  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsPriceEndpoint](https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsPriceEndpoint)

## Description

Get prices for multiple cryptocurrencies at once

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsyms` | string | TBD | TBD |
| `tsyms` | string | TBD | TBD |
| `e` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD"
```

### Python

```python
import requests

# Endpoint: /data/pricemulti
url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsyms: BTC,ETH
# - tsyms: USD
```

### JavaScript

```javascript
// Endpoint: /data/pricemulti
const url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "BTC": {
    "USD": 90176.22
  },
  "ETH": {
    "USD": 3120.03
  }
}
```

## Response Schema

**Top-level keys**: `BTC`, `ETH`

## Performance

**Average Response Time**: 1034.99ms  
**Min Response Time**: 667.66ms  
**Max Response Time**: 1758.57ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsyms=BTC,ETH, tsyms=USD | ✅ Success | 1758.57ms |
| 2 | fsyms=BTC,ETH,XRP, tsyms=USD,EUR | ✅ Success | 678.74ms |
| 3 | fsyms=BTC, tsyms=USD, e=CCCAGG | ✅ Success | 667.66ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
