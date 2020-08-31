# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")

MODES = [
    ("Pepperoni","Pe"),
    ("Cheese", "Ch"),
    ("Mushroom", "Mu"),
    ("Onion", "On")
]

pizza = StringVar()
pizza.set("Pe")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label (root, text=value).pack()


myLabel = Label(root, text=pizza.get())

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop ()

