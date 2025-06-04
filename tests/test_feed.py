import pytest
from app.pipelines.crypto_feed import fetch_latest_prices
from app.pipelines.transform import normalize_price_data


def test_fetch_latest_prices():
    data = fetch_latest_prices()
    assert "symbol" in data
    assert "price" in data
    assert "volume" in data


def test_normalize_price_data():
    raw = {
        "symbol": "BTCUSDT",
        "price": 30000.25,
        "volume": 1500000,
        "timestamp": "2025-06-04T09:00:00Z"
    }

    cleaned = normalize_price_data(raw)
    assert cleaned["price_usd"] == 30000.25
    assert cleaned["volume_24h"] == 1500000
