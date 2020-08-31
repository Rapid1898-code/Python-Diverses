# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Blablabla Title")
root.iconbitmap("FVCFull.ico")

my_img = ImageTk.PhotoImage(Image.open("demo.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

status = Label(root, text="Status")

root.mainloop()
