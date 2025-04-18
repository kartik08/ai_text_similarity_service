import unittest
import sys
import os

sys.path.insert(0,"../")

from text_sanitization import clean_html_and_scripts, tokenize_and_filter, sanitize_input,sanitize_output

class TestSanitizationFunctions(unittest.TestCase):
    
    def test_clean_html_and_scripts(self):
        # Test removing HTML and script injections
        text = '<html><body><script>alert("hello");</script></body></html>'
        cleaned_text = clean_html_and_scripts(text)
        self.assertEqual(cleaned_text, '')

        text = '<div>Hello World</div>'
        cleaned_text = clean_html_and_scripts(text)
        self.assertEqual(cleaned_text, 'Hello World')

    def test_tokenize_and_filter(self):
        # Simple case without stopwords or bad words
        text = "This is a simple test sentence"
        cleaned_text = tokenize_and_filter(text)
        self.assertEqual(cleaned_text, "This simple test sentence")
        
        # Test with stop words and bad words
        text = "This is a badword1 test sentence"
        cleaned_text = tokenize_and_filter(text, remove_stopword=True)
        self.assertEqual(cleaned_text, "test sentence")

        # Test that long input is truncated to 500 characters
        long_text = "a" * 600
        cleaned_text = tokenize_and_filter(long_text)
        self.assertEqual(len(cleaned_text), 500)

    def test_sanitize_input(self):
        # Test sanitizing user input (combines clean_html_and_scripts and tokenize_and_filter)
        text = '<script>badword1</script> This is a badword2 test'
        sanitized_text = sanitize_input(text)
        self.assertEqual(sanitized_text, "test")
        
        # Test input with html, script injections, and stop words
        text = '<div>Hello world, this is a test with badword1 and badword2.</div>'
        sanitized_text = sanitize_input(text)
        self.assertEqual(sanitized_text, "Hello world test")

    def test_sanitize_output(self):
        # Test sanitizing LLM output (similar to sanitize_input but without stopword removal)
        text = 'This is a badword1 test'
        sanitized_output = sanitize_output(text)
        self.assertEqual(sanitized_output, "This is test")

    def test_stopwords_and_badwords_handling(self):
        # Test that stopwords and badwords are handled correctly

        text = "The quick brown fox is in the badword1 forest"
        sanitized_text = tokenize_and_filter(text, remove_stopword=True)
        self.assertEqual(sanitized_text, "quick brown fox forest")

    def test_empty_input(self):
        # Test with empty string
        text = ""
        sanitized_text = sanitize_input(text)
        self.assertEqual(sanitized_text, "")

    def test_non_alphabetic_words(self):
        # Test input with numbers and punctuation
        text = "123 456 @#& badword1"
        sanitized_text = tokenize_and_filter(text)
        self.assertEqual(sanitized_text, "")

if __name__ == "__main__":
    unittest.main()
