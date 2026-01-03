# CoinDesk API Integration Guide

## Quick Start

### 1. Get API Key
1. Visit https://developers.coindesk.com/
2. Sign up or log in
3. Navigate to Settings → API Keys
4. Create new API key
5. Copy your API Key ID

### 2. Configure Environment
```bash
# Edit config/coindesk.env
API_KEY_ID=your_api_key_id_here
BASE_URL=https://data-api.coindesk.com
```

### 3. Test Connection
```bash
python scripts/check_rate_limits.py
```

---

## Authentication Methods

CoinDesk supports three authentication approaches:

### Method 1: X-API-Key Header (Recommended)
```python
headers = {
    "x-api-key": "your_api_key_id"
}
response = requests.get(url, headers=headers)
```

### Method 2: Authorization Header
```python
# Bearer token
headers = {
    "Authorization": "Bearer your_api_key_id"
}

# Or API key format
headers = {
    "Authorization": "Apikey your_api_key_id"
}
```

### Method 3: Query Parameter
```python
url = "https://data-api.coindesk.com/endpoint?api_key=your_api_key_id"
```

**Note**: X-API-Key header is recommended for security and clarity.

---

## Rate Limiting

### How It Works
- **Account-level** rate limiting (all API keys share same quota)
- **Call-based** (not credit-based) for simplicity
- **Multiple time windows**: second, minute, hour, day, month
- **Burst capability** for short-term spikes

### Monitoring Rate Limits

Every API response includes rate limit headers:

```python
response = requests.get(url, headers=headers)

# Check remaining calls
remaining = response.headers.get("X-Ratelimit-Remaining")
limit = response.headers.get("X-Ratelimit-Limit")
reset = response.headers.get("X-Ratelimit-Reset")

print(f"Calls remaining: {remaining}/{limit}")
print(f"Resets in: {reset} seconds")
```

### Best Practices
1. **Monitor headers** — Check remaining calls in each response
2. **Implement backoff** — Slow down if approaching limits
3. **Handle 429 errors** — Retry after reset time
4. **Use rate limiter** — Built into `CoinDeskClient`

---

## Using the CoinDeskClient

### Basic Usage
```python
from src.api_client import CoinDeskClient

# Initialize client
client = CoinDeskClient(api_key="your_api_key_id")

# Make request
response = client.get("/admin/v2/rate/limit")

# Access data
print(f"Status: {response['status_code']}")
print(f"Data: {response['data']}")
print(f"Rate Limit: {response['rate_limit']}")
```

### Rate Limit Information
```python
# Get rate limits
rate_info = client.get_rate_limits()

print(f"Remaining calls: {rate_info['rate_limit']['remaining']}")
print(f"Full data: {rate_info['data']}")
```

### Custom Requests
```python
# With parameters
response = client.get("/endpoint/path", params={
    "limit": 100,
    "market": "BTC-USD"
})

# Without rate limiting (use sparingly)
response = client.get("/endpoint", use_rate_limit=False)
```

---

## Error Handling

### Status Codes
- **200** — Success
- **400** — Bad Request (invalid parameters)
- **401** — Unauthorized (invalid API key)
- **403** — Forbidden (plan limitation)
- **404** — Not Found (invalid endpoint)
- **429** — Too Many Requests (rate limit exceeded)
- **500** — Internal Server Error

### Example Error Handling
```python
response = client.get("/endpoint")

if response["status_code"] == 200:
    data = response["data"]
    # Process data
elif response["status_code"] == 429:
    reset_time = response["rate_limit"]["reset"]
    print(f"Rate limit exceeded. Retry in {reset_time}s")
elif response["status_code"] == 403:
    print("Plan limitation - upgrade required")
else:
    print(f"Error: {response['error']}")
```

---

## Deprecation Handling

### Check for Deprecated Endpoints
```python
response = client.get("/some/endpoint")

if response.get("deprecated"):
    print("⚠️  This endpoint is deprecated!")
    print("Check documentation for replacement")
```

### Deprecation Timeline
- Deprecated endpoints continue to work with no changes
- After 6 months: may require API key (if previously IP-limited)
- Documentation moved to "Deprecated" section
- New versions available in current documentation

---

## Data Formats

### JSON (Default)
```python
response = client.get("/endpoint")
data = response["data"]  # Already parsed JSON
```

### CSV (Where Available)
```python
headers = {"Accept": "text/csv"}
response = client.get("/endpoint", headers=headers)
```

---

## CCSEQ System

CoinDesk uses **CCSEQ (CoinDesk Sequence)** for reliable data ordering:

- **Sequential**: Gapless, always-increasing numbers
- **Non-chronological**: Avoids timestamp discrepancies
- **Integrity**: Invalid messages don't increment sequence
- **Reliability**: Out-of-sequence messages integrated without gaps

### Response Structure
```json
{
  "Data": [...],        // Valid messages
  "Invalid": [...],     // Invalid messages (preserved sequence)
  "Err": null,          // Error information
  "Warn": null          // Warning information
}
```

---

## Next Steps

1. ✅ Test rate limit endpoint
2. ⏳ Explore market data endpoints
3. ⏳ Test index/reference price endpoints
4. ⏳ Explore OHLCV+ historical data
5. ⏳ Test news and social endpoints
6. ⏳ Document response formats

---

*Last Updated: January 2, 2026*
