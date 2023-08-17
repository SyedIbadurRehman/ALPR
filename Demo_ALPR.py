import easyocr
import cv2
import re
from PIL import Image
import os

def extract_patterns(result):
    pattern1 = r'\b[A-Z]{1,3}\b'
    pattern2 = r'\d{3,4}'
    extracted_letters = None
    extracted_digits = None

    for item in result:
        if not extracted_letters:
            match_letters = re.search(pattern1, item)
            if match_letters:
                extracted_letters = match_letters.group(0)

        if not extracted_digits:
            match_digits = re.search(pattern2, item)
            if match_digits:
                extracted_digits = match_digits.group(0)

        if extracted_letters and extracted_digits:
            break

    return extracted_letters, extracted_digits

files = os.listdir("path to your data")
for file in files:
    reader = easyocr.Reader(['en'])
    result = reader.readtext(os.path.join("path to your data",file), detail=0)
    plate = extract_patterns(result)
    img = Image.open(os.path.join("path to your data",file))
    print(plate)
    img.show()
)

