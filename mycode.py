import cv2
import numpy as np 

img = cv2.imread("t2.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

weaker =np.array([0,0,100])
stronger = np.array([10,100,44])

mask = cv2.inRange(hsv,weaker,stronger)

cv2.imshow('Image',img)
cv2.imshow('Result',mask)

cv2.waitkey(1000)


