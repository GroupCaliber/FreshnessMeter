import cv2
import numpy as np
from matplotlib import pyplot

img = cv2.imread('FF.jpg',0)
edges = cv2.Canny(img,100,300)
pyplot.subplot(121), pyplot.imshow(img, cmap ='gray')
pyplot.title('Original Image'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(122), pyplot.imshow(edges, cmap ='gray')
pyplot.title('Edge Image'), pyplot.xticks([]), pyplot.yticks([])
pyplot.show()

