from detect_category_map import detect_category_map


def test_one_word():
    review = "Delicious"
    assert detect_category_map(review) == ["Food"]


def test_two_words_same_category():
    review = "Fresh taste"
    assert detect_category_map(review) == ["Food"]


def test_two_words_different_categories():
    review = "Expensive meal"
    result = detect_category_map(review)
    assert set(result) == {"Food", "Price"}


def test_multiple_categories():
    review = "The food was cold, the service was slow, and the place was dirty."
    result = detect_category_map(review)
    expected = {"Food", "Service", "Environment", "Time"}
    assert set(result) == expected


def test_general():
    review = "No comments."
    assert detect_category_map(review) == ["General"]
