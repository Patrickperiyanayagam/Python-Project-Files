from PIL import Image
import pytesseract
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata-main'

# Open the image using Pillow (PIL Fork)
image_path = r'E:\Project\TextFromPic\4a4134e38575ac8427e75d3f381fd75d.jpg'
image = Image.open(image_path)

# Use pytesseract to extract Hindi text from the image
text = pytesseract.image_to_string(image, lang='eng+hin+tam')

# Print the extracted text
print(text)