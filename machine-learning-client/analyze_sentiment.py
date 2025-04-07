from textblob import TextBlob

def analyze_sentiment(sentence):
    blob = TextBlob(sentence)
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
        "subjectivity": subjectivity
    }