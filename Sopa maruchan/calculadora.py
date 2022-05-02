
import pyautogui as pt
from time import sleep

import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Darwing\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

def num1():
    sleep(0.3)
    pt.click((930, 775))

def num2():
    sleep(0.3)
    pt.click((1010, 775))

def num3():
    sleep(0.3)
    pt.click((1090, 770))

def num4():
    sleep(0.3)
    pt.click((930, 710))

def num5():
    sleep(0.3)
    pt.click((1011, 714))

def num6():
    sleep(0.3)
    pt.click((1090, 712))

def num7():
    sleep(0.3)
    pt.click((932, 650))

def num8():
    sleep(0.3)
    pt.click((1010, 655))

def num9():
    sleep(0.3)
    pt.click((1090, 649))

def igual():
    sleep(0.3)
    pt.click((1175, 790))

def sumar():
    sleep(0.3)
    pt.click((1180, 710))

def multiplicar():
    sleep(0.3)
    pt.click((1180, 580))

def runK(numba):
    if numba == 1:
        num1()
    elif numba == 2:
        num2()
    elif numba == 3:
        num3()
    elif numba == 4:
        num4()
    elif numba == 5:
        num5()
    elif numba == 6:
        num6()
    elif numba == 7:
        num7()
    elif numba == 8:
        num8()
    elif numba == 9:
        num9()


#clicker shit
end=0
chek=0
while True:
    sleep(2)
    cap = ImageGrab.grab(bbox=(835, 220, 1055, 315))
    tesstr = pytesseract.image_to_string(cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
    print(tesstr)
    cv2.destroyAllWindows()

    sleep(0.5)
    size = len(tesstr)
    tesstr = tesstr[:size - 2]

    if tesstr == "PREL":
        x = 2339
    elif tesstr == "LYYy,":
        x = 2447
    elif tesstr == "Ik":
        x = 2503
    elif tesstr == "PRYY":
        x = 2341
    elif tesstr == "PAVE":
        x = 2179
    else:
        x = int(tesstr)



    #x=1783
    aux1 = x / 9
    aux1 = aux1 - 0.05
    entero = int(aux1)
    decimal = abs(aux1) - abs(int(aux1))
    decimal = round(decimal, 1) * 10

    no3 = decimal
    if no3 < 9:
        print(no3)
        x = x - decimal
    x = x / 9

    aux1 = x / 9
    aux1 = aux1 - 0.05
    entero = int(aux1)
    decimal = abs(aux1) - abs(int(aux1))
    decimal = round(decimal, 1) * 10

    no2 = decimal
    if no2<9:
        print(no2)
        x = x - decimal
    x = x / 9
    # de aqui pa abajo es el primer digit
    no1 = x
    print(x)
    no0 = no1 - 24
    print(no0)

    # Paso1 :
    #y = 9 + no1
    #y = 9 * y
    #y = y + no2
    #y = 9 * y
    #y = y + no3
    #print(y)

#1933 2011 1951 2017 1913 1783 1741 2099
    #show time
    num6()
    multiplicar()
    num4()
    igual()
    sumar()
    runK(no0)
    igual()
    multiplicar()
    num9()
    igual()
    if no2 < 9:
        sumar()
        runK(no2)
        igual()
    multiplicar()
    num9()
    igual()
    if no3 < 9:
        sumar()
        runK(no3)
        igual()


    end += 1
    if end >= 10:
        break



