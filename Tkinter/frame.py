# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

frame = LabelFrame(root, text="This Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Click")
b.pack()
b2 = Button(root, text="Click2")
b2.pack()


root.mainloop ()

