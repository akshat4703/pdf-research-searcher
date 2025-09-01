import requests
from pathlib import Path

def download_pdfs(results, out_dir):
    out_dir.mkdir(exist_ok=True)
    downloaded = []
    for r in results:
        url = r.get("pdf_url")
        if not url: continue
        fname = out_dir / (r['title'].replace(" ", "_")[:50] + ".pdf")
        try:
            resp = requests.get(url, timeout=20)
            if resp.status_code == 200:
                with open(fname, "wb") as f:
                    f.write(resp.content)
                downloaded.append(fname)
        except Exception as e:
            print("Error downloading:", e)
    return downloaded
