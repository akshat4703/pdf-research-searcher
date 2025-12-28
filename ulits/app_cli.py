import argparse
from pathlib import Path

from core import (
    search_providers,
    downloader,
    text_extraction,
    summarize,
    generate_docx,
)


def main():
    parser = argparse.ArgumentParser(
        description="Research Paper Searcher & Summarizer"
    )
    parser.add_argument(
        "--query", required=True, help="Research query"
    )
    parser.add_argument(
        "--limit", type=int, default=5, help="Number of papers"
    )
    parser.add_argument(
        "--source",
        choices=["arxiv", "scholar", "both"],
        default="both",
        help="Paper source",
    )
    parser.add_argument(
        "--report",
        default="research_summary.docx",
        help="Output DOCX file",
    )

    args = parser.parse_args()

    pdf_dir = Path("downloaded_papers")
    text_dir = Path("extracted_texts")

    print(f"🔍 Searching papers for: {args.query}")
    papers = search_providers.get_pdf_urls(
        query=args.query,
        limit=args.limit,
        source=args.source,
    )

    if not papers:
        print("❌ No papers found.")
        return

    print("📄 Downloading PDFs where available...")
    papers = downloader.download_pdfs(papers, pdf_dir)

    print("📝 Extracting text with fallbacks...")
    texts, final_papers = text_extraction.extract_texts(
        papers=papers,
        text_dir=text_dir,
        query=args.query,
    )

    if not final_papers:
        print("❌ No usable content found.")
        return

    print("✍️ Summarizing content...")
    summaries = summarize.summarize_all(texts)

    for i in range(min(len(final_papers), len(summaries))):
        final_papers[i]["content"] = summaries[i]

    print(f"📄 Generating DOCX report: {args.report}")
    generate_docx.create_docx(final_papers, args.report)

    print("✅ Done! Research summary generated successfully.")


if __name__ == "__main__":
    main()
