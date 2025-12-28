import nltk
nltk.download("punkt", quiet=True)
from nltk.tokenize import sent_tokenize

def summarize_all(texts, n=3):
    summaries = []
    for t in texts:
        s = sent_tokenize(t)
        summaries.append(" ".join(s[:n]) if s else "")
    return summaries
