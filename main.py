import pandas as pd
import keys
import requests
from time import sleep


def get_crypto_rates(base_currency = "USD", assets ="BTC,ETH,XRP"):
    url = "https://pro-api.coinmarketcap.com"


    payload = {"key" : keys.COIN_MARKET_CAP_API_KEY, "convert":base_currency, "ids" : assets, "interval": "1d"}
    response = requests.get(url, params=payload)
    data =response.json()

    crypto_currency, crypto_price , crypto_timestamp = [], [], []

    

    for asset in data:
        crypto_currency.append(asset[currency])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])

    raw_data = {
        "assets": crypto_currency,
        "rates": crypto_price,
        "timestamp": crypto_timestamp
    }
    df = pd.DataFrame(raw_data)
    print(df)
    return df

get_crypto_rates()

