# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

def open():
    global img
    top = Toplevel ()
    top.title ("top Title")
    Label (top, text="Hello!").pack()
    img = ImageTk.PhotoImage(Image.open("demo.png"))
    Label (top, image=img).pack()

btn = Button(root, text="2nd Window", command=open).pack()

mainloop ()

