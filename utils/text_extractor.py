'''import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_txt(file):
    return file.read().decode("utf-8")'''
# text_extractor.py
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for i, page in enumerate(doc):
        if i >= 5:  # Limit to 5 pages to keep usage light
            break
        text += page.get_text()
    return text.strip()

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")
