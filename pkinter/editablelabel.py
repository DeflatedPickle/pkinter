#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "EditableLabel"
__version__ = "1.1.4"
__author__ = "DeflatedPickle"


class EditableLabel(ttk.Label):
    """
            -----DESCRIPTION-----
    A label that you can edit the text of.

            -----USAGE-----
    editableLabel = EditableLabel(parent, text=[string], does_resize=[boolean])
    editableLabel.pack()

            -----PARAMETERS-----
    parent      = The parent of the widget.
    text        = The text of the Label starts with.
    does_resize = Determines whether the Entry resizes with to the text.

            -----CONTENTS-----
    ---VARIABLES---
    parent      = The parent of the widget.
    _text       = The text of the Label starts with.

    ---TKINTER VARIABLES---
    _variable   = The text inside of the Entry.

    ---WIDGETS---
    self
    _entry      = The Entry widget.

    ---FUNCTIONS---
    _edit()     = Opens the Entry.
    _confirm()  = Closes the Entry.
    _resize()   = Resizes the Entry to the text inside.
    get()       = Returns the text of the Label.
    """
    def __init__(self, parent, text="Edit", does_resize=False, *args):
        ttk.Label.__init__(self, parent, *args)
        self.parent = parent
        self._text = text

        self._variable = tk.StringVar()
        self.configure(textvariable=self._variable)
        self._variable.set(self._text)

        self._entry = ttk.Entry(self, textvariable=self._variable)

        self.bind("<Double-Button-1>", self._edit, "+")
        self.bind("<Enter>", lambda: self.configure(cursor="hand2"), "+")
        self._entry.bind("<FocusOut>", self._confirm, "+")
        self._entry.bind("<Return>", self._confirm, "+")

        if does_resize:
            self._entry.bind("<Key>", self._resize)
            self._resize()

        self.configure(width=self._entry.cget("width"))

    def _edit(self, event=None):
        """Allows the Label to be edited."""
        self._entry.pack(fill="both")
        self._entry.focus_set()
        self._entry.icursor("end")

    def _confirm(self, event=None):
        """Stops the Label from being edited."""
        self._entry.pack_forget()
        self.configure(width=self._entry.cget("width"))

    def _resize(self, event=None):
        """Resizes the Entry to the text inside."""
        self._entry.configure(width=len(str(self._variable.get())) + 1)

    def get(self):
        """Returns the text of the Label."""
        return self._variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    elabel = EditableLabel(root, does_resize=False)
    elabel.pack(expand=True, padx=5, pady=5)
    root.mainloop()
