import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
''' Include above line on Windows '''

img = cv2.imread('sample-1.jpg')
# dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
text = pytesseract.image_to_string(img)
cv2.imshow('filtered', img)
print text
cv2.waitKey(0)
