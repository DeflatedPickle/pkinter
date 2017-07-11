#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ValidEntry"
__version__ = "1.0.5"
__author__ = "DeflatedPickle"


class ValidEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    An Entry that accepts a list.
    If the text in the Entry is also in the list, it's valid and the foreground turns green.

            -----USAGE-----
    validEntry = ValidEntry(parent, valid_list=[list])
    validEntry.pack()

            -----PARAMETERS-----
    parent      = The parent of the widget.
    valid_list  = The list of valid strings.

            -----CONTENTS-----
    ---VARIABLES---
    parent      = The parent of the widget.
    _valid_list = The list of valid strings.
    _valid      = If the text is valid or not.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _check()    = Checks the text in the Entry.
    is_valid()  = Returns the variable "valid".
    """
    def __init__(self, parent, valid_list=[], *args):
        ttk.Entry.__init__(self, parent, *args)
        self.parent = parent
        self._valid_list = valid_list
        self._valid = False

        ttk.Style().configure("Valid.TEntry", foreground="green")
        ttk.Style().configure("NotValid.TEntry", foreground="red")

        self.configure(style="Valid.TEntry")
        self.bind("<KeyRelease>", self._check, "+")

    def _check(self, *args):
        """Checks the text in the Entry."""
        if self.get() in self._valid_list:
            self.configure(style="Valid.TEntry")
            self._valid = True

        elif self.get() not in self._valid_list:
            self.configure(style="NotValid.TEntry")
            self._valid = False

    def is_valid(self):
        """Returns whether or not the text is valid."""
        return self._valid

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ventry = ValidEntry(root, valid_list=["hello", "bye"])
    ventry.pack(expand=True, padx=5, pady=5)
    ventry2 = ValidEntry(root, valid_list=["yes", "no"])
    ventry2.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Check", command=lambda: print(ventry.is_valid(), ventry2.is_valid())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
