from textblob import TextBlob

def analyze_sentiment(review):

    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity < -0.2:
        sentiment = "Negative"
    elif polarity > 0.2:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }
if __name__ == "__main__":
    review_text = input("Paste a review: ")
    result = analyze_sentiment(review_text)
    print("\nSentiment Analysis Result:")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")