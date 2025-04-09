"""Unit tests for the generate_suggestion function in the ML client."""

from helpers.generate_suggestion import generate_suggestion


def test_generate_suggestion_food():
    """Tests if a negative sentence is corrects appropriate suggestion."""
    review = "The food was cold and bland."
    sentiment = "Negative"
    key_word = "Food"
    suggestion = generate_suggestion(review, sentiment, key_word)
    assert suggestion == "Try improving food quality or consistency."
