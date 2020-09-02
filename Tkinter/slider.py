# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")
root.geometry("400x400")

vertical = Scale(root,from_=0,to=200)
vertical.pack()

horizontal = Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizontal.pack()



root.mainloop ()

