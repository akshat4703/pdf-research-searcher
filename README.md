# 📄 PDF Research Searcher & Summarizer

An end-to-end research automation tool that searches academic papers from Arxiv and Google Scholar, intelligently handles unavailable PDFs, extracts text, summarizes content, and generates structured DOCX reports.

This project is designed to work reliably with Conda environments, including Python 3.14, to avoid common dependency and compiler issues.

---

## 🚀 Features

- 🔍 Search research papers via arXiv and Google Scholar
- 📄 Download PDFs when available
- 🔁 Fallback text extraction when PDFs are blocked
- 🧠 Sentence-based summarization using NLTK
- 📊 Text similarity computation
- 📝 DOCX report generation
- 🖥 Streamlit UI + CLI interface
- 🧩 Modular backend architecture

---

## 📁 Project Structure

pdf_research_searcher/
├── core/
│ ├── search_providers.py
│ ├── scholar_discovery.py
│ ├── downloader.py
│ ├── text_extraction.py
│ ├── crossref_fallback.py
│ ├── summarize.py
│ ├── similarity.py
│ └── generate_docx.py
│
├── downloaded_papers/
├── extracted_texts/
├── pdfs/
├── runs/
│
├── ulits/
│ ├── app_cli.py
│ ├── app_streamlit_arxiv.py
│ └── app_streamlit_scholar.py
│
├── requirements.txt
└── README.md


---

## 🐍 Python & Environment Strategy

Python 3.14 currently lacks stable wheels for several scientific libraries on Windows.
To ensure stability and reproducibility, this project uses Conda.

---

## 🧪 Conda Setup (Python 3.14)

### 1️⃣ Create and activate environment
conda create -n pdf_research_py314 python=3.14 -y
conda activate pdf_research_py314

### 2️⃣ Install scientific dependencies via Conda
conda install -c conda-forge numpy scikit-learn -y

### 3️⃣ Install remaining project dependencies
pip install -r requirements.txt


📦 requirements.txt (Conda-compatible)

requests>=2.32.0
beautifulsoup4>=4.12.3
lxml>=5.2.2
tqdm>=4.66.4
pypdf>=4.2.0
pdfminer.six>=20231228
regex>=2024.5.15
nltk>=3.9.1
python-docx>=1.1.2
streamlit>=1.36.0
sentence-transformers>=3.0.1
rapidfuzz>=3.9.3

ℹ️ NumPy and scikit-learn are installed via Conda, not pip.

▶️ Running the Application

CLI
python -m ulits.app_cli --query "machine learning cancer detection" --limit 5

Streamlit (arXiv)
streamlit run ulits/app_streamlit_arxiv.py

Streamlit (Google Scholar)
streamlit run ulits/app_streamlit_scholar.py

Always run commands from the project root directory.

👤 Author

Akshat Pal