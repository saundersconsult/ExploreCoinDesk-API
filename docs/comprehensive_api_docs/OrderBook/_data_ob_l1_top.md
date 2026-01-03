# Order Book Level 1 Top

**Endpoint**: `/data/ob/l1/top`  
**Category**: OrderBook  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Orderbook/obL1TopEndpoint](https://developers.coindesk.com/documentation/legacy/Orderbook/obL1TopEndpoint)

## Description

Order book level 1 (top of book) data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `e` | string | TBD | TBD |
| `fsym` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/ob/l1/top"
```

### Python

```python
import requests

# Endpoint: /data/ob/l1/top
url = "https://min-api.cryptocompare.com/data/ob/l1/top"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/ob/l1/top
const url = "https://min-api.cryptocompare.com/data/ob/l1/top";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "You need a valid auth key or api key to access this endpoint",
  "HasWarning": false,
  "Type": 1,
  "RateLimit": {},
  "Data": {}
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

**Data object keys**: 

## Performance

**Average Response Time**: 673.77ms  
**Min Response Time**: 673.77ms  
**Max Response Time**: 673.77ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 673.77ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
