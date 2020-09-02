# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

root.filename = filedialog.askopenfilename(
    initialdir="/Users/Polzi/Documents/GitHub/Python-Diverses/Tkinter",
    title="Select file",
    filetypes=(("png files", "*.png"),("all files", "*.*"))
)
my_label = Label(root, text=root.filename).pack()

root.mainloop ()

