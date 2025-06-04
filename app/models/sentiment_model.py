import re
import nltk
from textblob import TextBlob
from app.utils.logger import log

# Download necessary NLTK resources once (only if not already installed)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


class SentimentModel:
    """
    A simple sentiment analysis model using TextBlob.
    You can later upgrade this with transformers or fine-tuned models.
    """

    def __init__(self):
        log("SentimentModel loaded using TextBlob backend.")

    def clean_text(self, text: str) -> str:
        """
        Remove URLs, mentions, hashtags, and special characters.
        """
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)
        text = re.sub(r"@\w+|#\w+", "", text)
        text = re.sub(r"[^\w\s]", "", text)
        return text.lower().strip()

    def analyze(self, text: str) -> dict:
        """
        Returns sentiment polarity and label for the input text.
        """
        cleaned = self.clean_text(text)
        blob = TextBlob(cleaned)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            label = "positive"
        elif polarity < -0.1:
            label = "negative"
        else:
            label = "neutral"

        log(f"Sentiment analysis: '{text[:50]}...' → {label.upper()} ({polarity:.2f})")

        return {
            "original": text,
            "cleaned": cleaned,
            "polarity": polarity,
            "label": label
        }
