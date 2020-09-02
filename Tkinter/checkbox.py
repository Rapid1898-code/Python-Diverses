# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")
root.geometry("400x400")

def show():
    myLabel = Label (root, text=var.get ()).pack ()

var = IntVar()
c = Checkbutton(root,text="Check1",variable=var)
c.select()
c.deselect()
c.pack()

myButton = Button(root,text="Show",command=show).pack()

root.mainloop ()

