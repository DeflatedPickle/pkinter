#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkInfoBar.html

__title__ = "InfoBar"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class InfoBar(ttk.Frame):
    """
            -----DESCRIPTION-----
    A bar to show a piece of information.
    Can be closed by the user.

            -----USAGE-----
    infoBar = InfoBar(parent, title=[string], title_command=[function], info=[string], info_command=[function], background=[string])
    infoBar.pack()

            -----PARAMETERS-----
    parent         = The parent of the widget.
    title          = The text used for the title Button.
    title_command  = The command that will run when the title Button is pressed.
    info           = The text used for the info Button.
    info_command   = The command that will run when the info Button is pressed.
    background     = The background of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent         = The parent of the widget.
    _title         = The text used for the title Button.
    _title_command = The command that will run when the title Button is pressed.
    _info          = The text used for the info Button.
    _info_command  = The command that will run when the info Button is pressed.
    _background    = The background of the widget.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _title_button  = Shows the title text.
    _info_button   = Shows the info text.
    _close_button  = The button for closing the widget.

    ---FUNCTIONS---
    close()        = Removes the widget from it's parent.
    """
    def __init__(self, parent, title="", title_command=None, info="", info_command=None, background="SystemButtonFace", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._title = title
        self._title_command = title_command
        self._info = info
        self._info_command = info_command
        self._background = background

        self.columnconfigure(1, weight=1)

        style = ttk.Style()
        style.configure("InfoBar.Toolbutton", background=self._background)
        style.configure("InfoClose.InfoBar.Toolbutton", anchor="center")

        if self._title != "":
            self._title_button = ttk.Button(self, text=self._title, style="InfoBar.Toolbutton", command=self._title_command)
            self._title_button.grid(row=0, column=0)

        self._info_button = ttk.Button(self, text=self._info, style="InfoBar.Toolbutton", command=self._info_command)
        self._info_button.grid(row=0, column=1, sticky="we")

        self._close_button = ttk.Button(self, text="x", width=2, style="InfoClose.InfoBar.Toolbutton", command=self.close)
        self._close_button.grid(row=0, column=2)

    def close(self):
        """Closes the InfoBar."""
        if self.winfo_manager() == "pack":
            self.pack_forget()

        elif self.winfo_manager() == "grid":
            self.grid_forget()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ibar = InfoBar(root, info="A Piece of Information", background="light blue")
    ibar.pack(fill="x")
    root.mainloop()
