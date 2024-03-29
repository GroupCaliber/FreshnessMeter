
from __future__ import division
import cv2
from matplotlib import pyplot as plt 
import numpy as np 
from math import sin,cos 

green= (0,255,0)


def show(image):
    plt.figure(figsize=(10,10))
    plt.imshow(image, interpolation='nearest')

def overlay_mask(mask,image):
    rgb_mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)

    img=cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    return img

def find_biggest_contour(image):
    image=image.copy()
    contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask,contours)
    return mask

def circle_contour(image, contour):
    image_with_ellipse = image.copy()
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(image_with_ellipse,ellipse,green,2,cv2.CV_AA)
    return image_with_ellipse


def find_tom(image):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



    #step2
    max_dimension = max(image.shape)
    scale=700/max_dimension
    image = cv2.resize(image,None,fx=scale,fy=scale)


    #step3-clean

    image_blur=cv2.GaussianBlur(image,(7,7),0)
    image_blur_hsv=cv2.cvtColor(image_blur,cv2.COLOR_RGB2HSV)

    #step4 - define filters
    #color
    min_red=np.array([0,100,80])
    max_red=np.array([10,256,256])

    mask1 = cv2.inRange(image_blur_hsv,min_red, max_red)
    #brightness
    min_red2=np.array([170,100,80])
    max_red2=np.array([180,256,256])


    mask2=cv2.inRange(image_blur_hsv,min_red2,max_red2)

    #combine
    mask = mask1+mask2

    #segment
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
    mask_closed= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    mask_clean = cv2.morphologyEx(mask_closed,cv2.MORPH_OPEN, kernel)

    big_tom_contour,mask_toms=find_biggest_contour(mask_clean)

    #overlay
    overlay = overlay_mask(mask_clean,image)

    #circle
    circled = circle_contour(overlay,big_tom_contour)
    show(circled)

    #orginal color
    bgr=cv2.cvtColor(cirled,cv2.COLOR_RGB2BGR)
    return bgr

image=cv2.imread('t1.jpg')
result =find_tom(image)

cv2.imwrite('t3.jpg',result)

    

    








