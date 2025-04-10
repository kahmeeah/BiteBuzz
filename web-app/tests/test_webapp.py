"""
unit tests for web app
These tests cover routes, MongoDB interactions, and edge cases.
"""

import unittest
from unittest.mock import patch, MagicMock
from app import app


class FlaskAppTest(unittest.TestCase):

    @patch("app.collection")
    def test_submit_review_no_text(self, mock_collection):
        """
        Test the /submit route when no text is provided.
        """
        with app.test_client() as client:
            response = client.post("/submit", json={})
            self.assertEqual(response.status_code, 400)

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
            response = client.get("/result/507f1f77bcf86cd799439011")
            self.assertEqual(response.status_code, 200)

    @patch("app.collection")
    def test_get_result_not_found(self, mock_collection):
        """
        Test the /result route when review is not found.
        """
        mock_collection.find_one.return_value = None

        with app.test_client() as client:
            response = client.get("/result/507f1f77bcf86cd799439011")
            self.assertEqual(response.status_code, 404)

    @patch("app.collection")
    def test_get_result_processing(self, mock_collection):
        """
        Test the /result route when review is still processing.
        """
        mock_review = {"_id": MagicMock(), "text": "Great product!", "processed": False}
        mock_collection.find_one.return_value = mock_review

        with app.test_client() as client:
            response = client.get("/result/507f1f77bcf86cd799439011")
            self.assertEqual(response.status_code, 202)

    @patch("app.collection")
    def test_get_result_invalid_id(self, mock_collection):
        """
        Test the /result route with an invalid review ID.
        """
        with app.test_client() as client:
            response = client.get("/result/invalid_id!")
            self.assertEqual(response.status_code, 400)

    @patch("app.collection")
    def test_submit_review_success(self, mock_collection):
        """
        Test submitting a valid review.
        """
        mock_insert_result = MagicMock()
        mock_insert_result.inserted_id = "507f1f77bcf86cd799439011"
        mock_collection.insert_one.return_value = mock_insert_result

        with app.test_client() as client:
            response = client.post("/submit", json={"text": "Great product!"})
            self.assertEqual(response.status_code, 200)

