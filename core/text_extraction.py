from pathlib import Path
import requests
from bs4 import BeautifulSoup

from core.pdf_text import extract_pdf_text
from core.crossref_fallback import search_crossref


def extract_html_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return " ".join(soup.get_text(separator=" ").split())


def is_garbage_text(text: str) -> bool:
    bad_phrases = [
        "just a moment",
        "enable javascript",
        "cookies",
        "sign in",
        "google books",
        "privacy policy",
        "terms of service",
    ]
    t = text.lower()
    return any(b in t for b in bad_phrases) or len(text) < 500


def extract_texts(papers, text_dir, query=None):
    """
    Returns:
    - texts: list[str] usable text or abstracts
    - final_papers: enriched paper dicts (including CrossRef fallback)
    """
    text_dir.mkdir(exist_ok=True)

    texts = []
    final_papers = []

    for i, paper in enumerate(papers, start=1):
        text = ""

        try:
            # 1️⃣ PDF extraction
            if paper.get("pdf_path"):
                text = extract_pdf_text(paper["pdf_path"])

            # 2️⃣ HTML fallback
            elif paper.get("pdf_url") or paper.get("link"):
                text = extract_html_text(paper.get("pdf_url") or paper.get("link"))

            # 3️⃣ Validate extracted text
            if text and not is_garbage_text(text):
                texts.append(text)
                final_papers.append(paper)
                (text_dir / f"text_{i}.txt").write_text(text, encoding="utf-8")
                continue

            # 4️⃣ Abstract fallback
            if paper.get("abstract"):
                texts.append(paper["abstract"])
                final_papers.append(paper)
                continue

        except Exception:
            pass

    # 5️⃣ Scholar failed → CrossRef fallback
    if not final_papers and query:
        crossref_papers = search_crossref(query, limit=5)
        for p in crossref_papers:
            texts.append(p.get("abstract", ""))
            final_papers.append(p)

    return texts, final_papers
