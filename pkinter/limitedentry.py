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
    max_chars         = The maximum amount of characters in the Entry.

            -----CONTENTS-----
    ---VARIABLES---
    max_chars         = The maximum amount of characters in the Entry.
    variable          = The text in the Entry.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    check()           = Removes any characters over the max_chars.
    characters_left() = Returns the amount of characters left.
    """
    def __init__(self, parent, max_chars=10, *args):
        ttk.Entry.__init__(self, parent, *args)
        self.max_chars = max_chars

        self.variable = tk.StringVar()

        self.configure(textvariable=self.variable)
        self.bind("<Key>", self.check)

        self.check()

    def check(self, *args):
        if self.max_chars != 0:
            if len(self.variable.get()) > self.max_chars:
                self.variable.set(self.variable.get()[:-1])

    def characters_left(self):
        return self.max_chars - len(self.variable.get())

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
