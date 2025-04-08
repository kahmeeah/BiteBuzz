import pytest
from generate_suggestion import generate_suggestion

def test_generate_suggestion_food():
    review = "The food was cold and bland."
    sentiment = "Negative"
    suggestion = generate_suggestion(review, sentiment)
    assert suggestion == "Try improving food quality or consistency."
