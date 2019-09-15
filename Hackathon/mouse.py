
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys 
from PIL import Image




def mouse_callback(event, x, y, flags, params):

    if event==1:
        clicks.append([x,y])

        print(clicks)
        print("r ="+str(img[x][y][0]),"g ="+str(img[x][y][1]),"b ="+str(img[x][y][2]))

img= cv2.imread('res/7.jpg')
cv2.imshow("image",img)

cv2.setMouseCallback('image', mouse_callback)
while True:
    clicks = []
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
