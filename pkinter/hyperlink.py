#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import font
import os

# link

__title__ = "Hyperlink"
__version__ = "1.2.4"
__author__ = "DeflatedPickle"


class Hyperlink(ttk.Label):
    """
            -----DESCRIPTION-----
    A modification of the TTK label to act as a hyperlink.
    It can take the user to any given website with a click.
    If the text parameter is left blank, it will use the link as the text.

            -----USAGE-----
    hyperlink = Hyperlink (parent, link = [string])
    hyperlink.pack ()

            -----PARAMETERS-----
    parent             = The parent of the widget.
    text               = The text shown on the Label.
    link               = Holds the website to go to.

            -----CONTENTS-----
    ---VARIABLES---
    parent             = The parent of the widget.
    _text               = The text shown on the Label.
    _link               = Holds the website to go to.
    _font               = The font of the Label.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _enter()           = Runs when the mouse enters the widget.
    _leave()           = Runs when the mouse leaves the widget.
    _button()          = Runs when the user clicks the widget.
    _button_released() = Runs when the user stops clicking on the widget.
    """
    def __init__(self, parent, text="", link="https://github.com/DeflatedPickle/pkinter", *args):
        ttk.Label.__init__(self, parent, foreground="blue", cursor="arrow", *args)
        self.parent = parent
        self._text = text
        self._link = link

        self._font = font.Font(self, self.cget("font"))
        self.configure(font=self._font)

        if self._text == "":
            self.configure(text=self._link)

        else:
            self.configure(text=self._text)

        self.bind("<Enter>", self._enter, "+")
        self.bind("<Leave>", self._leave, "+")
        self.bind("<Button-1>", self._button, "+")
        self.bind("<ButtonRelease-1>", self._button_released, "+")

    def _enter(self, event=None):
        self.configure(foreground="dodgerblue", cursor="hand2")
        self._font.configure(underline=True)

    def _leave(self, event=None):
        self.configure(foreground="blue", cursor="arrow")
        self._font.configure(underline=False)

    def _button(self, event=None):
        self.configure(foreground="medium blue", cursor="arrow")
        self._font.configure(underline=True)

    def _button_released(self, event=None):
        self.configure(foreground="dodgerblue", cursor="arrow")
        self._font.configure(underline=False)
        # webbrowser.open_new_tab(self._link)
        os.startfile(self._link)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    hlink = Hyperlink(root, link="https://github.com/DeflatedPickle/pkinter")
    hlink.pack(expand=True, padx=5, pady=5)
    htext = Hyperlink(root, text="GitHub", link="https://github.com/DeflatedPickle/pkinter")
    htext.pack(expand=True, padx=5, pady=5)
    root.mainloop()
