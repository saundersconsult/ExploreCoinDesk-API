# Latest News Articles

**Endpoint**: `/data/v2/news`  
**Category**: News  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/News/latestNewsArticlesEndpoint](https://developers.coindesk.com/documentation/legacy/News/latestNewsArticlesEndpoint)

## Description

Get latest cryptocurrency news articles

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `lang` | string | TBD | TBD |
| `sortOrder` | string | TBD | TBD |
| `limit` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/v2/news"
```

### Python

```python
import requests

# Endpoint: /data/v2/news
url = "https://min-api.cryptocompare.com/data/v2/news"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/v2/news
const url = "https://min-api.cryptocompare.com/data/v2/news";

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

**Average Response Time**: 1625.01ms  
**Min Response Time**: 1625.01ms  
**Max Response Time**: 1625.01ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 1625.01ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
