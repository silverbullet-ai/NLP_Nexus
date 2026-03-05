import PyPDF2


def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.

    Args:
        pdf_file: PDF file path or file object

    Returns:
        Extracted text from all pages
    """

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text