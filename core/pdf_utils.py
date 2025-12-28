def is_valid_pdf(path):
    return path.exists() and path.suffix.lower() == ".pdf"
