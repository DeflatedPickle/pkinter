#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
import os

# link

__title__ = "FileNavigator"
__version__ = "1.4.0"
__author__ = "DeflatedPickle"


class FileNavigator(ttk.Frame):
    """
            -----DESCRIPTION-----
    A Treeview that shows all contents of a directory.

            -----USAGE-----
    filenavigator = FileNavigator(parent, directory=[string])
    filenavigator.pack()

            -----PARAMETERS-----
    parent         = The parent of the widget.
    directory      = The directory to show.

            -----CONTENTS-----
    ---VARIABLES---
    parent         = The parent of the widget.
    _directory     = The directory to show.
    images         = A dictionary of images to use.
    selected       = The selected item in the Treeview.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _tree          = The Treeview widget.

    ---FUNCTIONS---
    _select()      = Sets the selected item
    _open_event()  =
    _close_event() =
    refresh()      = Refreshes the Treeview.
    """
    def __init__(self, parent, directory, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._directory = directory

        self.images = {"Directory": tk.PhotoImage(),
                       "File": tk.PhotoImage()}

        self.selected = None

        self._tree = ttk.Treeview(self, show="tree")
        self._tree.pack(fill="both", expand=True)

        self._tree.bind("<<TreeviewSelect>>", self._select, "+")
        # self._tree.bind("<Double-Button-1>", self._open_event)
        self._tree.bind("<<TreeviewOpen>>", self._open_event, "+")
        self._tree.bind("<<TreeviewClose>>", self._close_event, "+")

        self.refresh()

    def _select(self, event=None):
        self.selected = self._tree.item(self._tree.focus())

    def _open_event(self, event=None):
        self._select()
        self.event_generate("<<{}Open>>".format(self._tree.item(self._tree.focus())["tags"][0]))

    def _close_event(self, event=None):
        self._select()
        self.event_generate("<<{}Close>>".format(self._tree.item(self._tree.focus())["tags"][0]))

    def refresh(self):
        self._tree.delete(*self._tree.get_children())

        self._tree.insert(parent="",
                          index="end",
                          iid=self._directory,
                          text=self._directory,
                          image=self.images["Directory"],
                          tags=("Directory", "root", self._directory))

        for root, directories, files in os.walk(self._directory, topdown=True):
            # print("Root: {}".format(root))

            for name in directories:
                # print("Directory: {}".format(name))

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  image=self.images["Directory"],
                                  tags=("Directory", "\\", os.path.join(root, name)))

            for name in files:
                # print("File: {}".format(name))
                extension = os.path.splitext(name)[1]

                self._tree.insert(parent=root,
                                  index="end",
                                  iid=os.path.join(root, name),
                                  text=name,
                                  image=self.images.get(extension) if self.images.get(extension) else self.images["File"],
                                  tags=("File", extension, os.path.join(root, name)))

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    fnavigator = FileNavigator(root, "..\\")
    fnavigator.pack(fill="y", expand=True, padx=5, pady=5)

    fnavigator.bind("<<DirectoryOpen>>", lambda event: print("Opened:", fnavigator.selected["tags"][2]))
    fnavigator.bind("<<FileOpen>>", lambda event: print("Opened:", fnavigator.selected["tags"][2]))
    fnavigator.bind("<<DirectoryClose>>", lambda event: print("Closed:", fnavigator.selected["tags"][2]))
    fnavigator.bind("<<FileClose>>", lambda event: print("Closed:", fnavigator.selected["tags"][2]))
    root.mainloop()
