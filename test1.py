import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread("2.jpg",0)
#print(img.shape)
#print(img)

img = cv2.imread('t2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#detect it
#result = find_strawberry(image)
#write the new image
cv2.imwrite('t.jpg', thresh)

def show(image):
    # Figure size in inches
    plt.figure(figsize=(10, 10))

    # Show image, with nearest neighbour interpolation
    plt.imshow(image, interpolation='nearest')