/**
 * CryptoCompare MinAPI TypeScript Client
 * Auto-generated from deep discovery results
 */

interface RequestOptions {
  method?: string;
  headers?: Record<string, string>;
  params?: Record<string, any>;
}

interface PriceResponse {
  [key: string]: number;
}

interface MultiPriceResponse {
  [fsym: string]: {
    [tsym: string]: number;
  };
}

interface HistoricalDataPoint {
  time: number;
  high: number;
  low: number;
  open: number;
  close: number;
  volumefrom: number;
  volumeto: number;
}

interface HistoricalResponse {
  Response: string;
  Type: number;
  Aggregated: boolean;
  Data: HistoricalDataPoint[];
  TimeTo: number;
  TimeFrom: number;
}

export class CryptoCompareClient {
  private baseUrl = 'https://min-api.cryptocompare.com';
  private apiKey?: string;
  private lastRequestTime = 0;
  private minRequestInterval = 500; // 2 requests per second

  constructor(apiKey?: string, requestsPerSecond: number = 2) {
    this.apiKey = apiKey;
    this.minRequestInterval = 1000 / requestsPerSecond;
  }

  private async rateLimit(): Promise<void> {
    const now = Date.now();
    const elapsed = now - this.lastRequestTime;
    
    if (elapsed < this.minRequestInterval) {
      await new Promise(resolve => 
        setTimeout(resolve, this.minRequestInterval - elapsed)
      );
    }
    
    this.lastRequestTime = Date.now();
  }

  private async request<T>(endpoint: string, params?: Record<string, any>): Promise<T> {
    await this.rateLimit();

    const url = new URL(endpoint, this.baseUrl);
    
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          url.searchParams.append(key, String(value));
        }
      });
    }

    const headers: Record<string, string> = {};
    if (this.apiKey) {
      headers['x-api-key'] = this.apiKey;
    }

    const response = await fetch(url.toString(), { headers });
    
    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  // ========== Price Methods ==========

  async getPrice(
    fsym: string,
    tsyms: string | string[],
    exchange?: string
  ): Promise<PriceResponse> {
    const tsymsStr = Array.isArray(tsyms) ? tsyms.join(',') : tsyms;
    
    return this.request('/data/price', {
      fsym,
      tsyms: tsymsStr,
      e: exchange
    });
  }

  async getPriceMulti(
    fsyms: string | string[],
    tsyms: string | string[],
    exchange?: string
  ): Promise<MultiPriceResponse> {
    const fsymsStr = Array.isArray(fsyms) ? fsyms.join(',') : fsyms;
    const tsymsStr = Array.isArray(tsyms) ? tsyms.join(',') : tsyms;
    
    return this.request('/data/pricemulti', {
      fsyms: fsymsStr,
      tsyms: tsymsStr,
      e: exchange
    });
  }

  async getPriceMultiFull(
    fsyms: string | string[],
    tsyms: string | string[],
    exchange?: string
  ): Promise<any> {
    const fsymsStr = Array.isArray(fsyms) ? fsyms.join(',') : fsyms;
    const tsymsStr = Array.isArray(tsyms) ? tsyms.join(',') : tsyms;
    
    return this.request('/data/pricemultifull', {
      fsyms: fsymsStr,
      tsyms: tsymsStr,
      e: exchange
    });
  }

  // ========== Historical Data Methods ==========

  async getHistoricalDaily(
    fsym: string,
    tsym: string,
    options?: {
      limit?: number;
      aggregate?: number;
      toTs?: number;
      exchange?: string;
    }
  ): Promise<HistoricalResponse> {
    return this.request('/data/histoday', {
      fsym,
      tsym,
      limit: options?.limit ?? 30,
      aggregate: options?.aggregate ?? 1,
      toTs: options?.toTs,
      e: options?.exchange
    });
  }

  async getHistoricalHourly(
    fsym: string,
    tsym: string,
    options?: {
      limit?: number;
      aggregate?: number;
      toTs?: number;
      exchange?: string;
    }
  ): Promise<HistoricalResponse> {
    return this.request('/data/histohour', {
      fsym,
      tsym,
      limit: options?.limit ?? 30,
      aggregate: options?.aggregate ?? 1,
      toTs: options?.toTs,
      e: options?.exchange
    });
  }

  async getHistoricalMinute(
    fsym: string,
    tsym: string,
    options?: {
      limit?: number;
      aggregate?: number;
      toTs?: number;
      exchange?: string;
    }
  ): Promise<HistoricalResponse> {
    return this.request('/data/histominute', {
      fsym,
      tsym,
      limit: options?.limit ?? 30,
      aggregate: options?.aggregate ?? 1,
      toTs: options?.toTs,
      e: options?.exchange
    });
  }

  // ========== News & Social Methods ==========

  async getLatestNews(options?: {
    feeds?: string;
    categories?: string;
    lang?: string;
  }): Promise<any> {
    return this.request('/data/v2/news', {
      feeds: options?.feeds,
      categories: options?.categories,
      lang: options?.lang ?? 'EN'
    });
  }

  async getSocialStats(coinId: number): Promise<any> {
    return this.request('/data/social/coin/latest', { coinId });
  }

  // ========== General Info Methods ==========

  async getAllExchanges(): Promise<any> {
    return this.request('/data/all/exchanges');
  }

  async getAllCoins(): Promise<any> {
    return this.request('/data/all/coinlist');
  }

  async getTopByVolume(tsym: string = 'USD', limit: number = 10): Promise<any> {
    return this.request('/data/top/totalvolumefull', { tsym, limit });
  }

  async getTopByMarketCap(tsym: string = 'USD', limit: number = 10): Promise<any> {
    return this.request('/data/top/mktcapfull', { tsym, limit });
  }
}

// Example usage
export async function example() {
  const client = new CryptoCompareClient();
  
  // Get BTC price
  const price = await client.getPrice('BTC', 'USD');
  console.log(`BTC Price: $${price.USD}`);
  
  // Get historical data
  const historical = await client.getHistoricalDaily('BTC', 'USD', { limit: 7 });
  console.log(`Historical data points: ${historical.Data.length}`);
  
  // Get latest news
  const news = await client.getLatestNews();
  console.log(`Latest news count: ${news.Data?.length ?? 0}`);
}
