import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num, page in enumerate(reader.pages):
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                print(f"Warning: No text extracted from page {page_num}")
        except Exception as e:
            print(f"Error reading page {page_num}: {e}")
    return text
