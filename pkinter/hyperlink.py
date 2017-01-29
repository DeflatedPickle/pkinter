import tkinter as tk
from tkinter import ttk
from tkinter import font
import os

#link

__title__ = "Hyperlink"
__version__ = "1.1.2"
__author__ = "DeflatedPickle"

class Hyperlink (ttk.Label):
    """
            -----DESCRIPTION-----
    A modification of the TTK label to act as a hyperlink.
    It can take the user to any given website with a click.

            -----USAGE-----
    hyperlink = Hyperlink (parent, link = [string])
    hyperlink.pack ()

            -----CONTENTS-----
    ---VARIABLES---
    link               = Holds the website to go to.
    show_text          = Holds the text shown in the hyperlink label.
    font               = The font of the label.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    enter ()           = Runs when the mouse enters the widget.
    leave ()           = Runs when the mouse leaves the widget.
    button ()          = Runs when the user clicks the widget.
    button_released () = Runs when the user stops clicking on the widget.
    """
    def __init__ (self, parent, link = "https://github.com/DeflatedPickle/pkinter", show_text = "Hyperlink", *args):
        ttk.Label.__init__ (self, parent, text = show_text, foreground = "blue", cursor = "arrow", *args)
        self.link = link
        self.font = font.Font (self, self.cget ("font"))
        self.configure (font = self.font)

        self.bind ("<Enter>", self.enter)
        self.bind ("<Leave>", self.leave)
        self.bind ("<Button-1>", self.button)
        self.bind ("<ButtonRelease-1>", self.button_released)

    def enter (self, *args):
        self.configure (foreground = "dodgerblue", cursor = "hand2")
        self.font.configure (underline = True)

    def leave (self, *args):
        self.configure (foreground = "blue", cursor = "arrow")
        self.font.configure (underline = False)

    def button (self, *args):
        self.configure (foreground = "medium blue", cursor = "arrow")
        self.font.configure (underline = True)

    def button_released (self, *args):
        self.configure (foreground = "dodgerblue", cursor = "arrow")
        self.font.configure (underline = False)
        try:
            os.startfile(self.link)
        except FileNotFoundError:
            raise ValueError("Link value: {} is not a functioning URL".format(self.link))

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    hlink = Hyperlink (root, link = "https://github.com/DeflatedPickle/pkinter")
    hlink.pack (expand = True, padx = 5, pady = 5)
    root.mainloop ()
