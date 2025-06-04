import requests
from app.utils.logger import log


def get_coin_price(coin_id="bitcoin", vs_currency="usd") -> dict:
    """
    Fetch the current price and 24h volume from CoinGecko.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency,
        "include_24hr_vol": "true",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data[coin_id][vs_currency]
        volume = data[coin_id][f"{vs_currency}_24h_vol"]

        log(f"Fetched {coin_id.upper()} price: ${price} | 24h Vol: {volume}")
        return {
            "symbol": coin_id,
            "price": price,
            "volume": volume
        }

    except Exception as e:
        log(f"Error fetching price: {e}")
        return {}
