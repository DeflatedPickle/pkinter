#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "LimitedEntry"
__version__ = "1.2.3"
__author__ = "DeflatedPickle"


class LimitedEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    A TTK Entry with a character limit.

            -----USAGE-----
    limitedEntry = LimitedEntry(parent, max_chars=[integer])
    limitedEntry.pack()

            -----PARAMETERS-----
    parent            = The parent of the widget.
    max_chars         = The maximum amount of characters in the Entry.

            -----CONTENTS-----
    ---VARIABLES---
    parent            = The parent of the widget.
    _max_chars        = The maximum amount of characters in the Entry.

    ---TKINTER VARIABLES---
    _variable         = The text in the Entry.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _check()          = Removes any characters over the max_chars.
    characters_left() = Returns the amount of characters left.
    """
    def __init__(self, parent, max_chars=10, *args):
        ttk.Entry.__init__(self, parent, *args)
        self.parent = parent
        self._max_chars = max_chars

        self._variable = tk.StringVar()

        self.configure(textvariable=self._variable)
        self.bind("<Key>", self._check, "+")

        self._check()

    def _check(self, event=None):
        if self._max_chars != 0:
            if len(self._variable.get()) > self._max_chars:
                self._variable.set(self._variable.get()[:-1])

    def characters_left(self):
        """Returns the characters left available in the Entry."""
        return self._max_chars - len(self._variable.get())

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    lentry = LimitedEntry(root, max_chars=10)
    lentry.pack(expand=True, padx=5, pady=5)
    var = tk.IntVar()
    var.set(lentry.characters_left())
    lentry.bind("<KeyRelease>", lambda *args: var.set(lentry.characters_left()))
    label = ttk.Label(textvariable=var)
    label.pack(expand=True, padx=5, pady=5)
    root.mainloop()
