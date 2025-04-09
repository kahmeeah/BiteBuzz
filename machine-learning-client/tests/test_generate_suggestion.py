"""Unit tests for the generate_suggestion function in the ML client."""

from generate_suggestion import generate_suggestion


def test_generate_suggestion_food():
    """Tests if a negative sentence is corrects appropriate suggestion."""
    review = "The food was cold and bland."
    sentiment = "Negative"
    suggestion = generate_suggestion(review, sentiment)
    assert suggestion == "Try improving food quality or consistency."
