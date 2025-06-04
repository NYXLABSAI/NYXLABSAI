import snscrape.modules.twitter as sntwitter
from app.utils.logger import log


def fetch_recent_tweets(query: str, max_tweets: int = 5) -> list[str]:
    """
    Scrape recent tweets matching a query (e.g. $SOL, Bitcoin).
    Returns a list of tweet texts.
    """
    tweets = []
    log(f"Scraping Twitter for query: {query}")
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append(tweet.content)
        log(f"Tweet {i+1}: {tweet.content[:60]}...")

    return tweets
