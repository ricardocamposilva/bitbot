import requests

import pandas as pd
import numpy as np

import constants as c


def fetch_stock_data() -> dict:
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': 'BTC',
        'to_currency': 'USD',
        'apikey': c.ALPHAVANTAGE_API_KEY
    }
    
    response = requests.get(c.ALPHAVANTAGE_BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    
    return response.json()


if __name__ == "__main__":
    try:
        data = fetch_stock_data()

        if 'Realtime Currency Exchange Rate' not in data:
            raise Exception("Unexpected response format: 'Realtime Currency Exchange Rate' not found in response")
        
        data = data['Realtime Currency Exchange Rate']
        data = {
            'from_currency': data['1. From_Currency Code'],
            'to_currency': data['3. To_Currency Code'],
            'exchange_rate': data['5. Exchange Rate'],
            'bid_price': data['8. Bid Price'],
            'ask_price': data['9. Ask Price'],
            'last_updated': data['6. Last Refreshed']
        }

        df = pd.DataFrame([data])
        df['last_updated'] = pd.to_datetime(df['last_updated'])

        df.to_csv("btc_exchange_rates.csv", index=False, mode='a', header=False)


    except Exception as e:
        print(f"An error occurred: {e}")

    