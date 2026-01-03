# Exchanges with Order Book Data

**Endpoint**: `/data/ob/exchanges`  
**Category**: OrderBook  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Orderbook/exchangesWithOrdebookStaticInfoEndpointV2](https://developers.coindesk.com/documentation/legacy/Orderbook/exchangesWithOrdebookStaticInfoEndpointV2)

## Description

List exchanges that have order book data available

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
curl -X GET "https://min-api.cryptocompare.com/data/ob/exchanges"
```

### Python

```python
import requests

# Endpoint: /data/ob/exchanges
url = "https://min-api.cryptocompare.com/data/ob/exchanges"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/ob/exchanges
const url = "https://min-api.cryptocompare.com/data/ob/exchanges";

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

**Average Response Time**: 680.88ms  
**Min Response Time**: 680.88ms  
**Max Response Time**: 680.88ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 680.88ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
