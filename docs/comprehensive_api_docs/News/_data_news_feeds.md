# List News Feeds

**Endpoint**: `/data/news/feeds`  
**Category**: News  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/News/ListNewsFeedsEndpoint](https://developers.coindesk.com/documentation/legacy/News/ListNewsFeedsEndpoint)

## Description

List available news feed sources

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
curl -X GET "https://min-api.cryptocompare.com/data/news/feeds"
```

### Python

```python
import requests

# Endpoint: /data/news/feeds
url = "https://min-api.cryptocompare.com/data/news/feeds"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/news/feeds
const url = "https://min-api.cryptocompare.com/data/news/feeds";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
[
  {
    "key": "coindesk",
    "name": "CoinDesk",
    "img": "https://resources.cryptocompare.com/news/5/default.png",
    "lang": "EN"
  },
  {
    "key": "coindesk_es",
    "name": "CoinDesk",
    "img": "https://resources.cryptocompare.com/news/105/default.png",
    "lang": "ES"
  },
  {
    "key": "bitcoinmagazine",
    "name": "Bitcoin Magazine",
    "img": "https://images.cryptocompare.com/news/default/bitcoinmagazine.png",
    "lang": "EN"
  }
]
// ... (103 more items)
```

## Response Schema

## Performance

**Average Response Time**: 690.96ms  
**Min Response Time**: 690.96ms  
**Max Response Time**: 690.96ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 690.96ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
