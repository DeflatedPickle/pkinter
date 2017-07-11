#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# http://docs.wxwidgets.org/3.1/classwx_file_picker_ctrl.html

__title__ = "FilePicker"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class FilePicker(ttk.Frame):
    """
            -----DESCRIPTION-----
    A widget used to pick a file.

            -----USAGE-----
    filePicker = FilePicker(parent)
    filePicker.pack()

            -----PARAMETERS-----
    parent     = The parent of the widget.
    filetypes  = The types of files the user can select.
    directory  = The directory the window will open at.

            -----CONTENTS-----
    ---VARIABLES---
    parent     = The parent of the widget.
    _filetypes = The types of files the user can select.
    _directory = The directory the window will open at.

    ---TKINTER VARIABLES---
    _variable  = Holds the picked file.

    ---WIDGETS---
    self
    _entry     = The Entry used to show the picked file.
    _button    = The Button that lets the user pick a file.

    ---FUNCTIONS---
    _browse()  = Opens the file browser.
    get()      = Returns the value of variable.
    """
    def __init__(self, parent, filetypes=(("All Files", "*.*"), ("", "")), directory="", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._filetypes = filetypes
        self._directory = directory

        self._variable = tk.StringVar()

        self._entry = ttk.Entry(self, textvariable=self._variable)
        self._entry.pack(side="left", fill="x", expand=True)

        self._button = ttk.Button(self, text="Browse", command=self._browse)
        self._button.pack(side="right")

    def _browse(self):
        """Opens a file browser."""
        file = filedialog.askopenfile(filetype=self._filetypes, initialdir=self._directory)
        self._variable.set(file.name)
        file.close()

    def get(self):
        """Returns the chosen file."""
        return self._variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    fpicker = FilePicker(root)
    fpicker.pack(fill="x", expand=True, padx=5, pady=5)
    variable = tk.StringVar()
    label = ttk.Label(root, textvariable=variable)
    label.pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Get", command=lambda: variable.set(fpicker.get())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
