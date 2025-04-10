"""Unit tests for the process_review function in main.py"""

from main import process_review


def test_process_positive_review():
    """Test that positive reviews return correct sentiment and no suggestions."""
    review = "The food was amazing and the staff was very friendly!"
    result = process_review(review)

    assert result["sentiment"] == "Positive"
    assert "Food" in result["categories"] or "Service" in result["categories"]
    assert not result["suggestions"]


def test_process_negative_review_with_suggestions():
    """Test that negative reviews return suggestions per category."""
    review = "The food was cold and the service was terrible."
    result = process_review(review)

    assert result["sentiment"] == "Negative"
    assert "Food" in result["categories"]
    assert "Service" in result["categories"]
    assert any(
        s["category"] in ["Food", "Service"]
        for s in result["suggestions"]
    )


def test_process_neutral_review():
    """Test that neutral reviews return no suggestions."""
    review = "The restaurant is located in the city center."
    result = process_review(review)

    assert result["sentiment"] == "Neutral"
    assert isinstance(result["categories"], list)
    assert not result["suggestions"]
