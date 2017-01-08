import tkinter as tk
from tkinter import ttk

#link

__title__ = "EntryText"
__version__ = "0.1.0"
__author__ = "DeflatedPickle"

class EntryText (ttk.Entry):
    """
            -----DESCRIPTION-----
    A TTK Entry that when without user input, shows a set string of text.
    This can be used to tell the user what to put in the Entry.

            -----USAGE-----
    entryText = EntryText (parent, text = [string])
    entryText.pack ()

            -----CONTENTS-----
    ---VARIABLES---
    text     = The text shown in the entry.
    variable = The variable used for the text in the entry.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    check () = Checks value of variable.
    """
    def __init__ (self, parent, text = "Text", *args):
        ttk.Entry.__init__ (self, parent, *args)
        self.text = text

        self.variable = tk.StringVar ()

        self.configure (textvariable = self.variable)
        self.bind ("<FocusIn>", self.check)
        self.bind ("<FocusOut>", self.check)

        self.check ()

    def check (self, *args):
        if self.variable.get () == "":
            self.variable.set (self.text)
            self.configure (foreground = "grey")

        elif self.variable.get () == self.text:
            self.variable.set ("")
            self.configure (foreground = "black")

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    entrywt = EntryText (root, text = "Text")
    entrywt.grid (row = 0, column = 0)
    ttk.Button (root).grid (row = 1, column = 0)
    root.mainloop ()
