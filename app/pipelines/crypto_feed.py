import random
from datetime import datetime
from app.utils.logger import log


def fetch_latest_prices() -> dict:
    """
    Simulates fetching the latest crypto data from an exchange.
    You can later replace this with Binance/CoinGecko/FTX APIs.
    """
    data = {
        "symbol": "BTCUSDT",
        "price": round(random.uniform(25000, 31000), 2),
        "volume": random.randint(100000, 2000000),
        "timestamp": datetime.utcnow().isoformat()
    }

    log(f"Fetched price data: {data}")
    return data
