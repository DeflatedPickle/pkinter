#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import font
import os

# link

__title__ = "Hyperlink"
__version__ = "1.2.3"
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
    text               = The text shown on the Label.
    link               = Holds the website to go to.

            -----CONTENTS-----
    ---VARIABLES---
    text               = The text shown on the Label.
    link               = Holds the website to go to.
    font               = The font of the Label.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    enter()           = Runs when the mouse enters the widget.
    leave()           = Runs when the mouse leaves the widget.
    button()          = Runs when the user clicks the widget.
    button_released() = Runs when the user stops clicking on the widget.
    """
    def __init__(self, parent, text="", link="https://github.com/DeflatedPickle/pkinter", *args):
        ttk.Label.__init__(self, parent, foreground="blue", cursor="arrow", *args)
        self.text = text
        self.link = link
        self.font = font.Font(self, self.cget("font"))
        self.configure(font=self.font)

        if self.text == "":
            self.configure(text=self.link)

        else:
            self.configure(text=self.text)

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)
        self.bind("<Button-1>", self.button)
        self.bind("<ButtonRelease-1>", self.button_released)

    def enter(self, *args):
        self.configure(foreground="dodgerblue", cursor="hand2")
        self.font.configure(underline=True)

    def leave(self, *args):
        self.configure(foreground="blue", cursor="arrow")
        self.font.configure(underline=False)

    def button(self, *args):
        self.configure(foreground="medium blue", cursor="arrow")
        self.font.configure(underline=True)

    def button_released(self, *args):
        self.configure(foreground="dodgerblue", cursor="arrow")
        self.font.configure(underline=False)
        # webbrowser.open_new_tab(self.link)
        os.startfile(self.link)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    hlink = Hyperlink(root, link="https://github.com/DeflatedPickle/pkinter")
    hlink.pack(expand=True, padx=5, pady=5)
    htext = Hyperlink(root, text="GitHub", link="https://github.com/DeflatedPickle/pkinter")
    htext.pack(expand=True, padx=5, pady=5)
    root.mainloop()
