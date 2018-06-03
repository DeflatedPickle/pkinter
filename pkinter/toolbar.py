#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "Toolbar"
__version__ = "1.2.1"
__author__ = "DeflatedPickle"


class Toolbar(ttk.Frame):
    """
            -----DESCRIPTION-----
    The Toolbar can be used to add an ease of using commands.

            -----USAGE-----
    toolbar = Toolbar(parent)
    toolbar.pack()
    toolbar.add_button(text=[string], image=[string], side=[string])
    toolbar.add_checkbutton(text=[string], image=[string], variable=[variable], side=[left])
    toolbar.add_radiobutton(text=[string], image=[string], value=[integer], side=[string])
    toolbar.add_separator()

            -----PARAMETERS-----
    parent            = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent            = The parent of the widget.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    add_button()      = Adds a button to the toolbar.
    add_checkbutton() = Adds a checkbutton to the toolbar.
    add_radiobutton() = Adds a radiobutton to the toolbar.
    add_separator()   = Adds a separator to the toolbar.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

    def add_button(self, side="left", **kwargs):
        """Adds a Button to the Toolbar."""
        widget = ttk.Button(self, **kwargs, style="Toolbutton")
        widget.pack(side=side)

        return widget

    def add_checkbutton(self, side="left", **kwargs):
        """Adds a CheckButton to the Toolbar."""
        widget = ttk.Checkbutton(self, **kwargs, style="Toolbutton")
        widget.pack(side=side)

        return widget

    def add_radiobutton(self, side="left", **kwargs):
        """Adds a RadioButton to the Toolbar."""
        widget = ttk.Radiobutton(self, **kwargs, style="Toolbutton")
        widget.pack(side=side)


        return widget

    def add_separator(self, orient="vertical", side="left"):
        """Adds a Separator to the Toolbar."""
        widget = ttk.Separator(self, orient=orient)
        widget.pack(side=side, fill="y" if orient == "vertical" else "x", padx=3, pady=1)

        return widget

    def add_combobox(self, side="left", **kwargs):
        widget = ttk.Combobox(self, **kwargs)
        widget.pack(side=side)

        return widget


##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbar = Toolbar(root)
    tbar.pack(expand=True, fill="x", padx=5, pady=5)
    tbar.add_button(text="A Button", command=lambda: print("User pressed the button."))
    variable1 = tk.IntVar()
    variable2 = tk.IntVar()
    tbar.add_checkbutton(text="Check", variable=variable1)
    tbar.add_checkbutton(text="Check", variable=variable2)
    tbar.add_separator()
    variable3 = tk.IntVar()
    tbar.add_radiobutton(text="One", variable=variable3, value=0)
    tbar.add_radiobutton(text="Two", variable=variable3, value=1)
    tbar.add_radiobutton(text="Three", variable=variable3, value=2)
    tbar.add_separator()
    tbar.add_combobox(values=["Item 1", "Item 2", "Item 3"])
    tbar.add_separator()
    tbar.add_button(text="Right", side="right")
    root.mainloop()
