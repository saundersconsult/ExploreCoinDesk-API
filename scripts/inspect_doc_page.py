#!/usr/bin/env python3
import requests, re

def main():
    u='https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint/'
    h=requests.get(u,timeout=20).text
    print('len', len(h))
    urls=[x for x in re.findall(r'https?://[^"\s<>]+', h) if 'coindesk' in x.lower() or 'cryptocompare' in x.lower()]
    print('urls count', len(urls))
    print('\n'.join(sorted(urls)))
    scripts=re.findall(r'<script[^>]+src=\"([^\"]+)\"', h)
    print('scripts count', len(scripts))
    print('\n'.join(scripts))

if __name__ == '__main__':
    main()
