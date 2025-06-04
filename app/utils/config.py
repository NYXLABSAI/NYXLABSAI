import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional but recommended)
load_dotenv()


class Config:
    """
    Central configuration for NYXLABSAI. Reads from environment or defaults.
    """

    # Application settings
    APP_NAME = "NYXLABSAI"
    VERSION = "0.1.0"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    # Twitter / API settings (if later used)
    TWITTER_QUERY = os.getenv("TWITTER_QUERY", "$BTC OR #Bitcoin")
    MAX_TWEETS = int(os.getenv("MAX_TWEETS", 10))

    # Exchange API settings
    DEFAULT_COIN = os.getenv("DEFAULT_COIN", "bitcoin")
    DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "usd")

    # Logging / file output
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_TO_FILE = os.getenv("LOG_TO_FILE", "false").lower() == "true"
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./data")


config = Config()
