#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "EntrySpinner"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class EntrySpinbox(ttk.Spinbox):
    """
            -----DESCRIPTION-----
    A TTK Spinbox that when without user input, shows a set string of text.
    This can be used to tell the user what to put in the Spinbox.

            -----USAGE-----
    entrySpinbox = EntrySpinbox(parent, text=[string])
    entrySpinbox.pack()

            -----PARAMETERS-----
    parent    = The parent of the widget.
    text      = The text shown in the Entry.

            -----CONTENTS-----
    ---VARIABLES---
    parent    = The parent of the widget.
    _text     = The text shown in the Spinbox.

    ---TKINTER VARIABLES---
    _variable = The variable used for the text in the Spinbox.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    check()  = Checks value of variable.
    """
    def __init__(self, parent, text="1", from_=0.0, to=0.0, increment=1.0, wrap=False, format_="%0.0f", **kwargs):
        ttk.Spinbox.__init__(self, parent, from_=from_, to=to, increment=increment, wrap=wrap, format=format_, **kwargs)
        self.parent = parent
        self._text = text

        self._variable = tk.DoubleVar()
        self._variable.set(format_ % float(self._text))

        self.configure(textvariable=self._variable)
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        self.focus_in()
        self.focus_out()

    def focus_in(self, event=None):
        if self.get() == self._text:
            self.set("")

        else:
            self.configure(foreground="black")

    def focus_out(self, event=None):
        if self.get() == "" or self.get() == self._text:
            self.set(self._text)
            self.configure(foreground="grey")

        else:
            self.configure(foreground="black")


##################################################

if __name__ == "__main__":
    root = tk.Tk()
    entrywt = EntrySpinbox(root)
    entrywt.pack(expand=True, side="left", padx=5, pady=5)
    ttk.Button(root).pack(expand=True, side="left")
    root.mainloop()
