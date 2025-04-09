"""main app.py for flask"""

# import os
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
import pymongo


app = Flask(__name__)

# mongodb connection
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["bitebuzz"]
collection = db["reviews"]


@app.route("/")
def index():
    """renders index.html"""
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
# this sends the data to the db
def submit_review():
    review_text = request.json.get("text")
    if not review_text:
        return jsonify({"error": "No text provided"}), 400

    doc = {"text": review_text, "processed": False}
    result = collection.insert_one(doc) # here!
    return jsonify({"id": str(result.inserted_id)})


@app.route("/result/<review_id>")
# this retrieves the data
def get_result(review_id):
    try:
        review = collection.find_one({"_id": ObjectId(review_id)})
        if not review:
            return jsonify({"error": "Not found"}), 404
        if not review.get("processed"):
            return jsonify({"status": "processing"}), 202

        return jsonify({
            "text": review["text"],
            "sentiment": review["sentiment"],
            "suggestion": review["suggestion"],
            "category": review["category"],
            "polarity": review["polarity"],
            "subjectivity": review["subjectivity"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
