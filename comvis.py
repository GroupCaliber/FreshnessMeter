from urllib.request import urlopen
import cv2
import numpy as np

hoststr = "http://192.168.0.101:4747/mjpegfeed?640x480"
print('Streaming ' + hoststr)

stream = cv2.VideoCapture(hoststr)

while True:
    ret, frame = stream.read()
    
    cv2.imshow(hoststr, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
stream.release()
cv2.destroyAllWindows()
