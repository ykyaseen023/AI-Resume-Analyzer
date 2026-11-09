from pypdf import PdfReader
from docx import Document


def extract_resume_text(file_path):

    if file_path.lower().endswith('.pdf'):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    elif file_path.lower().endswith('.docx'):

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format")
    