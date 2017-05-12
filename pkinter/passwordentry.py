#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "PasswordEntry"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class PasswordEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    The PasswordEntry hides the typed text behind a given character.

            -----USAGE-----
    passwordEntry = PasswordEntry(parent, cover_character=[string])
    passwordEntry.pack()

            -----PARAMETERS-----
    cover_character = The character used to replace text.

            -----CONTENTS-----
    ---VARIABLES---
    cover_character = The character used to replace text.
    entry_text      = The actual text of the Entry.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    update_text()   = Replaces characters with covers.
    get_text()      = Gets the actual text of the Entry.
    delete_last()   = Deletes the last item in the list of characters.
    """
    def __init__(self, parent, cover_character="*", *args):
        ttk.Entry.__init__(self, parent, *args)
        self.cover_character = cover_character

        self.entry_text = []

        self.bind("<KeyRelease>", self.update_text)
        self.bind("<BackSpace>", self.delete_last)

    def update_text(self, *args):
        for i in self.get():
            if i == "":
                pass

            elif i != self.cover_character:
                self.entry_text.append(i)

        self.delete(0, "end")

        for i in range(len(self.entry_text)):
            self.insert("end", self.cover_character)

    def delete_last(self, *args):
        try:
            self.entry_text.pop()

        except IndexError:
            pass

    def get_text(self):
        """Gets the actual text of the Entry."""
        return "".join(self.entry_text)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    pentry = PasswordEntry(root)
    pentry.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Get", command=lambda: print(pentry.get_text())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
