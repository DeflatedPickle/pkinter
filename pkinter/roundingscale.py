import tkinter as tk
from tkinter import ttk

# link

__title__ = "RoundingScale"
__version__ = "1.1.3"
__author__ = "DeflatedPickle"


class RoundingScale(ttk.Scale):
    """
            -----DESCRIPTION-----
    A scale thats' value rounds when altered.

            -----USAGE-----
    roundingScale = RoundingScale(parent, from_=[integer], to=[integer])
    roundingScale.pack()

            -----CONTENTS-----
    ---VARIABLES---
    value    = The scales value.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    round()  = Rounds the scales' value.
    """
    def __init__(self, parent, from_=0, to=0, *args):
        ttk.Scale.__init__(self, parent, command=self.round, from_=from_, to=to, *args)
        self.value = self.get()

    def round(self, *args):
        self.value = self.get()
        if int(self.value) != self.value:
            self.set(round(self.value))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    rscale = RoundingScale(root, from_=0, to=10)
    rscale.pack(expand=True, padx=5, pady=5)
    root.mainloop()
