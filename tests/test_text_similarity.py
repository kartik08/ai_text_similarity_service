import unittest
import os, sys

sys.path.insert(0,"../")

from text_similarity import cosine_sim, jaccard_sim

class TestTextSimilarityFunctions(unittest.TestCase):
    
    def test_cosine_sim_identical_text(self):
        text1 = "Hello Kartik"
        text2 = "Hello Kartik"
        # Expect cosine similarity to be 1.0 since the texts are identical
        self.assertEqual(cosine_sim(text1, text2), 1.0)
    
    def test_cosine_sim_no_similarity(self):
        text1 = "Hello Kartik"
        text2 = "Goodbye universe"
        # Expect cosine similarity to be 0.0 since the texts are different
        self.assertEqual(cosine_sim(text1, text2), 0.0)
    
    def test_cosine_sim_partial_similarity(self):
        text1 = "I love programming"
        text2 = "I enjoy coding"
        # The texts have some common terms, so cosine similarity will be non-zero but less than 1
        similarity = cosine_sim(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)
    
    def test_jaccard_sim_identical_text(self):
        text1 = "Hello Kartik"
        text2 = "Hello Kartik"
        # Expect Jaccard similarity to be 1.0 since the texts are identical
        self.assertEqual(jaccard_sim(text1, text2), 1.0)
    
    def test_jaccard_sim_no_similarity(self):
        text1 = "Hello Kartik"
        text2 = "Goodbye universe"
        # Expect Jaccard similarity to be 0.0 since the texts have no common tokens
        self.assertEqual(jaccard_sim(text1, text2), 0.0)
    
    def test_jaccard_sim_partial_similarity(self):
        text1 = "I love programming"
        text2 = "I enjoy coding"
        # Expect Jaccard similarity to be a value between 0 and 1
        similarity = jaccard_sim(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)
    
    def test_jaccard_sim_empty_text(self):
        text1 = ""
        text2 = "Hello"
        # Expect Jaccard similarity to be 0.0 since one of the texts is empty
        self.assertEqual(jaccard_sim(text1, text2), 0.0)

if __name__ == "__main__":
    unittest.main()
