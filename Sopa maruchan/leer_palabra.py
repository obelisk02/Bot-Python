import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab
from time import sleep

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Darwing\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'


sleep(1)
cap = ImageGrab.grab(bbox=(865, 170, 1120, 205))
tesstr = pytesseract.image_to_string(cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY),lang='eng')
print(tesstr)



#hangman (865, 170, 1120, 205))