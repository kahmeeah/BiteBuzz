"""Unit tests for the analyze_sentiment function in the ML client."""

from analyze_sentiment import analyze_sentiment


def test_positive_sentiment():
    """Tests a positive sentence is correctly labeled."""
    result = analyze_sentiment("I absolutely loved the food and service!")
    assert result["sentiment"] == "Positive"
    assert result["polarity"] > 0


def test_negative_sentiment():
    """Tests a negative sentence is correctly labeled."""
    result = analyze_sentiment("The food was awful and the waiter was rude.")
    assert result["sentiment"] == "Negative"
    assert result["polarity"] < 0


def test_neutral_sentiment():
    """Tests a neutral sentence is correctly labeled."""
    result = analyze_sentiment("The restaurant is open from 9 to 5.")
    assert result["sentiment"] == "Neutral"
    assert -0.2 <= result["polarity"] <= 0.2
