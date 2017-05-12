import tkinter as tk
from tkinter import ttk

# link

__title__ = "ValidEntry"
__version__ = "1.0.3"
__author__ = "DeflatedPickle"


class ValidEntry(ttk.Entry):
    """
            -----DESCRIPTION-----
    An Entry that accepts a list.
    If the text in the Entry is also in the list, it's valid and the foreground turns green.

            -----USAGE-----
    validEntry = ValidEntry(parent, valid_list=[list])
    validEntry.pack()

            -----PARAMETERS-----
    parent
    valid_list = The list of valid strings.

            -----CONTENTS-----
    ---VARIABLES---
    valid_list = The list of valid strings.
    valid      = If the text is valid or not.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    check()    = Checks the text in the Entry.
    is_valid() = Returns the variable "valid".
    """
    def __init__(self, parent, valid_list=[], *args):
        style = ttk.Style()
        style.configure("Valid.TEntry", foreground="green")
        style.configure("Invalid.TEntry", foreground="red")

        ttk.Entry.__init__(self, parent, *args)
        self.valid_list = valid_list
        self.valid = False

        self.configure(style="Valid.TEntry")

        self.bind("<KeyRelease>", self.check)

    def check(self, *args):
        if self.get() in self.valid_list:
            self.configure(style="Valid.TEntry")
            self.valid = True

        else:
            self.configure(style="Invalid.TEntry")
            self.valid = False

    def is_valid(self):
        """
        Returns whether or not the text is valid.
        """
        return self.valid

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ventry = ValidEntry(root, valid_list=["hello", "bye"])
    ventry.pack(expand=True, padx=5, pady=5)
    ventry2 = ValidEntry(root, valid_list=["hello", "see"])
    ventry2.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Check", command=lambda: print(ventry.is_valid(), ventry2.is_valid())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
