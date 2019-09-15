
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
from PIL import Image




def mouse_callback(event, x, y, flags, params):

    if event==1:
        clicks.append([x,y])

        #print(clicks)
        print("sobelx ="+str(sobelx[x][y]), "sobely ="+str(sobely[x][y]))

img0= cv2.imread('res/out7.jpg')
cv2.imshow("image",img0)
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelox = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobeloy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y


sobelx=sobelox-np.min(sobelox)
sobelx=sobelx/(np.max(sobelx))

sobely=sobeloy-np.min(sobeloy)
sobely=sobely/(np.max(sobely))

cv2.setMouseCallback('image', mouse_callback)
while True:
    clicks = []
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
