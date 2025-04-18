import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Explicitly set data path
nltk.data.path.append("/usr/local/nltk_data")
# Download only if missing
nltk.download("stopwords", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Define bad words (can be loaded from DB or config file in future)
BAD_WORDS = {"badword1", "badword2"}
STOP_WORDS = set(stopwords.words("english"))

# Character limit for input sanitization
MAX_LENGTH = 500  


def clean_html_and_scripts(text: str) -> str:
    """
    Removes HTML tags and common script injection patterns.
    """
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)  
    # Remove JS patterns
    text = re.sub(r'(script|on\w+)=', '', text, flags=re.IGNORECASE)  
    return text


def tokenize_and_filter(text: str, remove_stopwords: bool = False) -> str:
    """
    Tokenizes text, removes stopwords and bad words, returns clean string.
    """
    tokens = word_tokenize(text)
    filtered = [
        word.lower()
        for word in tokens
        if word.isalpha()
        and word.lower() not in BAD_WORDS
        and (not remove_stopwords or word.lower() not in STOP_WORDS)
    ]
    return ' '.join(filtered).strip()[:MAX_LENGTH]


def sanitize_input(text: str) -> str:
    """
    Sanitizes user input by removing HTML/scripts, filtering words,
    and truncating input length.
    """
    text = clean_html_and_scripts(text)
    return tokenize_and_filter(text, remove_stopwords=True)


def sanitize_output(text: str) -> str:
    """
    Sanitizes LLM output (milder filter: no stopword removal).
    """
    return tokenize_and_filter(text, remove_stopwords=False)
