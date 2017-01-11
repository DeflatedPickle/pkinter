import tkinter as tk
from tkinter import ttk
from tkinter import font
import webbrowser

#link

__title__ = "Hyperlink"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"

class Hyperlink (ttk.Label):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__ (self, parent, link = "www.website.com", *args):
        ttk.Label.__init__ (self, parent, text = link, foreground = "blue", cursor = "arrow", *args)
        self.link = link
        self.font = font.Font ()
        self.configure (font = self.font)

        self.bind ("<Enter>", self.enter)
        self.bind ("<Leave>", self.leave)
        self.bind ("<Button-1>", self.button)
        self.bind ("<ButtonRelease-1>", self.button_released)

    def enter (self, *args):
        self.configure (foreground = "dodgerblue", cursor = "hand2")

    def leave (self, *args):
        self.configure (foreground = "blue", cursor = "arrow")

    def button (self, *args):
        self.configure (foreground = "medium blue", cursor = "arrow")

    def button_released (self, *args):
        self.configure (foreground = "dodgerblue", cursor = "arrow")
        webbrowser.open_new_tab (self.link)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    hlink = Hyperlink (root)
    hlink.grid (row = 0, column = 0, padx = 5, pady = 5)
    root.mainloop ()
