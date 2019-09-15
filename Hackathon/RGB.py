import cv2
from matplotlib import pyplot as plt

img = cv2.imread("A.jpg", 0)
pix_val = list(img)
plt.plot(pix_val)
plt.show()
