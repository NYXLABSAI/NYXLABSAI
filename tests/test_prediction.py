import pytest
from app.models.price_predictor import PricePredictor


def test_buy_signal():
    predictor = PricePredictor()
    result = predictor.predict({"volume": 1500000})
    assert result["signal"] == "BUY"


def test_hold_signal():
    predictor = PricePredictor()
    result = predictor.predict({"volume": 500000})
    assert result["signal"] == "HOLD"
