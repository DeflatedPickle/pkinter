#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# http://docs.wxwidgets.org/3.1/classwx_choicebook.html

__title__ = "ChoiceBook"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class ChoiceBook(ttk.Frame):
    """
            -----DESCRIPTION-----
    The ChoiceBook allows for navigation through added frames by using a Combobox.

            -----USAGE-----
    choiceBook = ChoiceBook(parent)
    choiceBook.pack()

    frame = ttk.Frame(choiceBook.frame)
    choiceBook.add(child=frame, label="Frame")

            -----PARAMETERS-----
    combobox_position  = The position of the Combobox.

            -----CONTENTS-----
    ---VARIABLES---
    parent             = The parent of the widget.
    _combobox_position = The position of the Combobox.
    _page_list         = A list of the pages.
    _label_list        = A list of the labels.

    ---TKINTER VARIABLES---
    _variable          = The current page of the widget.

    ---WIDGETS---
    self
    _combobox          = The Combobox used to change page.
    frame              = Holds the currently shown Frame.

    ---FUNCTIONS---
    _change_page()     = Changes the page to the selected one.
    add()              = Adds a new page to the widget.
    """
    def __init__(self, parent, combobox_position="top", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._combobox_position = combobox_position

        self._page_list = []
        self._label_list = []

        self._variable = tk.StringVar()

        self._combobox = ttk.Combobox(self, state="readonly", textvariable=self._variable)
        self._combobox.pack(side=combobox_position, fill="x")
        self._combobox.bind("<<ComboboxSelected>>", self._change_page, "+")

        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True)

    def _change_page(self, event=None):
        for i in range(len(self._page_list)):
            self._page_list[i].pack_forget()

        self._page_list[self._label_list.index(self._variable.get())].pack(fill="both", expand=True)

    def add(self, child=None, label=""):
        """Adds a new page to the ChoiceBook."""
        self._page_list.append(child)
        self._label_list.append(label)
        self._variable.set(self._label_list[0])
        self._combobox.configure(values=self._label_list)

        self._change_page()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    cbook = ChoiceBook(root)
    cbook.pack(expand=True, padx=5, pady=5)

    frame1 = ttk.Frame(cbook.frame)
    for i in range(3):
        ttk.Button(frame1, text=i).pack(side="left")
    frame2 = ttk.Frame(cbook.frame)
    ttk.Checkbutton(frame2, text="Checkbutton").pack()
    frame3 = ttk.Frame(cbook.frame)
    ttk.Label(frame3, text="Frame 3").pack(side="bottom")

    cbook.add(child=frame1, label="Frame1")
    cbook.add(child=frame2, label="Frame2")
    cbook.add(child=frame3, label="Frame3")
    root.mainloop()
