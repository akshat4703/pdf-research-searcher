from pypdf import PdfReader
import requests
from io import BytesIO

def extract_pdf_text(source):
    try:
        if source.startswith("http"):
            pdf = requests.get(source, timeout=15).content
            reader = PdfReader(BytesIO(pdf))
        else:
            reader = PdfReader(source)

        return "\n".join(p.extract_text() or "" for p in reader.pages)
    except Exception:
        return ""
