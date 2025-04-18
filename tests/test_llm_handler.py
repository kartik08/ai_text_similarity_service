import unittest

import sys
import os

sys.path.insert(0,"../")

from llm_handler import query_llm


class TestLLMHandler(unittest.TestCase):

    def test_query_llm_returns_string(self):
        prompt = "test test Prompt"
        result = query_llm(prompt=prompt)
        self.assertIsInstance(result,str)

if __name__ == "__main__":
    unittest.main()
