import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from core.search_providers import get_pdf_urls
from core import downloader, text_extraction, summarize, generate_docx

st.set_page_config(
    page_title="Google Scholar Research Searcher",
    layout="wide",
)

st.title("📄 Google Scholar Research Paper Searcher & Summarizer")

query = st.text_input(
    "Enter research query",
    placeholder="e.g. conspiracy theory psychology",
)

limit = st.slider(
    "Number of papers",
    min_value=1,
    max_value=10,
    value=5,
)

if st.button("🔍 Search & Generate Summary"):
    if not query.strip():
        st.warning("Please enter a research query.")
    else:
        with st.spinner("Searching Google Scholar..."):
            papers = get_pdf_urls(
                query=query,
                limit=limit,
                source="scholar",
            )

        if not papers:
            st.error("No papers found.")
        else:
            st.success(f"Found {len(papers)} papers")

            pdf_dir = Path("downloaded_papers")
            text_dir = Path("extracted_texts")

            with st.spinner("Downloading PDFs (if available)..."):
                papers = downloader.download_pdfs(papers, pdf_dir)

            with st.spinner("Extracting text with CrossRef fallback..."):
                texts, final_papers = text_extraction.extract_texts(
                    papers=papers,
                    text_dir=text_dir,
                    query=query,
                )

            if not final_papers:
                st.error("Could not extract any usable content.")
            else:
                with st.spinner("Summarizing content..."):
                    summaries = summarize.summarize_all(texts)

                for i in range(min(len(final_papers), len(summaries))):
                    final_papers[i]["content"] = summaries[i]

                report_file = "scholar_research_summary.docx"
                generate_docx.create_docx(final_papers, report_file)

                st.success("📄 DOCX report generated successfully!")

                with open(report_file, "rb") as f:
                    st.download_button(
                        label="⬇️ Download DOCX Report",
                        data=f,
                        file_name=report_file,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    )

                st.subheader("📌 Paper Summaries")
                for i, p in enumerate(final_papers, start=1):
                    st.markdown(f"### Paper {i}: {p.get('title','Unknown')}")
                    st.write(p.get("content") or p.get("abstract", ""))

                    if p.get("pdf_url"):
                        st.markdown(f"**PDF:** {p['pdf_url']}")
                    elif p.get("link"):
                        st.markdown(f"**Link:** {p['link']}")

                    st.divider()
