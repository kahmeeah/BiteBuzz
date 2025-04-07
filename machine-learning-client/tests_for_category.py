from detect_category_map import detect_category_map


def test_one_word():
    review = "Delicious"
    print(detect_category_map(review))  #['Food']

def test_two_words_same_category():
    review = "Fresh taste"
    print(detect_category_map(review))  #['Food']

def test_two_words_different_categories():
    review = "Expensive meal"
    print(detect_category_map(review))  #['Food', 'Price']

def test_multiple_categories():
    review = "The food was cold, the service was slow, and the place was dirty."
    print(detect_category_map(review))  #['Food', 'Service', 'Environment', 'Time']

def test_general():
    review = "No comments."
    print(detect_category_map(review))  #['General']

# Run the tests
test_one_word()
test_two_words_same_category()
test_two_words_different_categories()
test_multiple_categories()
test_general()
