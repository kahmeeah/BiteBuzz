"""Module for generating improvement suggestions based on user review keywords."""

from .category_map import CATEGORY_KEYWORDS


def generate_suggestion(review, sentiment, key_word):
    """
    Generates a suggestion based on the presence of specific keywords in the review text.

    Args:
        review (str): The user-submitted review.
        sentiment (str): The sentiment label (e.g., 'Positive', 'Negative', 'Neutral').
        key_word (str): The category of keywords to check in the review.

    Returns:
        str: A relevant suggestion or a general message if no keywords matched.
    """
    review = review.lower()

    if sentiment == "Positive":
        return "Awesome! Keep doing what you're doing."

    suggestion = "Review customer feedback for more insights."

    for word in CATEGORY_KEYWORDS.get(key_word, []):
        if word.lower() in review:
            match key_word:
                case "Food":
                    suggestion = "Try improving food quality or consistency."
                case "Service":
                    suggestion = "Train staff to enhance customer service."
                case "Price":
                    suggestion = "Consider adjusting pricing to match value."
                case "Environment":
                    suggestion = "Improve the environment of the store."
                case "Time":
                    suggestion = "Reduce wait times by optimizing service flow."
                case "Drinks":
                    suggestion = "Enhance drink variety or presentation."
                case "Location":
                    suggestion = "Improve accessibility or parking options."
                case "Cleanliness":
                    suggestion = "Ensure cleanliness across all areas."
                case _:
                    suggestion = "Check customer feedback for this area."
            break

    return suggestion
