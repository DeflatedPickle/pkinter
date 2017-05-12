#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "RoundingScale"
__version__ = "1.1.4"
__author__ = "DeflatedPickle"


class RoundingScale(ttk.Scale):
    """
            -----DESCRIPTION-----
    A Scale that's value rounds when altered.

            -----USAGE-----
    roundingScale = RoundingScale(parent, from_=[integer], to=[integer])
    roundingScale.pack()

            -----PARAMETERS-----
    from_    = The lowest value of the Scale.
    to       = The highest value of the Scale.

            -----CONTENTS-----
    ---VARIABLES---
    value    = The scales value.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    round()  = Rounds the scales' value.
    """
    def __init__(self, parent, from_=0, to=0, *args):
        ttk.Scale.__init__(self, parent, command=self.round, from_=from_, to=to, *args)
        self.value = self.get()

    def round(self, *args):
        """Rounds the Scale."""
        self.value = self.get()
        if int(self.value) != self.value:
            self.set(round(self.value))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    rscale = RoundingScale(root, from_=0, to=10)
    rscale.pack(expand=True, padx=5, pady=5)
    root.mainloop()
