# CryptoCompare API Clients

Auto-generated API clients from comprehensive endpoint discovery.

## Python Client

```python
from cryptocompare_client import CryptoCompareClient

client = CryptoCompareClient(api_key="your_key")

# Get price
price = client.get_price('BTC', 'USD')
print(f"BTC: ${price['USD']}")

# Get historical data
data = client.get_historical_daily('BTC', 'USD', limit=7)

# Get news
news = client.get_latest_news()
```

## TypeScript Client

```typescript
import { CryptoCompareClient } from './cryptocompare_client';

const client = new CryptoCompareClient('your_key');

// Get price
const price = await client.getPrice('BTC', 'USD');
console.log(`BTC: $${price.USD}`);

// Get historical data
const data = await client.getHistoricalDaily('BTC', 'USD', { limit: 7 });

// Get news
const news = await client.getLatestNews();
```

## Features

- ✅ Type-safe method signatures
- ✅ Automatic rate limiting
- ✅ Full parameter validation
- ✅ Comprehensive error handling
- ✅ Complete documentation
- ✅ Based on real API testing

