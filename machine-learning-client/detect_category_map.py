"""Module for detecting review categories based on keyword matching."""

from category_map import CATEGORY_KEYWORDS


def detect_category_map(text):
    """
    Detect categories from the input text using predefined keywords.

    Returns a list of matched categories, or ['General'] if none are found.
    """
    text = text.lower()
    categories_found = []

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                if category not in categories_found:
                    categories_found.append(category)
                break  # only need one match per category

    if not categories_found:
        categories_found.append("General")

    return categories_found
