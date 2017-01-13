import tkinter as tk
from tkinter import ttk

#link

__title__ = "LimitedEntry"
__version__ = "1.1.1"
__author__ = "DeflatedPickle"

class LimitedEntry (ttk.Entry):
    """
            -----DESCRIPTION-----
    A TTK Entry with a character limit.

            -----USAGE-----
    limitedEntry = LimitedEntry (parent, maxchars = [integer])
    limitedEntry.pack ()

            -----CONTENTS-----
    ---VARIABLES---
    maxchars = The maximum amount of characters in the Entry.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    check () = Removes any characters over the maxchars.
    """
    def __init__ (self, parent, maxchars = 10, *args):
        ttk.Entry.__init__ (self, parent, *args)
        self.maxchars = maxchars

        self.variable = tk.StringVar ()

        self.configure (textvariable = self.variable)
        self.bind ("<Key>", self.check)

        self.check ()

    def check (self, *args):
        if self.maxchars != 0:
            if len (self.variable.get ()) >= self.maxchars:
                self.variable.set (self.variable.get () [:-1])

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    lentry = LimitedEntry (root, maxchars = 10)
    lentry.pack (expand = True, padx = 5, pady = 5)
    root.mainloop ()
