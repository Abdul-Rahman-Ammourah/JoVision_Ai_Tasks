from PIL import Image # type: ignore
import pytesseract # type: ignore
import re
from Functions.GUIrequest import open_image_file

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
def Clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = cleaned_text.rstrip('\n')
    return cleaned_text
try:
    text = extract_text_from_image(open_image_file())
    cleaned_text = Clean_text(text)
    print("Extracted text from image: ", cleaned_text)
except Exception as e:
    print("Error: ",e)