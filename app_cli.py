import argparse
from pathlib import Path
from core import search_providers, downloader, text_extraction, summarize, similarity, generate_docx

def main():
    parser = argparse.ArgumentParser(description="Research Paper Downloader & Summarizer")
    parser.add_argument("--query", required=True, help="Research query")
    parser.add_argument("--limit", type=int, default=5, help="Number of papers to fetch")
    parser.add_argument("--source", choices=["scholar", "arxiv", "both"], default="both", help="Paper source")
    parser.add_argument("--report", default="research_summary.docx", help="Output DOCX file")
    args = parser.parse_args()

    pdf_dir = Path("downloaded_papers")
    text_dir = Path("extracted_texts")

    print(f"\n🔍 Searching papers for query: {args.query}")
    results = search_providers.get_pdf_urls(args.query, limit=args.limit, source=args.source)

    if not results:
        print("No results found.")
        return

    print(f"Found {len(results)} papers. Downloading...")
    downloaded = downloader.download_pdfs(results, pdf_dir)

    if not downloaded:
        print("No PDFs downloaded.")
        return

    print("📄 Extracting text...")
    texts = text_extraction.extract_texts(downloaded, text_dir, results)

    print("✍️ Summarizing...")
    summaries = summarize.summarize_all(texts)

    print("📊 Similarity matrix...")
    sim_matrix = similarity.compute_similarity(texts)

    print(f"📝 Generating DOCX report: {args.report}")
    generate_docx.create_docx(summaries, output_file=args.report)

    print("✅ Done!")

if __name__ == "__main__":
    main()
