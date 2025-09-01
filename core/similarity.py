from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(texts):
    try:
        vectorizer = TfidfVectorizer().fit_transform(texts)
        return cosine_similarity(vectorizer)
    except Exception:
        return np.array([])
