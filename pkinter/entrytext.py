#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "EntryText"
__version__ = "1.1.4"
__author__ = "DeflatedPickle"


class EntryText(ttk.Entry):
    """
            -----DESCRIPTION-----
    A TTK Entry that when without user input, shows a set string of text.
    This can be used to tell the user what to put in the Entry.

            -----USAGE-----
    entryText = EntryText(parent, text=[string])
    entryText.pack()

            -----PARAMETERS-----
    parent    = The parent of the widget.
    text      = The text shown in the Entry.

            -----CONTENTS-----
    ---VARIABLES---
    parent    = The parent of the widget.
    _text     = The text shown in the Entry.

    ---TKINTER VARIABLES---
    _variable = The variable used for the text in the Entry.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    check()  = Checks value of variable.
    """
    def __init__(self, parent, text="Text", *args):
        ttk.Entry.__init__(self, parent, *args)
        self.parent = parent
        self._text = text

        self._variable = tk.StringVar()

        self.configure(textvariable=self._variable)
        self.bind("<FocusIn>", self.check)
        self.bind("<FocusOut>", self.check)

        self.check()

    def check(self, event=None):
        if self._variable.get() == "":
            self._variable.set(self._text)
            self.configure(foreground="grey")

        elif self._variable.get() == self._text:
            self._variable.set("")
            self.configure(foreground="black")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    entrywt = EntryText(root, text="Text")
    entrywt.pack(expand=True, side="left", padx=5, pady=5)
    ttk.Button(root).pack(expand=True, side="left")
    root.mainloop()
