import numpy as np
import cv2 as cv
from PIL import ImageTk, Image
import guihelper

import tkinter as tk

# global parameters ---------------------------------------------
wnd_width = 960
wnd_height = 680
default_input_image_path = "..\Hackathon\Adwnsz.jpg"

# input image bounding box size
input_image_width = 300
input_image_height = 300

canny_image_width = 300
canny_image_height = 300

spacing = 10
# ---------------------------------------------------------------

class Caliber(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)

    def loadimage(self, path=default_input_image_path):
        self.img = Image.open(path)
        self.imgarr = cv.imread(path)
        self.asp_rat = self.img.width/self.img.height

    def cropimage2(self):
        gray = cv.cvtColor(self.imgarr, cv.COLOR_BGR2GRAY) # convert to grayscale
        # threshold to get just the signature (INVERTED)
        retval, thresh_gray = cv.threshold(gray, thresh=200, maxval=255, type=cv.THRESH_BINARY_INV)

        contours, hierarchy = cv.findContours(thresh_gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

        # Find object with the biggest bounding box
        mx = (0,0,0,0)      # biggest bounding box so far
        mx_area = 0
        for cont in contours:
            x,y,w,h = cv.boundingRect(cont)
            area = w*h
            if area > mx_area:
                mx = x,y,w,h
                mx_area = area
        x,y,w,h = mx

        # Output to files
        roi=self.imgarr[y:y+h,x:x+w]
        cv.imshow('Image_crop.jpg', roi)
        cv.waitKey()

        #cv.rectangle(self.imgarr,(x,y),(x+w,y+h),(200,0,0),2)
        #cv.imwrite('Image_cont.jpg', img)

    def cropimage(self):
        sum_array = []

        miny = 0
        maxy = 0
        minx = 0
        maxx = 0

        xthresh = 1.0
        ythresh = 1.0

        for i in range(0, self.imgarr.shape[0]):
            r = np.average(self.imgarr[i, :, 2])
            g = np.average(self.imgarr[i, :, 1])
            b = np.average(self.imgarr[i, :, 0])
            h=(b+g)/2
            h=r/h

            if h < ythresh:
                h=0
            else:
                h=1

            sum_array.append(h)

        miny = sum_array.index(1)
        maxy = self.imgarr.shape[0]-sum_array[::-1].index(1)

        sum_array=[]

        for i in range(0, self.imgarr.shape[1]):
            r = np.average(self.imgarr[:, i, 2])
            g = np.average(self.imgarr[:, i, 1])
            b = np.average(self.imgarr[:, i, 0])
            h=(b+g)/2
            h=r/h

            if h < xthresh:
                h=0
            else:
                h=1

            sum_array.append(h)

        minx = sum_array.index(1)
        maxx = self.imgarr.shape[1]-sum_array[::-1].index(1)

        rect = self.imgarr[miny:maxy, minx:maxx]

        self.imgarr = rect
        self.img = Image.fromarray(cv.cvtColor(rect, cv.COLOR_BGR2RGB))

        return True

    def loadimagefromcam(self, ip_add):
        # e.g. ip_add = 10.30.0.118:4747
        cap = cv.VideoCapture('http://' + ip_add + '/mjpegfeed?640x480')

        while(True):
            if (cap.isOpened() == False):
                print("Error opening video stream or file")

            # Read the video
            while (cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                if ret == True:

                    fgbg = cv.createBackgroundSubtractorMOG2(
                        history=10,
                        varThreshold=2,
                        detectShadows=False)

                    # Converting the image to grayscale.
                    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                    # Extract the foreground
                    edges_foreground = cv.bilateralFilter(gray, 9, 75, 75)
                    foreground = fgbg.apply(edges_foreground)

                    # Smooth out to get the moving area
                    kernel = np.ones((50, 50), np.uint8)
                    foreground = cv.morphologyEx(foreground, cv.MORPH_CLOSE, kernel)

                    # Applying static edge extraction
                    edges_foreground = cv.bilateralFilter(gray, 9, 75, 75)
                    edges_filtered = cv.Canny(edges_foreground, 60, 120)

                    # Crop off the edges out of the moving area
                    cropped = (foreground // 255) * edges_filtered

                    # Stacking the images to print them together for comparison
                    images = np.hstack((gray, edges_filtered, cropped))
                    cv.imshow('Frame', cropped)
                    # Press Q on keyboard to  exit
                    if cv.waitKey(25) & 0xFF == ord('q'):
                        break

                # Break the loop
                else:
                    break

                # When everything done, release the video capture object
                cap.release()

                # Closes all the frames
                cv.destroyAllWindows()

    def getcannyimage(self):
        frame = np.asarray(self.img)
        #ret, frame = cap.read()
        fgbg = cv.createBackgroundSubtractorMOG2(history=10, varThreshold=2, detectShadows=False)

        # Converting the image to grayscale.
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Extract the foreground
        edges_foreground = cv.bilateralFilter(gray, 9, 75, 75)
        foreground = fgbg.apply(edges_foreground)

        # Smooth out to get the moving area
        kernel = np.ones((50, 50), np.uint8)
        foreground = cv.morphologyEx(foreground, cv.MORPH_CLOSE, kernel)

        # Applying static edge extraction
        edges_foreground = cv.bilateralFilter(gray, 9, 75, 75)
        edges_filtered = cv.Canny(edges_foreground, 60, 120)

        # Crop off the edges out of the moving area
        cropped = (foreground // 255) * edges_filtered

        return cropped

    def placeimage(self, img_arr, pos, box_sz, caption):
        i_w = img_arr.shape[1]
        i_h = img_arr.shape[0]
        w = box_sz[0]
        h = box_sz[1]

        r = i_w/i_h

        if r >= 1:
            i_w = min(w, i_w)
            i_h = int(i_w / r)
        else:
            i_h = min(h, i_h)
            i_w = int(i_h * r)

        tmpimg = Image.fromarray(cv.cvtColor(img_arr, cv.COLOR_BGR2RGB)).resize((i_w, i_h), Image.ANTIALIAS)
        tkimg = ImageTk.PhotoImage(tmpimg)

        panel = tk.Label(self, image=tkimg)
        panel.image = tkimg
        caption = tk.Label(self, text=caption)
        print(r)
        if r >= 1:
            panel.place(width=i_w, height=i_h, x=pos[0], y=pos[1]+int((h-i_h)/2))
        else:
            panel.place(width=i_w, height=i_h, x=pos[0]+int((w-i_w)/2), y=pos[1])
        
        caption.place(x=pos[0], y=h+pos[1], w=w, h=20)

    def placeinputimage(self, path=default_input_image_path):
        self.placeimage(self.imgarr, [spacing, spacing], [input_image_width, input_image_height], "Input image")

    def placecannyimage(self):
        canny_image = self.getcannyimage()
        
        self.placeimage(canny_image, [input_image_width + 2*spacing, spacing], [canny_image_width, canny_image_height], "Canny operator")

    

#photo = ImageTk.PhotoImage(image)
#w1 = tk.Label(root, image=photo).pack(side="right",expand=True)

main_wnd = tk.Tk() # Window object
app = Caliber(main_wnd) # app object
app.loadimage(path="..\Hackathon\Gdwnsz.jpg") # load the image
app.cropimage()
#app.cropimage2()

main_wnd.title("Caliber") # set the window title
guihelper.center_window(main_wnd, wnd_width, wnd_height) # center the window

app.placeinputimage()
app.placecannyimage()

main_wnd.mainloop()