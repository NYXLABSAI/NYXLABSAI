def normalize_price_data(raw_data: dict) -> dict:
    """
    Converts raw crypto data into a normalized structure for ML models.
    """
    return {
        "symbol": raw_data.get("symbol"),
        "price_usd": float(raw_data.get("price", 0)),
        "volume_24h": int(raw_data.get("volume", 0)),
        "timestamp": raw_data.get("timestamp")
    }


def encode_sentiment(sentiment: str) -> int:
    """
    Encode sentiment labels into numerical form for models.
    """
    mapping = {"positive": 1, "neutral": 0, "negative": -1}
    return mapping.get(sentiment.lower(), 0)
