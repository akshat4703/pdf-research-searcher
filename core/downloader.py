import requests
from pathlib import Path

def download_pdfs(papers, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    for i, paper in enumerate(papers, 1):
        pdf_url = paper.get("pdf_url")
        if not pdf_url:
            paper["pdf_path"] = None
            continue

        try:
            res = requests.get(pdf_url, timeout=15)
            path = out_dir / f"paper_{i}.pdf"
            path.write_bytes(res.content)
            paper["pdf_path"] = str(path)
        except Exception:
            paper["pdf_path"] = None

    return papers
