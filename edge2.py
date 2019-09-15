#!/usr/bin/python3
# Created by Silencer @ Stackoverflow 
# 2018.01.23 14:41:42 CST
# 2018.01.23 18:17:42 CST
import cv2
import numpy as np

src = cv2.imread("..\Hackathon\Bdwnsz.jpg")
src=cv2.bilateralFilter(src,9,75,75)
#kernel = np.ones((5,5),np.float32)/25
#src = cv2.filter2D(src,-1,kernel)
#src = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

src_cpy = src#cv2.imread("..\Hackathon\Bdwnsz.jpg")

N = 8

for j in range(0, src.shape[0]):
    for i in range(0, src.shape[1]):
        b = src[j, i, 0]
        g = src[j, i, 1]
        r = src[j, i, 2]

        src_cpy[j, i, 0] = int(round(b*(N/255))*(255/N))
        src_cpy[j, i, 1] = int(round(g*(N/255))*(255/N))
        src_cpy[j, i, 2] = int(round(r*(N/255))*(255/N))

#cv2.imshow('Binary Image', bw)

#cv.imshow('Laplace Filtered Image', imgLaplacian)
cv2.imwrite('BEdge.jpg', src_cpy)

## (4) Crop and save it
#x,y,w,h = cv2.boundingRect(cnt)
#dst = img[y:y+h, x:x+w]