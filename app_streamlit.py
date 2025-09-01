import streamlit as st
from pathlib import Path
from core import search_providers, downloader, text_extraction, summarize, similarity, generate_docx

st.title("📑 Research Paper Searcher & Summarizer")

query = st.text_input("Enter research query", "machine learning cancer detection")
limit = st.slider("Number of results", 1, 20, 5)
source = st.selectbox("Source", ["scholar", "arxiv", "both"])

if st.button("Search and Process"):
    pdf_dir = Path("downloaded_papers")
    text_dir = Path("extracted_texts")

    st.write(f"🔍 Searching for '{query}'...")
    results = search_providers.get_pdf_urls(query, limit=limit, source=source)

    if not results:
        st.error("No papers found.")
    else:
        st.success(f"Found {len(results)} papers")
        for r in results:
            st.markdown(f"- **{r['title']}** [Link]({r.get('link','')})")

        st.write("📥 Downloading PDFs...")
        downloaded = downloader.download_pdfs(results, pdf_dir)

        if downloaded:
            st.success(f"Downloaded {len(downloaded)} papers")

            st.write("📄 Extracting text...")
            texts = text_extraction.extract_texts(downloaded, text_dir, results)

            st.write("✍️ Summarizing papers...")
            summaries = summarize.summarize_all(texts)

            for i, s in enumerate(summaries, start=1):
                st.subheader(f"Summary {i}")
                st.write(s)

            st.write("📊 Computing similarity...")
            sim_matrix = similarity.compute_similarity(texts)
            st.write(sim_matrix)

            report_file = f"Research_Summary_{query.replace(' ', '_')}.docx"
            generate_docx.create_docx(summaries, output_file=report_file)

            with open(report_file, "rb") as f:
                st.download_button("Download Report", f, file_name=report_file)

        else:
            st.error("Failed to download PDFs.")
