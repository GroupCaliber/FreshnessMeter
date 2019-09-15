"""Access IP Camera in Python OpenCV"""

import cv2

stream = cv2.VideoCapture('http://10.30.5.77:4747/mjpegfeed?720x480')



# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')  

while True:

    r, f = stream.read()
    #print(r)
    cv2.imshow('IP Camera stream',f)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()