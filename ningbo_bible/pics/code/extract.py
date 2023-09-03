import pytesseract
from PIL import Image

def extract_words_from_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='fra')

    # Split the text into words and return
    words = text.split()
    return words


image_path = input("ningbo_bible/pics/1.1.png")
words = extract_words_from_image(image_path)
print("Extracted words:", words)
