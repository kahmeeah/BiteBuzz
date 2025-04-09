"""Main module for processing and analyzing customer reviews from MongoDB."""

import os
from datetime import datetime

from dotenv import load_dotenv
import pymongo

from analyze_sentiment import analyze_sentiment
from generate_suggestion import generate_suggestion

# docker???
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
        suggestion = generate_suggestion(review_text, sentiment_result["sentiment"])
        date = datetime.now().strftime("%B %d %I:%M%p")

        # Update the  document
        collection.update_one(
            {"_id": _id},
            {
                "$set": {
                    "sentiment": sentiment_result["sentiment"],
                    "polarity": sentiment_result["polarity"],
                    "subjectivity": sentiment_result["subjectivity"],
                    "suggestion": suggestion,
                    "date": date,
                    "processed": True,
                }
            },
        )
