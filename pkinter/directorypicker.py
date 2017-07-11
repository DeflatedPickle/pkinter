#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# http://docs.wxwidgets.org/3.1/classwx_dir_picker_ctrl.html

__title__ = "DirectoryPicker"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class DirectoryPicker(ttk.Frame):
    """
            -----DESCRIPTION-----
    A widget used to pick a directory.

            -----USAGE-----
    directoryPicker = DirectoryPicker(parent)
    directoryPicker.pack()

            -----PARAMETERS-----
    parent    = The parent of the widget.
    directory = The directory the window will open at.

            -----CONTENTS-----
    ---VARIABLES---
    parent     = The parent of the widget.
    _directory = The directory the window will open at.

    ---TKINTER VARIABLES---
    _variable  = Holds the picked directory.

    ---WIDGETS---
    self
    _entry     = The Entry used to show the picked directory.
    _button    = The Button that lets the user pick a directory.

    ---FUNCTIONS---
    _browse()  = Opens the directory browser.
    get()      = Returns the value of variable.
    """
    def __init__(self, parent, directory="", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._directory = directory

        self._variable = tk.StringVar()

        self._entry = ttk.Entry(self, textvariable=self._variable)
        self._entry.pack(side="left", fill="x", expand=True)

        self._button = ttk.Button(self, text="Browse", command=self._browse)
        self._button.pack(side="right")

    def _browse(self):
        """Opens a directory browser."""
        directory = filedialog.askdirectory(initialdir=self._directory)
        self._variable.set(directory)

    def get(self):
        """Returns the chosen directory."""
        return self._variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    dpicker = DirectoryPicker(root)
    dpicker.pack(fill="x", expand=True, padx=5, pady=5)
    variable = tk.StringVar()
    label = ttk.Label(root, textvariable=variable)
    label.pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Get", command=lambda: variable.set(dpicker.get())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
