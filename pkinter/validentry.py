import tkinter as tk
from tkinter import ttk

# link

__title__ = "ValidEntry"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class ValidEntry(ttk.Entry):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__(self, parent, list=[], *args):
        ttk.Entry.__init__(self, parent, *args)
        self.list = list

        self.style = ttk.Style()
        self.style.configure("Valid.TEntry")
        self.configure(style="Valid.TEntry")

        self.bind("<KeyRelease>", self.check)

    def check(self, *args):
        if self.get() in self.list:
            print("Valid")
            self.style.configure("Valid.TEntry", background="green")

        elif self.get() not in self.list:
            print("Invalid")
            self.style.configure("Valid.TEntry", background="red")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ventry = ValidEntry(root, list=["hello", "bye"])
    ventry.pack(expand=True, padx=5, pady=5)
    root.mainloop()
