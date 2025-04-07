from category_map import CATEGORY_KEYWORDS

def detect_category_map(text):
    text = text.lower()
    categories_found = []

    for category in CATEGORY_KEYWORDS:
        keywords = CATEGORY_KEYWORDS[category]
        for keyword in keywords:
            if keyword in text:
                if category not in categories_found:
                    categories_found.append(category)
                break  # only need one match per category

    if len(categories_found) == 0:
        categories_found.append("General")

    return categories_found

