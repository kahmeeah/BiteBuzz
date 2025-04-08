from datetime import datetime
import pymongo
from pymongo import MongoClient
from analyze_sentiment import analyze_sentiment
from generate_suggestion import generate_suggestion
# from detect_category import detect_category  When ready
import os
from dotenv import load_dotenv

#docker???
load_dotenv(override=True)

database_url = os.getenv("MONGO_URI")
client = pymongo.MongoClient(database_url)
db = client[os.getenv("MONGO_DBNAME")]
collection = db["reviews"]

def process_unprocessed_reviews():

    """
    Fetch unprocessed reviews from MongoDB, analyze them,
    and update the date in place.
    """
    unprocessed_reviews = collection.find({"processed": False})

    for review_doc in unprocessed_reviews:
        review_text = review_doc["text"]
        _id = review_doc["_id"] 

        sentiment_result = analyze_sentiment(review_text)
        category = detect_category(review_text)
        suggestion = generate_suggestion(review_text, sentiment_result["sentiment"])
        date = datetime.now().strftime("%B %d %I:%M%p")

        # Update the  document
        collection.update_one(
            {"_id": _id},
            {"$set": {
                "sentiment": sentiment_result["sentiment"],
                "polarity": sentiment_result["polarity"],
                "subjectivity": sentiment_result["subjectivity"],
                "category": category,
                "suggestion": suggestion,
                "date": date,
                "processed": True
            }}
        )