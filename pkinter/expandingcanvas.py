#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
# from tkinter import ttk

# link

__title__ = "ExpandingCanvas"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class ExpandingCanvas(tk.Canvas):
    """
            -----DESCRIPTION-----
    A Canvas that expands to its parent.

            -----USAGE-----
    expandingCanvas = ExpandingCanvas(parent)
    expandingCanvas.pack()

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
    _on_resize
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.bind("<Configure>", self._on_resize)

    def _on_resize(self, event=None):
        self.configure(width=self.parent.winfo_width(), height=self.parent.winfo_height())

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    ecanvas = ExpandingCanvas(root)
    ecanvas.pack(expand=True, padx=5, pady=5)
    root.mainloop()
