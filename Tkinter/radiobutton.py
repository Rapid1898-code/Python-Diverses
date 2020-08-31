# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label (root, text=value).pack()

Radiobutton(root, text="Opt1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Opt2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get()).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop ()

