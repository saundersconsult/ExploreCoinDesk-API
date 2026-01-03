# Single Symbol Price

**Endpoint**: `/data/price`  
**Category**: Price  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/](https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/)

## Description

Get current price of any cryptocurrency in any other currency

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsyms` | string | TBD | TBD |
| `tryConversion` | string | TBD | TBD |
| `e` | string | TBD | TBD |
| `extraParams` | string | TBD | TBD |
| `sign` | string | TBD | TBD |
| `relaxedValidation` | string | TBD | TBD |

## Test Results

**Total Tests**: 4  
**Successful**: 4  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
```

### Python

```python
import requests

# Endpoint: /data/price
url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsym: BTC
# - tsyms: USD
```

### JavaScript

```javascript
// Endpoint: /data/price
const url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "USD": 90178.02
}
```

## Response Schema

**Top-level keys**: `USD`

## Performance

**Average Response Time**: 671.10ms  
**Min Response Time**: 665.73ms  
**Max Response Time**: 680.99ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsyms=USD | ✅ Success | 680.99ms |
| 2 | fsym=ETH, tsyms=USD,EUR,GBP | ✅ Success | 666.76ms |
| 3 | fsym=BTC, tsyms=USD, e=Coinbase | ✅ Success | 670.93ms |
| 4 | fsym=BTC, tsyms=USD, e=Binance | ✅ Success | 665.73ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
