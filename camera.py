import numpy as np
import cv2

cap = cv2.VideoCapture('http://10.30.0.118/4747')

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()