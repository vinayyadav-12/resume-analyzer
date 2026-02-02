import pdfplumber
from docx import Document

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_docx_text(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

