# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root, text="Look i clicked a button!")
    myLabel.pack()

myButton1 = Button(root,text="Click me!")
myButton2 = Button(root,text="Click me!",state=DISABLED)
myButton3 = Button(root,text="C", padx=50, pady=50 )
myButton4 = Button(root,text="Text",command=myclick)
myButton5 = Button(root,text="col",bg="blue",fg="white")
myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()

root.mainloop()
