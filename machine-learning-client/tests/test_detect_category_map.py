"""Unit tests for the detect_category_map function in the ML client."""

from helpers.detect_category_map import detect_category_map


def test_one_word():
    """Tests one word."""
    review = "Delicious"
    assert detect_category_map(review) == ["Food"]


def test_two_words_same_category():
    """Tests two words."""
    review = "Fresh taste"
    assert detect_category_map(review) == ["Food"]


def test_two_words_different_categories():
    """Tests different categories."""
    review = "Expensive meal"
    result = detect_category_map(review)
    assert set(result) == {"Food", "Price"}


def test_multiple_categories():
    """Tests different categories."""
    review = "The food was cold, the service was slow, and the place was dirty."
    result = detect_category_map(review)
    expected = {"Food", "Service", "Cleanliness", "Environment", "Time"}
    assert set(result) == expected


def test_general():
    """Tests no comments"""
    review = "No comments."
    assert detect_category_map(review) == ["General"]
