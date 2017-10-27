#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
import os

# link

__title__ = "FileNavigator"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class FileNavigator(ttk.Treeview):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    filenavigator = FileNavigator(parent)
    filenavigator.pack()

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
    def __init__(self, parent, directory, *args):
        ttk.Treeview.__init__(self, parent, show="tree", *args)
        self.parent = parent
        self._directory = directory

        self.refresh()

    def refresh(self):
        self.insert(parent="",
                    index="end",
                    iid=self._directory,
                    text=self._directory,
                    tags="directory")

        for root, directories, files in os.walk(self._directory, topdown=True):
            # print("Root: {}".format(root))

            for name in directories:
                # print("Directory: {}".format(name))

                self.insert(parent=root,
                            index="end",
                            iid=os.path.join(root, name),
                            text=name,
                            tags="directory")

            for name in files:
                # print("File: {}".format(name))

                self.insert(parent=root,
                            index="end",
                            iid=os.path.join(root, name),
                            text=name,
                            tags="directory")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    fnavigator = FileNavigator(root, "../")
    fnavigator.pack(fill="y", expand=True, padx=5, pady=5)
    root.mainloop()
