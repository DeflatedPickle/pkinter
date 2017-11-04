#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ToasterBox"
__version__ = "1.1.0"
__author__ = "DeflatedPickle"


class ToasterBox(tk.Toplevel):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    template = ToasterBox(parent)

            -----PARAMETERS-----
    parent = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent = The parent of the widget.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, minus_width=5, minus_height=5, extra_height=40, *args):
        tk.Toplevel.__init__(self, parent, *args)
        self.parent = parent
        self._minus_width = minus_width
        self._minus_height = minus_height
        self._extra_height = extra_height

        self.attributes("-toolwindow", True, "-topmost", True, "-disable", True)
        self.overrideredirect(True)

        self.update()

        self.geometry("+{}+{}".format((self.winfo_screenwidth() - self.winfo_width()) - self._minus_width,
                                      (self.winfo_screenheight() - self.winfo_height()) - self._extra_height - self._minus_height))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbox = ToasterBox(root)
    root.mainloop()
