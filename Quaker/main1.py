import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab, Image
import pyautogui as pt
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

sleep(1)



filepath = 'full.png'
#screenshot = ImageGrab.grab(bbox=(630,285, 1277,323))
#screenshot.save(filepath, 'PNG')

print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('full.png')))


cap = Image.open('full.png')
#cap = ImageGrab.grab(bbox=(630,285, 660,940))
tesstr = pytesseract.image_to_string(cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
size = len(tesstr)
palabra = tesstr[:size - 2]

print(palabra)



img_cv = cv2.imread('full.png')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)



img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))