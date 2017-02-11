import tkinter as tk
from tkinter import ttk

# link

__title__ = "ListBook"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class ListBook(ttk.Frame):
    """
            -----DESCRIPTION-----
    A ListBox that can control shown frames.

            -----USAGE-----
    listBook = ListBook(parent)
    listBook.pack()

            -----PARAMETERS-----
    parent

            -----CONTENTS-----
    ---VARIABLES---
    frame_list = The list of added Frames.

    ---WIDGETS---
    self
    list_box   = The ListBox.
    frame      = The Frame that holds the shown Frame.

    ---FUNCTIONS---
    select()   = Selects the Frame.
    add()      = Adds a new Frame.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)

        self.frame_list = []

        self.list_box = tk.Listbox(self)
        self.list_box.pack(side="left", fill="y")
        self.list_box.bind("<<ListboxSelect>>", self.select)

        self.frame = ttk.Frame(self)
        self.frame.pack(side="right", fill="both", expand=True)

    def select(self, *args):
        for i in range(len(self.frame_list)):
            self.frame_list[i].pack_forget()

        self.frame_list[self.list_box.curselection()[0]].pack(fill="both", expand=True)

    def add(self, child=None, label=""):
        """
        Adds a new page to the ListBook.
        """
        self.frame_list.append(child)
        self.list_box.insert("end", label)

        self.list_box.focus()
        self.list_box.selection_set(0)
        self.select()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    lbook = ListBook(root)
    lbook.pack(fill = "both", expand=True, padx=5, pady=5)

    frame1 = ttk.Frame(lbook.frame)
    for i in range(3):
        ttk.Button(frame1, text=i).pack(side="left")
    frame2 = ttk.Frame(lbook.frame)
    ttk.Checkbutton(frame2, text="Checkbutton").pack()
    frame3 = ttk.Frame(lbook.frame)
    ttk.Label(frame3, text="Frame 3").pack(side="bottom")

    lbook.add(child=frame1, label="Frame1")
    lbook.add(child=frame2, label="Frame2")
    lbook.add(child=frame3, label="Frame3")
    root.mainloop()
