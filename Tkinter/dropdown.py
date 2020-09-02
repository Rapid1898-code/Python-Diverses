# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")
root.geometry("400x400")

options=["Mo","Tu","We","Th","Fr"]

var = StringVar()
var.set("Mo")
drop = OptionMenu(root,var,*options)
drop.pack()

def show():
    myLab=Label(root,text=var.get()).pack()



myB = Button(root,text="Show",command=show).pack()

root.mainloop ()

