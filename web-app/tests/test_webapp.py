"""
unit tests for web app
These tests cover routes, MongoDB interactions, and edge cases.
"""

import unittest
from unittest.mock import patch, MagicMock
from app import app


class FlaskAppTest(unittest.TestCase):
    """
    Test cases for the Flask web application.
    These tests verify functionality of the app's routes and MongoDB interactions.
    """
    @patch("app.collection")
    def test_submit_review_success(self, mock_collection):
        """
        Test the /submit route for successfully submitting a review.
        """
        mock_collection.insert_one.return_value = MagicMock(inserted_id="12345")

        with app.test_client() as client:
            response = client.post("/submit", json={"text": "Great product!"})

            self.assertEqual(response.status_code, 200)
            self.assertIn("id", response.json)
            self.assertEqual(response.json["id"], "12345")

    @patch("app.collection")
    def test_submit_review_no_text(self, mock_collection):
        """
        Test when no text is provided
        """
        with app.test_client() as client:
            response = client.post("/submit", json={})

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json["error"], "No text provided")

    @patch("app.collection")
    def test_get_result_success(self, mock_collection):
        """
        Test the /result route for successfully retrieving a processed review.
        """
        mock_review = {
            "_id": MagicMock(),
            "text": "Great product!",
            "processed": True,
            "sentiment": "positive",
            "suggestion": "Keep it up",
            "category": "product",
            "polarity": 0.8,
            "subjectivity": 0.5,
        }
        mock_collection.find_one.return_value = mock_review

        with app.test_client() as client:
            response = client.get("/result/12345")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["text"], "Great product!")
            self.assertEqual(response.json["sentiment"], "positive")
            self.assertEqual(response.json["suggestion"], "Keep it up")

    @patch("app.collection")
    def test_get_result_not_found(self, mock_collection):
        """
        Test the /result route when review is not found.
        """
        mock_collection.find_one.return_value = None

        with app.test_client() as client:
            response = client.get("/result/12345")

            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json["error"], "Not found")

    @patch("app.collection")
    def test_get_result_processing(self, mock_collection):
        """
        Test the /result route when review is still processing.
        """
        mock_review = {"_id": MagicMock(), "text": "Great product!", "processed": False}
        mock_collection.find_one.return_value = mock_review

        with app.test_client() as client:
            response = client.get("/result/12345")

            self.assertEqual(response.status_code, 202)
            self.assertEqual(response.json["status"], "processing")

    @patch("app.collection")
    def test_get_result_invalid_id(self, mock_collection):
        """
        Test the /result route with an invalid review ID.
        """
        with app.test_client() as client:
            response = client.get("/result/invalid_id")

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json["error"], "Invalid review ID")


if __name__ == "__main__":
    unittest.main()
