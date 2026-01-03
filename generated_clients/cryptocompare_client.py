"""
CryptoCompare MinAPI Python Client
Auto-generated from deep discovery results
"""

import requests
from typing import Optional, Dict, List, Union
from datetime import datetime
import time


class RateLimiter:
    """Simple rate limiter to respect API limits."""
    
    def __init__(self, calls_per_second: float = 2.0):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0
    
    def wait(self):
        """Wait if necessary to respect rate limit."""
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()


class CryptoCompareClient:
    """
    CryptoCompare MinAPI Client
    
    Full-featured Python client for the CryptoCompare MinAPI.
    Auto-generated from comprehensive endpoint discovery.
    """
    
    BASE_URL = "https://min-api.cryptocompare.com"
    
    def __init__(self, api_key: Optional[str] = None, rate_limit: float = 2.0):
        """
        Initialize the client.
        
        Args:
            api_key: Optional API key for authenticated requests
            rate_limit: Maximum calls per second (default: 2.0)
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.rate_limiter = RateLimiter(rate_limit)
        
        if api_key:
            self.session.headers.update({"x-api-key": api_key})
    
    def _request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make API request with rate limiting and error handling.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            API response as dictionary
            
        Raises:
            requests.HTTPError: On HTTP errors
        """
        self.rate_limiter.wait()
        
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    # ========== Price Endpoints ==========
    
    def get_price(
        self,
        fsym: str,
        tsyms: Union[str, List[str]],
        exchange: Optional[str] = None,
        try_conversion: bool = True,
        relaxed_validation: bool = True
    ) -> Dict:
        """
        Get current price of cryptocurrency.
        
        Args:
            fsym: From symbol (e.g., 'BTC')
            tsyms: To symbols (e.g., 'USD' or ['USD', 'EUR'])
            exchange: Specific exchange (default: CCCAGG)
            try_conversion: Try conversion if no direct pair
            relaxed_validation: Filter non-trading pairs
            
        Returns:
            Dictionary with prices
            
        Example:
            >>> client.get_price('BTC', 'USD')
            {'USD': 42000.0}
        """
        if isinstance(tsyms, list):
            tsyms = ','.join(tsyms)
        
        params = {
            'fsym': fsym,
            'tsyms': tsyms,
            'tryConversion': str(try_conversion).lower(),
            'relaxedValidation': str(relaxed_validation).lower()
        }
        
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/price', params)
    
    def get_price_multi(
        self,
        fsyms: Union[str, List[str]],
        tsyms: Union[str, List[str]],
        exchange: Optional[str] = None
    ) -> Dict:
        """
        Get prices for multiple cryptocurrencies.
        
        Args:
            fsyms: From symbols (e.g., ['BTC', 'ETH'])
            tsyms: To symbols (e.g., ['USD', 'EUR'])
            exchange: Specific exchange (optional)
            
        Returns:
            Dictionary with nested prices
            
        Example:
            >>> client.get_price_multi(['BTC', 'ETH'], 'USD')
            {'BTC': {'USD': 42000.0}, 'ETH': {'USD': 2500.0}}
        """
        if isinstance(fsyms, list):
            fsyms = ','.join(fsyms)
        if isinstance(tsyms, list):
            tsyms = ','.join(tsyms)
        
        params = {'fsyms': fsyms, 'tsyms': tsyms}
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/pricemulti', params)
    
    def get_price_multi_full(
        self,
        fsyms: Union[str, List[str]],
        tsyms: Union[str, List[str]],
        exchange: Optional[str] = None,
        try_conversion: bool = True
    ) -> Dict:
        """
        Get detailed price info with market data.
        
        Includes: high, low, volume, market cap, change, etc.
        
        Args:
            fsyms: From symbols
            tsyms: To symbols
            exchange: Specific exchange (optional)
            try_conversion: Try conversion if no direct pair
            
        Returns:
            Dictionary with RAW and DISPLAY data
        """
        if isinstance(fsyms, list):
            fsyms = ','.join(fsyms)
        if isinstance(tsyms, list):
            tsyms = ','.join(tsyms)
        
        params = {
            'fsyms': fsyms,
            'tsyms': tsyms,
            'tryConversion': str(try_conversion).lower()
        }
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/pricemultifull', params)
    
    def get_average_price(
        self,
        fsym: str,
        tsym: str,
        exchange: Optional[str] = None
    ) -> Dict:
        """
        Get weighted average price across exchanges.
        
        Args:
            fsym: From symbol
            tsym: To symbol
            exchange: Specific exchanges to include
            
        Returns:
            Average price data
        """
        params = {'fsym': fsym, 'tsym': tsym}
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/generateAvg', params)
    
    # ========== Historical Data Endpoints ==========
    
    def get_historical_daily(
        self,
        fsym: str,
        tsym: str,
        limit: int = 30,
        aggregate: int = 1,
        to_timestamp: Optional[int] = None,
        exchange: Optional[str] = None
    ) -> Dict:
        """
        Get daily historical OHLCV data.
        
        Args:
            fsym: From symbol
            tsym: To symbol
            limit: Number of data points (max: 2000)
            aggregate: Aggregate data points
            to_timestamp: Unix timestamp to get data up to
            exchange: Specific exchange
            
        Returns:
            Historical OHLCV data
        """
        params = {
            'fsym': fsym,
            'tsym': tsym,
            'limit': limit,
            'aggregate': aggregate
        }
        if to_timestamp:
            params['toTs'] = to_timestamp
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/histoday', params)
    
    def get_historical_hourly(
        self,
        fsym: str,
        tsym: str,
        limit: int = 30,
        aggregate: int = 1,
        to_timestamp: Optional[int] = None,
        exchange: Optional[str] = None
    ) -> Dict:
        """Get hourly historical OHLCV data."""
        params = {
            'fsym': fsym,
            'tsym': tsym,
            'limit': limit,
            'aggregate': aggregate
        }
        if to_timestamp:
            params['toTs'] = to_timestamp
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/histohour', params)
    
    def get_historical_minute(
        self,
        fsym: str,
        tsym: str,
        limit: int = 30,
        aggregate: int = 1,
        to_timestamp: Optional[int] = None,
        exchange: Optional[str] = None
    ) -> Dict:
        """Get minute-level historical OHLCV data."""
        params = {
            'fsym': fsym,
            'tsym': tsym,
            'limit': limit,
            'aggregate': aggregate
        }
        if to_timestamp:
            params['toTs'] = to_timestamp
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/histominute', params)
    
    def get_price_at_time(
        self,
        fsym: str,
        tsyms: Union[str, List[str]],
        timestamp: int,
        exchange: Optional[str] = None
    ) -> Dict:
        """
        Get historical price at specific timestamp.
        
        Args:
            fsym: From symbol
            tsyms: To symbols
            timestamp: Unix timestamp
            exchange: Specific exchange
            
        Returns:
            Historical price data
        """
        if isinstance(tsyms, list):
            tsyms = ','.join(tsyms)
        
        params = {'fsym': fsym, 'tsyms': tsyms, 'ts': timestamp}
        if exchange:
            params['e'] = exchange
        
        return self._request('/data/pricehistorical', params)
    
    # ========== Social & News Endpoints ==========
    
    def get_latest_news(
        self,
        feeds: Optional[str] = None,
        categories: Optional[str] = None,
        lang: str = 'EN'
    ) -> Dict:
        """
        Get latest cryptocurrency news.
        
        Args:
            feeds: Comma-separated news feeds
            categories: Comma-separated categories
            lang: Language code
            
        Returns:
            Latest news articles
        """
        params = {'lang': lang}
        if feeds:
            params['feeds'] = feeds
        if categories:
            params['categories'] = categories
        
        return self._request('/data/v2/news', params)
    
    def get_social_stats(self, coin_id: int) -> Dict:
        """
        Get latest social media stats for a coin.
        
        Args:
            coin_id: CryptoCompare coin ID
            
        Returns:
            Social media statistics
        """
        return self._request('/data/social/coin/latest', {'coinId': coin_id})
    
    # ========== General Info Endpoints ==========
    
    def get_all_exchanges(self) -> Dict:
        """Get list of all exchanges."""
        return self._request('/data/all/exchanges')
    
    def get_all_coins(self) -> Dict:
        """Get list of all coins."""
        return self._request('/data/all/coinlist')
    
    def get_top_by_volume(
        self,
        tsym: str = 'USD',
        limit: int = 10
    ) -> Dict:
        """
        Get top cryptocurrencies by volume.
        
        Args:
            tsym: To symbol for volume calculation
            limit: Number of results
            
        Returns:
            Top coins by volume
        """
        return self._request('/data/top/totalvolumefull', {
            'tsym': tsym,
            'limit': limit
        })
    
    def get_top_by_market_cap(
        self,
        tsym: str = 'USD',
        limit: int = 10
    ) -> Dict:
        """Get top cryptocurrencies by market cap."""
        return self._request('/data/top/mktcapfull', {
            'tsym': tsym,
            'limit': limit
        })


# Example usage
if __name__ == "__main__":
    # Initialize client
    client = CryptoCompareClient()
    
    # Get Bitcoin price
    btc_price = client.get_price('BTC', 'USD')
    print(f"BTC Price: ${btc_price['USD']:,.2f}")
    
    # Get multiple prices
    prices = client.get_price_multi(['BTC', 'ETH'], ['USD', 'EUR'])
    print(f"\nMultiple Prices: {prices}")
    
    # Get historical data
    historical = client.get_historical_daily('BTC', 'USD', limit=7)
    print(f"\nHistorical Data Points: {len(historical.get('Data', []))}")
    
    # Get latest news
    news = client.get_latest_news()
    if news.get('Data'):
        print(f"\nLatest News: {news['Data'][0].get('title', 'N/A')}")
