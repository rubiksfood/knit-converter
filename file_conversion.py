from pdf2docx import Converter
from docx2pdf import convert as docx2pdf_convert


def pdf_to_docx(pdf_path: str, docx_path: str) -> None:
    cv = Converter(pdf_path)
    try:
        cv.convert(docx_path, start=0, end=None)
    finally:
        cv.close()


def docx_to_pdf(docx_path: str, pdf_path: str) -> None:
    docx2pdf_convert(docx_path, pdf_path)