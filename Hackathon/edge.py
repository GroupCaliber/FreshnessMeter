import cv2
import numpy as np
import sys
from matplotlib import pyplot

for i in range(1, 20+1):
    path = sys.argv[1] + str(i) + ".jpg"

    frame = cv2.imread(path)
    #frame =  cv2.fastNlMeansDenoisingColored(frame1,None,10,10,7,21)

    # Converting the image to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Using the Canny filter to get contours
    edges = cv2.Canny(gray, int(sys.argv[2]), int(sys.argv[3]))
    # Using the Canny filter with different parameters
    #edges_high_thresh = cv2.Canny(gray, 60, 120)
    # Stacking the images to print them together
    # For comparison
    #images = np.hstack((edges))

    # Display the resulting frame
    #cv2.imshow('Frame', edges)

    coords = cv2.findNonZero(edges)  # Find all non-zero points (text)
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    rect = frame[y:y + h, x:x + w]  # Crop the image - note we do this on the original image
    #cv2.imshow("Cropped", rect)  # Show it

    savepath = path.replace(".jpg", "Canny.jpg")
    cv2.imwrite(savepath, edges)
    #cv2.imshow("Canny", rect)
    print("Image", i, ":", savepath)

#cv2.waitKey()