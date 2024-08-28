from PIL import Image
import pytesseract

# Specify the full path to the Tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

# Example usage
image_path = r'C:\Users\admin\ShreyaProjects\pythonProjectCourseInfosys\DCC Card.jpg'
text = image_to_text(image_path)
print(text)
