"""
CoinDesk API Client
Base client for interacting with the CoinDesk Digital Asset Data REST API
"""
import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional, Dict, Any
from datetime import datetime, timedelta

# Default API key (fallback if not in env or CLI)
DEFAULT_API_KEY = "f48c49c7984e050797df6039d58c07826a144e39db3121c285ba405b7b5b4023"


class RateLimiter:
    """
    Rate limiter that tracks API calls locally to avoid polling rate limit endpoint.
    Polls actual limits once at initialization, then tracks internally.
    """
    
    def __init__(self):
        self.min_interval = 2.0  # Conservative 2 seconds between calls
        self.last_call = 0
        
        # Local tracking of rate limits
        self.limits = {
            "SECOND": {"max": 20, "remaining": 20, "reset_time": None},
            "MINUTE": {"max": 300, "remaining": 300, "reset_time": None},
            "HOUR": {"max": 3000, "remaining": 3000, "reset_time": None},
            "DAY": {"max": 7500, "remaining": 7500, "reset_time": None},
            "MONTH": {"max": 11000, "remaining": 11000, "reset_time": None}
        }
        
        self.initialized = False
        self.last_poll_time = None
    
    def initialize_from_api(self, rate_limit_data: Dict[str, Any]):
        """
        Initialize rate limits from API response.
        Only called once at client initialization.
        
        Args:
            rate_limit_data: Response from /admin/v2/rate/limit endpoint
        """
        if not rate_limit_data or "Data" not in rate_limit_data:
            print("⚠️  Warning: Could not fetch rate limits, using defaults")
            return
        
        api_key_data = rate_limit_data["Data"].get("API_KEY", {})
        max_limits = api_key_data.get("MAX", {})
        remaining = api_key_data.get("REMAINING", {})
        
        # Update our tracked limits
        for window in ["SECOND", "MINUTE", "HOUR", "DAY", "MONTH"]:
            if window in max_limits:
                self.limits[window]["max"] = max_limits[window]
            if window in remaining:
                self.limits[window]["remaining"] = remaining[window]
            
            # Set reset times
            now = datetime.now()
            if window == "SECOND":
                self.limits[window]["reset_time"] = now + timedelta(seconds=1)
            elif window == "MINUTE":
                self.limits[window]["reset_time"] = now + timedelta(minutes=1)
            elif window == "HOUR":
                self.limits[window]["reset_time"] = now + timedelta(hours=1)
            elif window == "DAY":
                self.limits[window]["reset_time"] = now + timedelta(days=1)
            elif window == "MONTH":
                self.limits[window]["reset_time"] = now + timedelta(days=31)
        
        self.initialized = True
        self.last_poll_time = datetime.now()
        print(f"✅ Rate limits initialized: {remaining.get('MONTH', 0)}/{max_limits.get('MONTH', 0)} monthly calls remaining")
    
    def decrement_counters(self):
        """
        Decrement all rate limit counters after making an API call.
        This tracks usage locally without polling the API.
        """
        now = datetime.now()
        
        for window in ["SECOND", "MINUTE", "HOUR", "DAY", "MONTH"]:
            # Reset counter if the time window has passed
            if self.limits[window]["reset_time"] and now >= self.limits[window]["reset_time"]:
                self.limits[window]["remaining"] = self.limits[window]["max"]
                
                # Update reset time
                if window == "SECOND":
                    self.limits[window]["reset_time"] = now + timedelta(seconds=1)
                elif window == "MINUTE":
                    self.limits[window]["reset_time"] = now + timedelta(minutes=1)
                elif window == "HOUR":
                    self.limits[window]["reset_time"] = now + timedelta(hours=1)
                elif window == "DAY":
                    self.limits[window]["reset_time"] = now + timedelta(days=1)
                elif window == "MONTH":
                    self.limits[window]["reset_time"] = now + timedelta(days=31)
            
            # Decrement counter
            if self.limits[window]["remaining"] > 0:
                self.limits[window]["remaining"] -= 1
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current tracked rate limit status.
        This does NOT make an API call.
        """
        return {
            "initialized": self.initialized,
            "last_poll": self.last_poll_time.isoformat() if self.last_poll_time else None,
            "limits": {
                window: {
                    "max": data["max"],
                    "remaining": data["remaining"],
                    "reset_time": data["reset_time"].isoformat() if data["reset_time"] else None
                }
                for window, data in self.limits.items()
            }
        }
    
    def check_limit(self) -> bool:
        """
        Check if we have remaining calls in all time windows.
        Returns True if safe to make a call, False otherwise.
        """
        for window, data in self.limits.items():
            if data["remaining"] <= 0:
                print(f"⚠️  Warning: {window} rate limit exhausted (0/{data['max']})")
                return False
        return True
    
    def wait(self):
        """Wait if necessary to respect rate limit"""
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()


class CoinDeskClient:
    """
    Client for CoinDesk API with intelligent rate limiting.
    
    Polls rate limits once at initialization, then tracks API calls locally
    to avoid wasting 50% of API quota on rate limit checks.
    """
    
    def __init__(self, api_key: Optional[str] = None, auto_init_limits: bool = True):
        """
        Initialize CoinDesk API client
        
        Args:
            api_key: API key for authentication. If not provided, will try env var or default
            auto_init_limits: If True, automatically poll rate limits on initialization
        """
        # Load from .env file
        config_dir = Path(__file__).parent.parent / "config"
        env_path = config_dir / "coindesk.env"
        if env_path.exists():
            load_dotenv(env_path)
        
        # Set API key (priority: parameter > env > default)
        self.api_key = api_key or os.getenv("API_KEY_ID") or DEFAULT_API_KEY
        
        # Base URL
        self.base_url = os.getenv("BASE_URL", "https://data-api.coindesk.com")
        
        # Rate limiter with local tracking
        self.rate_limiter = RateLimiter()
        
        # Automatically initialize rate limits from API
        if auto_init_limits:
            self._initialize_rate_limits()
    
    def _initialize_rate_limits(self):
        """
        Poll rate limits once from API and initialize local tracking.
        This is called automatically on client initialization.
        """
        print("🔄 Initializing rate limits from API...")
        response = self._make_request(
            "GET", 
            "/admin/v2/rate/limit",
            use_rate_limit=False,  # Don't wait for this initial call
            track_call=False  # Don't track this as it's the initialization call
        )
        
        if response["status_code"] == 200 and response["data"]:
            self.rate_limiter.initialize_from_api(response["data"])
        else:
            print(f"⚠️  Warning: Could not initialize rate limits (status {response['status_code']})")
    
    def get_rate_limit_status(self) -> Dict[str, Any]:
        """
        Get current tracked rate limit status WITHOUT making an API call.
        This uses locally tracked values.
        
        Returns:
            Rate limit status with remaining calls for each time window
        """
        return self.rate_limiter.get_status()
    
    def refresh_rate_limits(self) -> Dict[str, Any]:
        """
        Manually refresh rate limits from API.
        Use sparingly - this counts as an API call!
        
        Returns:
            Fresh rate limit data from API
        """
        print("🔄 Refreshing rate limits from API (this counts as 1 API call)...")
        response = self.get_rate_limits()
        
        if response["status_code"] == 200 and response["data"]:
            self.rate_limiter.initialize_from_api(response["data"])
        
        return response
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        use_rate_limit: bool = True,
        track_call: bool = True
    ) -> Dict[str, Any]:
        """
        Make API request with local rate limit tracking
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            headers: Additional headers
            use_rate_limit: Whether to apply rate limiting wait
            track_call: Whether to track this call against rate limits
        
        Returns:
            Response data and metadata
        """
        # Check if we have remaining calls
        if track_call and not self.rate_limiter.check_limit():
            return {
                "status_code": 429,
                "error": "Rate limit exhausted (local tracking)",
                "data": None
            }
        
        if use_rate_limit:
            self.rate_limiter.wait()
        
        url = f"{self.base_url}{endpoint}"
        
        # Build headers with API key
        request_headers = {
            "x-api-key": self.api_key,
            "Accept": "application/json"
        }
        if headers:
            request_headers.update(headers)
        
        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                headers=request_headers,
                timeout=30
            )
            
            # Track this API call locally (decrement counters)
            if track_call:
                self.rate_limiter.decrement_counters()
            
            # Extract rate limit headers (still available for reference, but not used for tracking)
            rate_limit_info = {
                "limit": response.headers.get("X-Ratelimit-Limit"),
                "remaining": response.headers.get("X-Ratelimit-Remaining"),
                "remaining_all": response.headers.get("X-Ratelimit-Remaining-All"),
                "reset": response.headers.get("X-Ratelimit-Reset"),
                "reset_all": response.headers.get("X-Ratelimit-Reset-All"),
            }
            
            # Check for deprecation
            is_deprecated = response.headers.get("Deprecation") == "true"
            
            # Add local tracked limits to response
            result = {
                "status_code": response.status_code,
                "url": response.url,
                "headers": dict(response.headers),
                "rate_limit": rate_limit_info,
                "rate_limit_tracked": self.rate_limiter.get_status()["limits"],
                "deprecated": is_deprecated,
                "data": response.json() if response.status_code == 200 else None,
                "error": response.text if response.status_code != 200 else None
            }
            
            return result
        
        except requests.exceptions.RequestException as e:
            return {
                "status_code": 0,
                "url": url,
                "error": str(e),
                "data": None
            }
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """Make GET request"""
        return self._make_request("GET", endpoint, params=params, **kwargs)
    
    def post(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """Make POST request"""
        return self._make_request("POST", endpoint, params=params, **kwargs)
    
    def get_rate_limits(self) -> Dict[str, Any]:
        """
        Get current rate limit status from API.
        
        WARNING: This makes an API call and counts against your quota!
        For local tracking, use get_rate_limit_status() instead.
        
        Returns:
            Rate limit information from API
        """
        return self._make_request(
            "GET",
            "/admin/v2/rate/limit",
            use_rate_limit=False,
            track_call=True  # This counts as an API call
        )
        """
        Get current rate limit status
        
        Returns:
            Rate limit information including remaining calls
        """
        return self.get("/admin/v2/rate/limit")
