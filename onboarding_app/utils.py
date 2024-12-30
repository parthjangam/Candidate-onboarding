from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_information_from_file(file_path):
    """
    Extracts candidate information from an uploaded image or PDF file using OCR.
    Specifically tailored to the provided PDF format.
    """
    extracted_data = {'candidate_info': {}}

    try:
        # Convert PDF to images and extract text
        if file_path.endswith('.pdf'):
            images = convert_from_path(file_path)
            text = ' '.join([pytesseract.image_to_string(image) for image in images])
        else:
            text = pytesseract.image_to_string(Image.open(file_path))

        # Clean OCR output
        text = re.sub(r'\s+', ' ', text).strip()

        # Parse specific fields
        name_match = re.search(r"Name \(Block Letters.*?\):\s*(\w+)\s+(\w+)?\s+(\w+)?", text, re.IGNORECASE)
        mobile_match = re.search(r"Mobile:\s*(\d+)", text)
        address_match = re.search(r"Permanent Address:\s*(.*)", text)  # Adjust regex as needed for address

        # Extract and assign values
        if name_match:
            extracted_data['candidate_info']['first_name'] = name_match.group(1)
            if name_match.group(2):
                extracted_data['candidate_info']['middle_name'] = name_match.group(2)
            if name_match.group(3):
                extracted_data['candidate_info']['last_name'] = name_match.group(3)

        if mobile_match:
            extracted_data['candidate_info']['mobile'] = mobile_match.group(1)

        if address_match:
            extracted_data['candidate_info']['permanent_address'] = address_match.group(1)

    except Exception as e:
        print(f"Error during extraction: {e}")

    return extracted_data


