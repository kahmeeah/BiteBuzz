"""Main module for processing and analyzing customer reviews from MongoDB."""

import os
from datetime import datetime
import time

# from dotenv import load_dotenv
import pymongo

from helpers.analyze_sentiment import analyze_sentiment
from helpers.generate_suggestion import generate_suggestion
from helpers.detect_category_map import detect_category_map


# docker???
# load_dotenv(override=True)

# database_url = os.getenv("MONGO_URI")
# client = pymongo.MongoClient(database_url)
# db = client[os.getenv("MONGO_DBNAME")]
# collection = db["reviews"]

# this is the new mongo connection stuff
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["bitebuzz"]
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
        categories = detect_category_map(review_text)
        category = categories[0]
        key_word = category.lower()
        suggestion = generate_suggestion(
            review_text, sentiment_result["sentiment"], key_word
        )

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
                    "category": category,
                    "date": date,
                    "processed": True,
                }
            },
        )


if __name__ == "__main__":
    print("ml client started, periodically checking for unprocessed reviews")
    while True:
        process_unprocessed_reviews()
        time.sleep(2)  # polling interval: every 2 seconds, can change later
