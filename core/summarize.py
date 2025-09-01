from nltk.tokenize import sent_tokenize

def summarize_text(text, max_sentences=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences]) if sentences else "No summary available."

def summarize_all(texts):
    return [summarize_text(t) for t in texts]
