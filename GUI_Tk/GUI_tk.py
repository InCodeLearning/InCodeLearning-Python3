"""
Tkinter is the Python interface to the Tk GUI toolkit shipped with Python
LP1: create GUI application main window.
LP2: Frame
LP3: Label, Entry
LP4: Geometry Management: .pack, .grid, .place
LP5: Button
LP6: Checkbutton
LP7: Menu
"""
from tkinter import *


def cmd():
    print("clicked")

mainwd = Tk()       # create a blank window, other items shown in
mainwd.title("GUI_tkinter")   # change widget title


top = Frame(mainwd)
top.pack()
bottom = Frame(mainwd)
bottom.pack()

name = Label(bottom, text="Name")   # add a label function
passwd = Label(bottom, text="Password")
entry1 = Entry(bottom)   # used to accept single-line text strings from a user
entry2 = Entry(bottom)

name.grid(row=0, sticky=W)   # used to organize widgets in table-like structure
passwd.grid(row=1, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button1 = Button(bottom, text="Login")  # add a button
button1.grid(row=2)

c1 = Checkbutton(bottom, text="Keep me log in")
c1.grid(row=2, column=1)

menubar = Menu(mainwd)

filemenu = Menu(menubar)   # create menu bar
menubar.add_cascade(label='File', menu=filemenu)  # add File menu
filemenu.add_command(label='New', command=cmd)  # File menu content
filemenu.add_command(label='Open', command=cmd)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit)

editmenu = Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo', command=cmd)
editmenu.add_separator()
editmenu.add_command(label='Cut', command=cmd)
editmenu.add_command(label='Copy', command=cmd)
editmenu.add_command(label='Paste', command=cmd)

mainwd.config(menu=menubar)

mainwd.mainloop()    # keep the window open, or break with close button
