class PricePredictor:
    def predict(self, data):
        # Simulated simple logic
        return {"signal": "BUY" if data["volume"] > 1000000 else "HOLD"}
