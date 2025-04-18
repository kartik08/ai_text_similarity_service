from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import nltk
# Explicitly set data path
nltk.data.path.append("/usr/local/nltk_data")
# Download only if needed
nltk.download('punkt_tab', quiet=True)

# Initialize shared TF-IDF vectorizer once
_vectorizer = TfidfVectorizer()

def cosine_sim(text1: str, text2: str) -> float:
    """
    Compute cosine similarity between two texts using TF-IDF.
    """
    tfidf_matrix = _vectorizer.fit_transform([text1, text2])
    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return float(score[0][0])  # Return as native float


def jaccard_sim(text1: str, text2: str) -> float:
    """
    Compute Jaccard similarity between two texts based on unique word tokens.
    """
    tokens1 = set(word_tokenize(text1.lower()))
    tokens2 = set(word_tokenize(text2.lower()))
    intersection = tokens1 & tokens2
    union = tokens1 | tokens2
    return len(intersection) / len(union) if union else 0.0
