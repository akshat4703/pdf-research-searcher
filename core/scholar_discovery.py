from scholarly import scholarly

def search_scholar(query, limit=5):
    results = []
    try:
        search = scholarly.search_pubs(query)
        for _ in range(limit):
            pub = next(search)
            bib = pub.get("bib", {})
            results.append({
                "title": bib.get("title", "Unknown title"),
                "authors": ", ".join(bib.get("author", [])),
                "year": bib.get("pub_year", ""),
                "abstract": bib.get("abstract", ""),
                "link": pub.get("pub_url"),
                "pdf_url": None  # Scholar rarely gives direct PDFs
            })
    except Exception:
        pass
    return results
