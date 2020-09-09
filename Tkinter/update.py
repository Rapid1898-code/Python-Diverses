# from https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk ()
root.title("Blablabla Title")
root.iconbitmap ("FVCFull.ico")
root.geometry("400x400")

def edit():
    editor = Tk ()
    editor.title ("Update A Record")
    editor.iconbitmap ("FVCFull.ico")
    editor.geometry ("400x400")
    conn = sqlite3.connect ("address_book.db")
    c = conn.cursor ()


    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect ("address_book.db")
    c = conn.cursor ()

    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    conn.commit()
    conn.close()


def submit():
    # create connection
    conn = sqlite3.connect ("address_book.db")
    c = conn.cursor ()

    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                    "f_name": f_name.get(),
                    "l_name": l_name.get(),
                    "address": address.get(),
                    "city": city.get(),
                    "state": state.get(),
                    "zipcode": zipcode.get()
                  })

    conn.commit()
    conn.close()

    # delete fields
    f_name.delete(0, END)
    l_name.delete (0, END)
    address.delete (0, END)
    city.delete (0, END)
    state.delete (0, END)
    zipcode.delete (0, END)

def query():
    conn = sqlite3.connect ("address_book.db")
    c = conn.cursor ()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    conn.commit()
    conn.close()

f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
address = Entry(root,width=30)
address.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)
delete_box_label = Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0,pady=5)

submit_btn = Button(root,text="Add",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

query_btn = Button(root,text="Query",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

delete_btn = Button(root,text="Delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

edit_btn = Button(root,text="Edit Record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

root.mainloop ()

