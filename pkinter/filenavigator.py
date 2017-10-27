#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
import os

# link

__title__ = "FileNavigator"
__version__ = "1.1.1"
__author__ = "DeflatedPickle"


class FileNavigator(ttk.Frame):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    filenavigator = FileNavigator(parent)
    filenavigator.pack()

            -----PARAMETERS-----
    parent     = The parent of the widget.
    directory  = The directory to show.

            -----CONTENTS-----
    ---VARIABLES---
    parent     = The parent of the widget.
    _directory = The directory to show.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _tree      = The Treeview widget.

    ---FUNCTIONS---
    refresh()  = Refreshes the Treeview.
    """
    def __init__(self, parent, directory, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._directory = directory

        self._tree = ttk.Treeview(self, show="tree")
        self._tree.pack(fill="both", expand=True)

        self.refresh()

        self._tree.bind("<Double-Button-1>", lambda event: self.event_generate("<<{}Open>>".format(self._tree.item(self._tree.focus())["tags"][0])))

    def refresh(self):
        self._tree.delete(*self._tree.get_children())

        self._tree.insert(parent="",
                          index="end",
                          iid=self._directory,
                          text=self._directory,
                          tags=("Directory", "root"))

        for root, directories, files in os.walk(self._directory, topdown=True):
            # print("Root: {}".format(root))

            for name in directories:
                # print("Directory: {}".format(name))

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  tags="Directory")

            for name in files:
                # print("File: {}".format(name))

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  tags=("File", os.path.splitext(name)[1]))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    fnavigator = FileNavigator(root, "../")
    fnavigator.pack(fill="y", expand=True, padx=5, pady=5)
    fnavigator.bind("<<DirectoryOpen>>", lambda event: print("Directory."))
    fnavigator.bind("<<FileOpen>>", lambda event: print("File."))
    root.mainloop()
