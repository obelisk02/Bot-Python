import cv2 as cv
import pyautogui as pt

from time import sleep
from PIL import ImageGrab

array_correctos = []
array_checkers = []
array_final = []
coords = [270,183, 222,  182, 310, 265, 310, 224]
# All the 6 methods for comparison in a list
img_templates = ['energia1.png','energia2.png','avena1.png','avena2.png','cereal1.png','cereal2.png','fibra1.png','fibra2.png',
                 'integral1.png','integral2.png','natural1.png','natural2.png','proteina1.png','proteina2.png','quaker1.png','quaker2.png']


filepath = 'full.png'

sleep(0.4)
screenshot = ImageGrab.grab(bbox=(625, 286 ,1275, 940))
screenshot.save(filepath, 'PNG')

imgF = cv.imread('full.png',0)

#img2 = img.copy()


for image in img_templates:
    img = imgF.copy()

    template = cv.imread(image, 0)
    w, h = template.shape[::-1]
    # ----------- > method = eval('cv.TM_CCOEFF_NORMED')
    method = eval('cv.TM_CCOEFF_NORMED')
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    #if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
    #    top_left = min_loc
    #else:
    print(image , ":" ,max_loc, "- min loc:",  min_loc, " / amin val: ", min_val, "- max loc: ", max_val)
    array_correctos.append(max_loc)
    array_checkers.append(max_val)
    #array_correctos.append(image , ":" ,max_loc, "- min loc:",  min_loc, " / amin val: ", min_val, "- max loc: ", max_val)


#
cont = 0
for checkin in array_checkers:      #0 -2 -4 -6 -8 -10 -12 -14
    contmas1 = cont + 1
    if array_checkers[cont] > array_checkers[contmas1]:
        #print(cont, " ", array_checkers[cont])
        array_final.append(0)
        array_final.append(array_correctos[cont])
    else:
        #print(contmas1, " ", array_checkers[contmas1])
        array_final.append(1)
        array_final.append(array_correctos[contmas1])
    if cont != 14:
        cont += 2
    else:
        break
print( array_final)



unade8= 0
for i in range(0,15,2): #screenshot = ImageGrab.grab(bbox=(625, 286 ,1275, 935))
    sleep(0.43)
    #print(i)
    if array_final[i] == 0: #Horizontal
        pt.moveTo( (array_final[i+1][0] + 635), (array_final[i+1][1] +  302) )
        pt.drag(coords[unade8], 0 ,0.6, button='left')
    elif array_final[i] == 1: #Vertical
        pt.moveTo((array_final[i + 1][0] + 640), (array_final[i + 1][1] + 293))
        pt.drag(0, coords[unade8] ,0.5, button='left')

    #moves+=2
    unade8+=1
