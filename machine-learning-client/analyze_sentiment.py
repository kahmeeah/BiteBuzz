"""Module for analyzing sentiment from review text using TextBlob."""

from textblob import TextBlob


def analyze_sentiment(review):
    """
    Analyze the sentiment of a given review string using TextBlob.

    Returns:
        dict: A dictionary containing sentiment label, polarity, and subjectivity.
    """
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity < -0.2:
        sentiment = "Negative"
    elif polarity > 0.2:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2),
    }
