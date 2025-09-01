from pathlib import Path
from PyPDF2 import PdfReader

def extract_texts(files, out_dir, results):
    out_dir.mkdir(exist_ok=True)
    texts = []
    for i, file in enumerate(files):
        try:
            reader = PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            texts.append(text)
            with open(out_dir / f"text_{i}.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print("Extraction error:", e)
            texts.append("")
    return texts
