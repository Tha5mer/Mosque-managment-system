#Thamer Almarshad
#361112464
#final project for CS492

from tkinter import *
import tkinter as tk
import sqlite3


class mosque():
    def __init__(self):
        self.conn = sqlite3.connect('mosque.db')
        self.cur = self.conn.cursor()
        # initialize Database :
        try:
            self.cur.execute("""create table mosque_records(
                    mosID_entry int PRIMARY KEY NOT NULL UNIQUE,
                    mosType_entry text,
                    coordinates_entry text,
                    name_entry text ,
                    address_entry text,
                    imam_entry text)
                """)
            self.conn.commit()
        except sqlite3.OperationalError:
            None

    def Display(self):
        conn = sqlite3.connect('mosque.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM mosque_records")
        d = cur.fetchall()
        listbox.delete(0, END)
        for x in d:
            listbox.insert(END, x)
        conn.commit()
        conn.close()

    def search(self, name_entry):
        conn = sqlite3.connect('mosque.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM mosque_records where name_entry =?" , [name_entry.get()])
        data = cur.fetchall()
        for i in data:
            listbox.insert(END, i)
        conn.commit()
        conn.close()

    def Insert(self, mosID_entry, v, coordinates_entry, name_entry, address_entry, imam_entry):
        conn = sqlite3.connect('mosque.db')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO mosque_records VALUES(:mosID_entry, :mosType_entry, :coordinates_entry,:name_entry, :address_entry, :imam_entry)",
            {
                "mosID_entry": mosID_entry.get(),
                "mosType_entry": v.get(),
                "coordinates_entry": coordinates_entry.get(),
                "name_entry": name_entry.get(),
                "address_entry": address_entry.get(),
                "imam_entry": imam_entry.get()

            })
        conn.commit()
        mosID_entry.delete(0,END)
        v.set('         Choose          ')
        coordinates_entry.delete(0,END)
        name_entry.delete(0,END)
        address_entry.delete(0,END)
        imam_entry.delete(0,END)

    def delete(self, mosID_entry):
        conn = sqlite3.connect('Mosque.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM mosque_records WHERE mosID_entry = " + mosID_entry.get())
        conn.commit()
        conn.close()

    def __del__(self):
        self.conn.close()

# GUI
root = Tk()
root.title("Mosques Management System")
# ID
mosID = Label(root, text="ID")
mosID.grid(row=1, column=0, padx=4, pady=4)
mosID_entry = Entry(root)
mosID_entry.grid(row=1, column=1)
# type
mosType = Label(root, text="Type", padx=4, pady=4)
mosType.grid(row=2, column=0)
v = StringVar(root)
v.set('         Choose          ')
mosType_entry = OptionMenu(root, v, '   مصلى عيد      ', '   مسجد حي  ', '     جامع       ')
mosType_entry.grid(row=2, column=1, padx=6, pady=6)
# Coordinates
coordinates = Label(root, text=' Coordinates ', padx=4, pady=4)
coordinates.grid(row=3, column=0)
coordinates_entry = Entry(root)
coordinates_entry.grid(row=3, column=1)
# Name
name = Label(root, text=' Name ', padx=4, pady=4)
name.grid(row=1, column=2)
name_entry = Entry(root)
name_entry.grid(row=1, column=3)
# Address
address = Label(root, text=' Address ', padx=4, pady=4)
address.grid(row=2, column=2)
address_entry = Entry(root)
address_entry.grid(row=2, column=3)
# Imam Name
imam = Label(root, text=' Imam Name ', padx=4, pady=4)
imam.grid(row=3, column=2)
imam_entry = Entry(root)
imam_entry.grid(row=3, column=3)

obj = mosque()

# Display All
displayAll = Button(root, text='Display All', command= obj.Display, padx=5, pady=5, width=15)
displayAll.grid(row=4, column=1, padx=4, pady=4)
# Add Entry
addEntry = Button(root, text='Add Entry',
                  command=lambda: obj.Insert(mosID_entry, v, coordinates_entry, name_entry, address_entry, imam_entry),
                  padx=5, pady=5, width=15)
addEntry.grid(row=5, column=1, padx=4, pady=4)
# Search By Name
search = Button(root, text='Search By Name', command=lambda: obj.search(name_entry), padx=5, pady=5, width=15)
search.grid(row=4, column=2, padx=4, pady=4)
# Delete Entry
delete = Button(root, text='Delete Entry', command=lambda: obj.delete(mosID_entry), padx=5, pady=5, width=15)
delete.grid(row=5, column=2, padx=4, pady=4)
# Update Entry
update = Button(root, text='Update Entry', padx=4, pady=4, width=15, state='disabled')
update.grid(row=4, column=3, padx=4, pady=4)
# Display on Map
map = Button(root, text='Display on Map', padx=4, pady=4, width=15, state='disabled')
map.grid(row=5, column=3, padx=4, pady=4)

# we need to create a label due to pack the scrollbar and listbox
view = LabelFrame(root, text=' Result ', padx=6, pady=8)
view.grid(row=1, column=5, rowspan=5, padx=2, pady=2)
# Scroll bar
scrollbar = Scrollbar(view)
scrollbar.pack(side=RIGHT, fill=Y)
# List box
listbox = Listbox(view, bd=0, yscrollcommand=scrollbar.set, width=60, height=13)
listbox.pack()
scrollbar.config(command=listbox.yview)

root.mainloop()
