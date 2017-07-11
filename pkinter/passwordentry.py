#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "PasswordEntry"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class PasswordEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    The PasswordEntry hides the typed text behind a given character.

            -----USAGE-----
    passwordEntry = PasswordEntry(parent, cover_character=[string])
    passwordEntry.pack()

            -----PARAMETERS-----
    parent          = The parent of the widget.
    cover_character = The character used to replace text.

            -----CONTENTS-----
    ---VARIABLES---
    parent          = The parent of the widget.
    _cover_character = The character used to replace text.
    _entry_text      = The actual text of the Entry.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _update_text()   = Replaces characters with covers.
    get_text()     = Gets the actual text of the Entry.
    _delete_last()  = Deletes the last item in the list of characters.
    """
    def __init__(self, parent, cover_character="*", *args):
        ttk.Entry.__init__(self, parent, *args)
        self.parent = parent
        self._cover_character = cover_character

        self._entry_text = []

        self.bind("<KeyRelease>", self._update_text, "+")
        self.bind("<BackSpace>", self._delete_last, "+")

    def _update_text(self, *args):
        for i in self.get():
            if i == "":
                pass

            elif i != self._cover_character:
                self._entry_text.append(i)

        self.delete(0, "end")

        for i in range(len(self._entry_text)):
            self.insert("end", self._cover_character)

    def _delete_last(self, event=None):
        try:
            self._entry_text.pop()

        except IndexError:
            pass

    def get_text(self):
        """Gets the actual text of the Entry."""
        return "".join(self._entry_text)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    pentry = PasswordEntry(root)
    pentry.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Get", command=lambda: print(pentry.get_text())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
