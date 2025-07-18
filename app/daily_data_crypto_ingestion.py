import requests
from datetime import datetime

import pandas as pd
import numpy as np

import constants as c


def fetch_daily_stock_data() -> dict:
    params = {
        'function': 'DIGITAL_CURRENCY_DAILY',
        'symbol': 'BTC',
        'market': 'USD',
        'apikey': c.ALPHAVANTAGE_API_KEY
    }
    
    response = requests.get(c.ALPHAVANTAGE_BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    
    return response.json()


if __name__ == "__main__":
    try:
        data = fetch_daily_stock_data()

        print(data)

        if 'Time Series (Digital Currency Daily)' not in data:
            raise Exception("Unexpected response format: 'Time Series (Digital Currency Daily)' not found in response")
        
        data = data['Time Series (Digital Currency Daily)']

        df = pd.DataFrame.from_dict(data, orient='index')

        df.to_csv(f"btc_daily_exchange_rates_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv", header=True)


    except Exception as e:
        print(f"An error occurred: {e}")

    