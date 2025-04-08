from datetime import datetime
import pymongo
from pymongo import MongoClient
from analyze_sentiment import analyze_sentiment
from generate_suggestion import generate_suggestion

# from detect_category import detect_category  When ready
import os
from dotenv import load_dotenv

load_dotenv(override=True)

database_url = os.getenv("MONGO_URI")
client = pymongo.MongoClient(database_url)
db = client[os.getenv("MONGO_DBNAME")]
collection = db["reviews"]


def detect_category(review):  # placeholder for nyjur function
    return "Unknown"


def process_review(review):
    date = datetime.now().strftime("%B %d %I:%M%p")

    sentiment_result = analyze_sentiment(review)
    category = detect_category(review)
    suggestion = generate_suggestion(review, sentiment_result["sentiment"])

    result = {
        "text": review,
        "sentiment": sentiment_result["sentiment"],
        "polarity": sentiment_result["polarity"],
        "subjectivity": sentiment_result["subjectivity"],
        "category": category,
        "suggestion": suggestion,
        "date": date,
        "processed": True,
    }

    collection.insert_one(result)
    return result
