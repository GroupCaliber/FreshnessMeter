from tkinter import *

# pip install pillow
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)


        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

load = Image.open("res/tomatoes.jpg")
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("1080x720")
root.mainloop()