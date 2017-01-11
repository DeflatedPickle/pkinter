import tkinter as tk
from tkinter import ttk
from tkinter import font
import webbrowser

#link

__title__ = "Hyperlink"
__version__ = "1.0.2"
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
    font               = The font of the label.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    enter ()           = Runs when the mouse enters the widget.
    leave ()           = Runs when the mouse leaves the widget.
    button ()          = Runs when the user clicks the widget.
    button_released () = Runs when the user stops clicking on the widget.
    """
    def __init__ (self, parent, link = "https://github.com/DeflatedPickle/pkinter", *args):
        ttk.Label.__init__ (self, parent, text = link, foreground = "blue", cursor = "arrow", *args)
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
        webbrowser.open_new_tab (self.link)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    hlink = Hyperlink (root, link = "https://github.com/DeflatedPickle/pkinter")
    hlink.grid (row = 0, column = 0, padx = 5, pady = 5)
    root.mainloop ()
