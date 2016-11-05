"""
how to create text editor.
source: http://www.newthinktank.com/2016/09/learn-program-23/
"""

from tkinter import *
import tkinter.filedialog


class TextEditor:

    def open_file(self, event=None):
        txt_file = tkinter.filedialog.askopenfilename(parent=root)

        if txt_file:
            self.text_area.delete(1.0, END)

            with open(txt_file) as f:
                self.text_area.insert(1.0, f.read())

                root.update_idletasks()

    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')

        if file is not None:
            data = self.text_area.get('1.0', END + '-1c')

            file.write(data)
            file.close()

    def __init__(self, root):

        self.text_to_write = ""

        root.title("Text Editor")

        root.geometry("600x500")

        frame = Frame(root, width=600, height=550)

        scrollbar = Scrollbar(frame)

        self.text_area = Text(frame, width=600, height=550,
                              yscrollcommand=scrollbar.set,
                              padx=10, pady=10)

        scrollbar.config(command=self.text_area.yview)

        scrollbar.pack(side=RIGHT, fill=Y)

        self.text_area.pack(side=LEFT, fill=BOTH, expand=TRUE)
        frame.pack()

        the_menu = Menu(root)

        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        file_menu.add_command(label="Exit", command=quit)

        the_menu.add_cascade(label="File", menu=file_menu)

        root.config(menu=the_menu)

root = Tk()

text_editor = TextEditor(root)

root.mainloop()
