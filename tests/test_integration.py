import unittest
import os,sys
sys.path.insert(0,"../")
from app import create_app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Create a test client using the Flask app
        self.app = create_app().test_client()

    def test_cosine_similarity_response(self):
        
        """
        Testing Cosine based similarity testing. 
        """
        response = self.app.post("/analyze", json={
            "prompt1": "Artificial intelligence is the future.",
            "prompt2": "Aartifical intelligence will shape tomorrow.",
            "method": "cosine"
        })

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("similarity_score", data)
        self.assertIn("response", data)
        self.assertIsInstance(data["similarity_score"], float)
        self.assertIsInstance(data["response"], str)

    def test_jaccard_similarity_response(self):
        """
        Testing jaccard based similarity testing. 
        """
        response = self.app.post("/analyze", json={
            "prompt1": "Gravity pulls things down.",
            "prompt2": "What does gravity do?",
            "method": "jaccard"
        })

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("similarity_score", data)
        self.assertIn("response", data)

    def test_low_similarity_no_llm(self):

        """
        Testing Cosine based similarity testing with no simiarlity. 
        """

        response = self.app.post("/analyze", json={
            "prompt1": "The sky is blue.",
            "prompt2": "Programming in Python is fun.",
            "method": "cosine"
        })

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertLess(data["similarity_score"], 0.5)
        self.assertEqual(data["response"], "")

    def test_missing_prompts(self):
        """
        Testing llm with with missing prompt. 
        """
        response = self.app.post("/analyze", json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('Both prompt1 and prompt2 are required.', data["error"])

if __name__ == "__main__":
    unittest.main()
