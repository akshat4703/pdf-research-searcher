from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(texts):
    if len(texts) < 2:
        return []
    vec = TfidfVectorizer(stop_words="english")
    tfidf = vec.fit_transform(texts)
    return cosine_similarity(tfidf)
