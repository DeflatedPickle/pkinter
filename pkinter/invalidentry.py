#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "InvalidEntry"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class InvalidEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    An Entry that accepts a list.
    If the text in the Entry is also in the list, it's invalid and the foreground turns red.

            -----USAGE-----
    invalidEntry = InvalidEntry(parent, invalid_list=[list])
    invalidEntry.pack()

            -----PARAMETERS-----
    invalid_list = The list of invalid strings.

            -----CONTENTS-----
    ---VARIABLES---
    invalid_list = The list of invalid strings.
    invalid      = If the text is valid or not.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    check()    = Checks the text in the Entry.
    is_invalid() = Returns the variable "invalid".
    """
    def __init__(self, parent, invalid_list=[], *args):
        ttk.Entry.__init__(self, parent, *args)
        self.invalid_list = invalid_list
        self.invalid = False

        self.style = ttk.Style()
        self.style.configure("Invalid.TEntry", foreground="red")
        self.style.configure("NotInvalid.TEntry", foreground="green")

        self.configure(style="Invalid.TEntry")
        self.bind("<KeyRelease>", self.check)

    def check(self, *args):
        if self.get() in self.invalid_list:
            self.configure(style="Invalid.TEntry")
            self.invalid = True

        elif self.get() not in self.invalid_list:
            self.configure(style="NotInvalid.TEntry")
            self.invalid = False

    def is_invalid(self):
        """Returns whether or not the text is invalid."""
        return self.invalid

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ientry = InvalidEntry(root, invalid_list=["hello", "bye"])
    ientry.pack(expand=True, padx=5, pady=5)
    ientry2 = InvalidEntry(root, invalid_list=["yes", "no"])
    ientry2.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Check", command=lambda: print(ientry.is_invalid(), ientry2.is_invalid())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
