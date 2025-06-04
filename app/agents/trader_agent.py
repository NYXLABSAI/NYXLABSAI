from app.models.price_predictor import PricePredictor
from app.pipelines.crypto_feed import fetch_latest_prices
from app.utils.logger import log

class TraderAgent:
    def __init__(self):
        self.model = PricePredictor()

    def run(self):
        data = fetch_latest_prices()
        prediction = self.model.predict(data)
        log(f"[NYXLABSAI] Prediction: {prediction}")
