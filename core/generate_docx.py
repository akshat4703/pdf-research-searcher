from docx import Document

def create_docx(summaries, output_file="summary.docx"):
    doc = Document()
    doc.add_heading("Research Summaries", level=1)
    for i, s in enumerate(summaries, start=1):
        doc.add_heading(f"Paper {i}", level=2)
        doc.add_paragraph(s)
    doc.save(output_file)
    return output_file
