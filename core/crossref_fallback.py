import requests


def search_crossref(query, limit=5):
    url = "https://api.crossref.org/works"
    params = {"query": query, "rows": limit}
    res = requests.get(url, params=params, timeout=10).json()

    results = []
    for item in res["message"]["items"]:
        results.append({
            "title": item.get("title", ["Unknown"])[0],
            "authors": ", ".join(
                a.get("family", "") for a in item.get("author", [])
            ),
            "year": item.get("issued", {}).get("date-parts", [[None]])[0][0],
            "abstract": item.get("abstract", "Abstract not available"),
            "pdf_url": None,
            "link": item.get("URL"),
            "source": "crossref",
        })
    return results
