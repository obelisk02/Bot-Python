
import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab
from time import sleep

import pyautogui as pt


def llamada(letra):
    if letra == 'q':
        pt.click((900, 815))
    elif letra == 'w':
        pt.click((960, 815))
    elif letra == 'e':
        pt.click((1020, 815))
    elif letra == 'r':
        pt.click((1080, 815))
    elif letra == 't':
        pt.click((1140, 815))
    elif letra == 'y':
        pt.click((1200, 815))
    elif letra == 'u':
        pt.click((1260, 815))
    elif letra == 'i':
        pt.click((1320, 815))
    elif letra == 'o':
        pt.click((1380, 815))
    elif letra == 'p':
        pt.click((1440, 815))
    elif letra == 'a':
        pt.click((900, 870))
    elif letra == 's':
        pt.click((960, 870))
    elif letra == 'd':
        pt.click((1020, 870))
    elif letra == 'f':
        pt.click((1080, 870))
    elif letra == 'g':
        pt.click((1140, 870))
    elif letra == 'h':
        pt.click((1200, 870))
    elif letra == 'j':
        pt.click((1260, 870))
    elif letra == 'k':
        pt.click((1320, 870))
    elif letra == 'l':
        pt.click((1380, 870))
    elif letra == 'ñ':
        pt.click((1440, 870))
    elif letra == 'z':
        pt.click((985, 925))
    elif letra == 'x':
        pt.click((1045, 925))
    elif letra == 'c':
        pt.click((1105, 925))
    elif letra == 'v':
        pt.click((1165, 925))
    elif letra == 'b':
        pt.click((1225, 925))
    elif letra == 'n':
        pt.click((1285, 925))
    elif letra == 'm':
        pt.click((1345, 925))




pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'
pala_limpia =[]
sleep(3)

end = 0
while True:
    sleep(1.9)
    cap = ImageGrab.grab(bbox=(865, 170, 1120, 205))
    tesstr = pytesseract.image_to_string(cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
    #print(tesstr)
    size = len(tesstr)
    palabra = tesstr[:size - 2]
    #print(palabra)
    #palabra = tesstr

    #Aqui haces los if else para encontrar la palabra y pasarle la respuesta a pala_limpia
    if palabra == "La palabra “cuece” e":
        pala_limpia = ['f', 'a', 'b', 'd', 'e','g', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u'] #CV   F
    elif palabra == "£Qué es una sintesis":
        pala_limpia = ['g', 'a', 'c', 'd', 'e', 'i', 'n', 'o', 'p', 'r', 's', 'u', 'y'] #MT     G
    elif palabra == "L CIETS G T EXCYS": #horacio quiroga
        pala_limpia = ['f', 'a', 'd', 'e', 'g', 'i', 'l', 'n', 'o', 'r', 't', 'u', 'v', 'y'] #SC     F
    elif palabra == "Obra de escritor com":
        pala_limpia = ['h','a', 'b', 'c', 'd', 'e', 'i', 'j', 'k', 'l', 'o', 'p', 'r', 's', 'x', 'y'] #MT   H
    elif palabra == "El idioma es...":
        pala_limpia = ['a', 'c', 'd', 'e', 'g', 'i', 'l', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'z'] #MT
    elif palabra == "2Qué es el premio Né":
        pala_limpia = ['b', 'a', 'c', 'd', 'e', 'g', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'u'] #FL     B
    elif palabra == "L ECE EL G CXC 1T":   #POETA GENERAICON DEL 27
        pala_limpia = ['x', 'a', 'c', 'd', 'e', 'g', 'i', 'l', 'n', 'o', 'p', 'r', 't'] #F   X
    elif palabra == "Atenea era":
        pala_limpia = ['z', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'n', 'o', 'r', 't', 'u'] #MS  Z
    elif palabra == "(VEL YR T T": #Ad Hoc
        pala_limpia = ['g', 'a', 'c', 'e', 'f', 'i', 'n', 'o', 'p', 's', 't', 'u', 'v'] #RL      G
    elif palabra == "Uso del adjetivo “oni":
        pala_limpia = ['a', 'c', 'd', 'e', 'i', 'l', 'n', 'o', 'p', 'r', 'u', 'v', 'ñ'] #ST
    elif palabra == "£Qué es la sintaxis?":
        pala_limpia = ['a', 'c', 'd', 'e', 'i', 'l', 'm', 'n', 'o', 'r', 's', 't', 'u', 'x', 'y'] #PB
    elif palabra == "La Real Academia Es":
        pala_limpia = ['a', 'c', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'z'] #DG
    elif palabra == "Obra de escritor fran":
        pala_limpia = ['a', 'c', 'e', 'i', 'x', 'l', 'n', 'o', 'r', 's', 't', 'u'] #MD
    elif palabra == "Definicion de “frase”":
        pala_limpia = ['a', 'b', 'c', 'e', 'i', 'j', 'l', 'n', 'o', 'q', 'r', 's', 't', 'u', 'y'] #PD
    elif palabra == "Caracteriza a escritc":
        pala_limpia = ['a', 'b', 'c', 'd', 'e', 'i', 'l', 'n', 'o', 'q', 'r', 's', 'u', 'v', 'z'] #GM
    elif palabra == "Otelo es un personaj":
        pala_limpia = ['a', 'd', 'e', 'i', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 'u'] #CH
    elif palabra == "Definicion de “epitaf":
        pala_limpia = ['a', 'd', 'e', 'f', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']   #PC
    elif palabra == "P TEXC-ER N EVEY P": #QUE ES LEXEMA
        pala_limpia = ['a', 'b', 'd', 'e', 'i', 'l', 'm', 'n', 'o', 'r', 's', 't', 'u', 'v'] #PF
    elif palabra == "Obra erdtica de escri":
        pala_limpia = ['a', 'd', 'e', 'g', 'i', 'j', 'l', 'o', 'r', 's', 't'] #HB
    elif palabra == "Obra dramatirgica d":
        pala_limpia = ['a', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 'u', 'z'] #TJ
    elif palabra == "Novela de dramaturg": #brasileño
        pala_limpia = ['a', 'c', 'd', 'e', 'h', 'i', 'l', 'm', 'n', 'o', 's', 'u'] #PT
    elif palabra == "DEVTYHCL Y Gl G 6": #Def de Destajo
        pala_limpia = ['a', 'd', 'e', 'f', 'i', 'l', 'm', 'n', 'o', 'r', 'u', 'ó'] #PC
    elif palabra == "DEVTYHCL Y Gl ELEL T":  #Def Palabra
        pala_limpia = ['a', 'c', 'e', 'f', 'g', 'i', 'j', 'l', 'n', 'o', 'p', 'r', 's', 'u', 'x', 'y'] #DT
    elif palabra == "Escultura griega fam":
        pala_limpia = ['a', 'c', 'd', 'e', 'i', 'l', 'o', 'r', 's', 'u', 'v'] #MT
    elif palabra == "LELNE DI EY X CAAE]":  #Rodrigo diaz vivar
        pala_limpia = ['a', 'b', 'c', 'e', 'g', 'i', 'l', 'm', 'o', 'p', 'r', 's', 't']  #ND
    elif palabra == "Definicion de parafrz":
        pala_limpia = ['a', 'c', 'd', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'u'] #FT
    elif palabra == " ": #La enunciación es…
        pala_limpia = ['a', 'b', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'x']  #DC
    elif palabra == "¢Por qué es conocide":  #Walter groupius
        pala_limpia = ['a', 'c', 'd', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 's', 'u']
    elif palabra == "Muere de viejo en no":
        pala_limpia = ['a', 'b', 'e', 'i', 'l', 'n', 'o', 'r', 's', 'v'] #MJ
    elif palabra == "El lenguaje es...":
        pala_limpia = ['a', 'c', 'e', 'f', 'i', 'j', 'l', 'n', 'o', 'p', 'r', 's', 't', 'u', 'x', 'y']  #DG
    elif palabra == "Obra de Italo Calvino":
        pala_limpia = ['a', 'b', 'c', 'd', 'e', 'g', 'l', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v'] #IM
    elif palabra == "":
        pala_limpia = ""

    #recorre la respuesta y letra por letra click
    for i in range(len(pala_limpia)):
        letra1 = pala_limpia[i]
        llamada(letra1)
        sleep(0.24) #0.22

    end += 1
    pala_limpia=""
    if end > 14:
        break

