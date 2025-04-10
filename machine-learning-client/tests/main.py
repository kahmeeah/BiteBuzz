from helpers.analyze_sentiment import analyze_sentiment
from helpers.detect_category_map import detect_category_map
from helpers.generate_suggestion import generate_suggestion

def process_review (review: str):
    sentiment_data = analyze_sentiment(review)
    sentiment = sentiment_data["sentiment"]
    categories = detect_category_map(review)

    suggestions = []
    if sentiment == "Negative":
        for category in categories:
            suggestion = generate_suggestion(review, sentiment, category)
            if suggestion:
                suggestions.append((category, suggestion))
    
    return {
        "sentiment": sentiment,
        "categories": categories,
        "suggestions": suggestions
    }
