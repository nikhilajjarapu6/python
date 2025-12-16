# app/services/pdf_reader.py
import fitz

class PDFReader:
    """Handles reading text content from PDF."""

    @staticmethod
    def read_text(pdf_path: str) -> str:
        text = []
        doc = fitz.open(pdf_path)

        for page in doc:
            text.append(page.get_text())

        doc.close()
        return "\n".join(text)
