import requests
from bs4 import BeautifulSoup

def search_arxiv(query, limit=5):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={limit}"
    resp = requests.get(url)
    results = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "xml")
        for entry in soup.find_all("entry"):
            results.append({
                "title": entry.title.text,
                "link": entry.id.text,
                "pdf_url": entry.id.text.replace("abs", "pdf") + ".pdf"
            })
    return results

def search_scholar(query, limit=5):
    # Dummy fallback (scholar blocks scraping)
    return [{"title": f"Dummy Scholar Paper {i+1}",
             "link": "https://example.com",
             "pdf_url": None} for i in range(limit)]

def get_pdf_urls(query, limit=5, source="both"):
    results = []
    if source in ["arxiv", "both"]:
        results.extend(search_arxiv(query, limit))
    if source in ["scholar", "both"]:
        results.extend(search_scholar(query, limit))
    return results[:limit]
