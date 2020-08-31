# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    # messagebox.showinfo("Title of PopUp", "Hello World!")
    response = messagebox.askquestion ("Title of PopUp", "Hello World!")
    if response == 1:
        Label(root, text= "You clicked YES").pack()
    else:
        Label(root, text= "You clicked NO").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop ()

