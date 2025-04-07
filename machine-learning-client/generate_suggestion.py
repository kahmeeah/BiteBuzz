"""Module for generating improvement suggestions based on user review keywords."""

from category_map import CATEGORY_KEYWORDS


def generate_suggestion(review, sentiment):
    """
    Generates a suggestion based on the presence of specific keywords in the review text.

    Args:
        text (str): The user-submitted review.

    Returns:
        str: A relevant suggestion or general message if no keywords matched.
    """
    review = review.lower()

    if sentiment == "Positive":
        return "Awesome! Keep doing what you're doing."

    suggestions = []

    for word in CATEGORY_KEYWORDS["Food"]:
        if word in review:
            suggestions.append("Try improving food quality or consistency.")
            break

    for word in CATEGORY_KEYWORDS["Service"]:
        if word in review:
            suggestions.append("Focus on better customer service.")
            break

    for word in CATEGORY_KEYWORDS["Cleanliness"]:
        if word in review:
            suggestions.append("Consider improving cleanliness and hygiene.")
            break

    for word in CATEGORY_KEYWORDS["Time"]:
        if word in review:
            suggestions.append("Work on faster service or reducing wait times.")
            break

    for word in CATEGORY_KEYWORDS["Price"]:
        if word in review:
            suggestions.append("Reassess pricing for better value.")
            break

    for word in CATEGORY_KEYWORDS["Environment"]:
        if word in review:
            suggestions.append("Enhance the restaurant’s vibe or atmosphere.")
            break

    for word in CATEGORY_KEYWORDS["Drinks"]:
        if word in review:
            suggestions.append("Improve drink options or quality.")
            break

    for word in CATEGORY_KEYWORDS["Location"]:
        if word in review:
            suggestions.append("Improve location accessibility or parking.")
            break

    if suggestions:
        return " ".join(suggestions)
    return "Review customer feedback for more insights."
