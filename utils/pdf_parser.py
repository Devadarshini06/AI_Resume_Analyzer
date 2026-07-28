import fitz  # PyMuPDF library

def extract_text_from_pdf(pdf_path):
    """
    Opens a PDF file from disk and extracts all text content page by page.
    
    Args:
        pdf_path (str): The absolute or relative file path to the target PDF.
        
    Returns:
        str: Accumulated plain text extracted from the PDF, or an empty string if reading fails.
    """
    extracted_text = ""
    
    try:
        # Open the PDF document using PyMuPDF (fitz)
        doc = fitz.open(pdf_path)
        
        # Iterate over each page in the document
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Extract plain text from the page
            text = page.get_text("text")
            
            if text:
                extracted_text += text + "\n"
                
        doc.close()
        
    except Exception as e:
        print(f"Error reading PDF file {pdf_path}: {e}")
        return ""

    # Clean up excessive whitespace/lines while preserving readable formatting
    cleaned_text = "\n".join([line.strip() for line in extracted_text.splitlines() if line.strip()])
    
    return cleaned_text