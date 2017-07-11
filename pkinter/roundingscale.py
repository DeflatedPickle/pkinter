#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "RoundingScale"
__version__ = "1.1.5"
__author__ = "DeflatedPickle"


class RoundingScale(ttk.Scale):
    """
            -----DESCRIPTION-----
    A Scale that's value rounds when altered.

            -----USAGE-----
    roundingScale = RoundingScale(parent, from_=[integer], to=[integer])
    roundingScale.pack()

            -----PARAMETERS-----
    parent   = The parent of the widget.
    from_    = The lowest value of the Scale.
    to       = The highest value of the Scale.

            -----CONTENTS-----
    ---VARIABLES---
    parent   = The parent of the widget.
    _from_   = The lowest value of the Scale.
    _to      = The highest value of the Scale.
    _value   = The scales value.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _round() = Rounds the scales' value.
    """
    def __init__(self, parent, from_=0, to=0, *args):
        ttk.Scale.__init__(self, parent, command=self._round, from_=from_, to=to, *args)
        self.parent = parent
        self._from = from_
        self._to = to

        self._value = self.get()

    def _round(self, *args):
        """Rounds the Scale."""
        self._value = self.get()
        if int(self._value) != self._value:
            self.set(round(self._value))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    rscale = RoundingScale(root, from_=0, to=10)
    rscale.pack(expand=True, padx=5, pady=5)
    root.mainloop()
