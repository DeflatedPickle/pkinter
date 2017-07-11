#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ListBook"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class ListBook(ttk.Frame):
    """
            -----DESCRIPTION-----
    A ListBox that can control shown frames.

            -----USAGE-----
    listBook = ListBook(parent)
    listBook.pack()

            -----PARAMETERS-----
    parent      = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent      = The parent of the widget.
    _frame_list = The list of added Frames.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _list_box   = The ListBox.
    frame       = The Frame that holds the shown Frame.

    ---FUNCTIONS---
    _select()   = Selects the Frame.
    add()       = Adds a new Frame.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

        self._frame_list = []

        self._list_box = tk.Listbox(self)
        self._list_box.pack(side="left", fill="y")
        self._list_box.bind("<<ListboxSelect>>", self._select)

        self.frame = ttk.Frame(self)
        self.frame.pack(side="right", fill="both", expand=True)

    def _select(self, event=None):
        for i in range(len(self._frame_list)):
            self._frame_list[i].pack_forget()

        self._frame_list[self._list_box.curselection()[0]].pack(fill="both", expand=True)

    def add(self, child=None, label=""):
        """Adds a new page to the ListBook."""
        self._frame_list.append(child)
        self._list_box.insert("end", label)

        self._list_box.focus()
        self._list_box.selection_set(0)
        self._select()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    lbook = ListBook(root)
    lbook.pack(fill="both", expand=True, padx=5, pady=5)

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
