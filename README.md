# 📄 PDF Research Paper Searcher

A Python-based tool that allows users to **search, download, extract, and summarize research papers** from **Google Scholar and arXiv**.  
The project supports both **CLI** and **Streamlit UI** for flexibility.  

---

## ✨ Features
- 🔎 Search research papers by query (Google Scholar + arXiv).  
- 📥 Download PDFs automatically.  
- 📑 Extract text from research papers.  
- 📝 Generate summaries of extracted content.  
- 📊 Compute similarity between papers.  
- 📄 Export results as a structured DOCX report.  
- 🖥️ Use via **CLI** or **Streamlit Web App**.  

---

## 🚀 Installation
```bash
git clone https://github.com/akshat4703/pdf-research-searcher.git
cd pdf-research-searcher
pip install -r requirements.txt

⚡ Usage
CLI
python app_cli.py --query "machine learning cancer detection" --limit 5 --source both

Streamlit UI
streamlit run app_streamlit.py

📂 Project Structure
pdf-research-searcher/
│── core/
│   ├── search_providers.py   # Scholar + Arxiv search
│   ├── downloader.py         # PDF downloader
│   ├── text_extraction.py    # Extract text from PDFs
│   ├── summarize.py          # Summarization logic
│   ├── similarity.py         # Similarity computation
│   ├── generate_docx.py      # DOCX report generator
│
│── app_cli.py                # CLI entry point
│── app_streamlit.py          # Streamlit web app
│── requirements.txt
│── README.md

🛠️ Tech Stack

Python

Streamlit (UI)

NLTK / Scikit-learn (Summarization & similarity)

python-docx (Report generation)

📌 Example Output

Research papers automatically downloaded.

Summaries generated per paper.

DOCX report saved with structured summaries.

📜 License

This project is licensed under the MIT License.