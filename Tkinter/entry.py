# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def myclick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton4 = Button(root,text="Enter Your Name",command=myclick)
myButton4.pack()

root.mainloop()
