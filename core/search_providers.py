from core.scholar_discovery import search_scholar
from core.crossref_fallback import search_crossref

try:
    import arxiv
except ModuleNotFoundError:
    arxiv = None

def get_pdf_urls(query, limit=5, source="both"):
    papers = []

    # -------- arXiv --------
    if source in ("arxiv", "both") and arxiv is not None:
        search = arxiv.Search(
            query=query,
            max_results=limit * 2,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        for r in search.results():
            papers.append({
                "title": r.title,
                "pdf_url": r.pdf_url,
                "source": "arxiv",
            })


    # -------- Google Scholar --------
    if source in ("scholar", "both"):
        try:
            papers.extend(search_scholar(query, limit))
        except Exception:
            pass  # Scholar is best-effort only

    # -------- CrossRef fallback (discovery-level) --------
    if not papers:
        papers.extend(search_crossref(query, limit))

    return papers[:limit]
