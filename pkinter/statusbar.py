import tkinter as tk
from tkinter import ttk

# link

__title__ = "Statusbar"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class Statusbar(ttk.Frame):
    """
            -----DESCRIPTION-----
    The Statusbar can be used to show certain variables.

            -----USAGE-----
    statusbar = Statusbar(parent)
    statusbar.pack()
    statusbar.add_label(text=[string], textvariable=[string], image=[string], side=[string])
    statusbar.add_separator()

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    add_label()      = Adds a label to the statusbar.
    add_separator()  = Adds a separator to the statusbar.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)

    def add_label(self, text="", textvariable="", image="", side="left"):
        ttk.Label(self, text=text, textvariable=textvariable, image=image).pack(side=side)

    def add_sizegrip(self, side="left"):
        ttk.Sizegrip(self).pack(side=side)

    def add_separator(self):
        ttk.Separator(self, orient="vertical").pack(side="left", fill="y", padx=3, pady=1)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    sbar = Statusbar(root)
    sbar.pack(expand=True, fill="x", padx=5, pady=5)
    sbar.add_label(text="A Label")
    sbar.add_separator()
    sbar.add_sizegrip(side="right")
    root.mainloop()
