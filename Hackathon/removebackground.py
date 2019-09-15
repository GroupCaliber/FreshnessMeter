import cv2
import matplotlib.pyplot as plt
import numpy as np

for k in range(1, 20+1):
    img = cv2.imread("res/"+str(k)+".jpg")
    #img = cv2.addWeighted(img, 0, img, 0, 0)

    redvals = []
    greenvals = []
    bluevals = []

    gh = []

    miny = 0
    maxy = 0
    minx = 0
    maxx = 0

    xthresh = 1.02
    ythresh = 1.0

    for i in range(0, img.shape[0]):
        r = np.average(img[i, :, 2])
        g = np.average(img[i, :, 1])
        b = np.average(img[i, :, 0])
        h=(b+g)/2
        h=r/h

        if h < ythresh:# and miny < 0:
            #miny = i
            h=0
        else:
            h=1
        gh.append(h)

    miny = gh.index(1)
    maxy = img.shape[0]-gh[::-1].index(1)

    #plt.plot(gh,"k")
    #plt.show()

    gh=[]

    for i in range(0, img.shape[1]):
        r = np.average(img[:, i, 2])
        g = np.average(img[:, i, 1])
        b = np.average(img[:, i, 0])
        h=(b+g)/2
        h=r/h

        if h < xthresh:# and miny < 0:
            #miny = i
            h=0
        else:
            h=1
        gh.append(h)

    minx = gh.index(1)
    maxx = img.shape[1]-gh[::-1].index(1)

   # print(miny,maxy,minx,maxx)
    #plt.plot(redvals,'r')
    #plt.plot(greenvals,"g")
    #plt.plot(bluevals,"b")

    #plt.plot(gh,"k")
    #plt.show()

    rect = img[miny:maxy, minx:maxx]

    #cv2.imshow("asdfgh", rect)
    cv2.imwrite("res\out"+str(k)+".jpg", rect)
    print("Writing image", k)
    #cv2.waitKey()