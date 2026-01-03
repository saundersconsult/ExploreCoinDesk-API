# Daily Historical Minute

**Endpoint**: `/data/dayavg`  
**Category**: Historical  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Historical/DailyHistoMinute](https://developers.coindesk.com/documentation/legacy/Historical/DailyHistoMinute)

## Description

Daily historical minute data aggregation

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |
| `toTs` | string | TBD | TBD |

## Test Results

**Total Tests**: 6  
**Successful**: 6  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/dayavg?fsym=BTC&tsym=USD&limit=10"
```

### Python

```python
import requests

# Endpoint: /data/dayavg
url = "https://min-api.cryptocompare.com/data/dayavg?fsym=BTC&tsym=USD&limit=10"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsym: BTC
# - tsym: USD
# - limit: 10
```

### JavaScript

```javascript
// Endpoint: /data/dayavg
const url = "https://min-api.cryptocompare.com/data/dayavg?fsym=BTC&tsym=USD&limit=10";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "Path does not exist",
  "Type": 0,
  "Data": {}
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `Type`, `Data`

**Data object keys**: 

## Performance

**Average Response Time**: 714.25ms  
**Min Response Time**: 648.85ms  
**Max Response Time**: 884.82ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsym=USD, limit=10 | ✅ Success | 669.86ms |
| 2 | fsym=BTC, tsym=USD, limit=100 | ✅ Success | 648.85ms |
| 3 | fsym=ETH, tsym=USD, limit=30 | ✅ Success | 744.17ms |
| 4 | fsym=BTC, tsym=USD, limit=7, aggregate=1 | ✅ Success | 671.66ms |
| 5 | fsym=BTC, tsym=USD, toTs=1767324913 | ✅ Success | 884.82ms |
| 6 | fsym=BTC, tsym=USD, toTs=1766806513, limit=7 | ✅ Success | 666.17ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
