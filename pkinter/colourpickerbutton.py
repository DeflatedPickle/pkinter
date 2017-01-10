import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

#link

__title__ = "ColourPickerButton"
__version__ = "0.1.1"
__author__ = "DeflatedPickle"

class ColourPickerButton (ttk.Button):
    """
            -----DESCRIPTION-----
    A TTK Button that allows you to choose a colour.
    It then sets the background to that colour.

            -----USAGE-----
    colourPickerButton = ColourPickerButton (root, text = [string])
    colourPickerButton.pick ()

            -----CONTENTS-----
    ---VARIABLES---
    text           = The text shown on the button.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    pick_colour () = Opens the colour picker window.
    reset ()       = Resets the button.
    get ()         = Gets the text of the button.
    """
    def __init__ (self, parent, text = "Pick A Colour", *args):
        ttk.Button.__init__ (self, parent, text = text, command = self.pick_colour, *args)
        self.text = text

        ttk.Style ().configure ("ColourButton.TButton")

        self.configure (style = "ColourButton.TButton")

    def pick_colour (self):
        colour = askcolor ()
        self.configure (text = colour [1])
        ttk.Style ().configure ("ColourButton.TButton", background = colour [1])

    def reset (self):
        self.configure (text = self.text)
        ttk.Style ().configure ("ColourButton.TButton", background = ttk.Style ().lookup ("TButton", "background"))

    def get (self):
        return self ["text"]

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    cpbutton = ColourPickerButton (root, text = "Pick A Colour")
    cpbutton.grid (row = 0, column = 0, padx = 5, pady = 5)
    ttk.Button (root, text = "Reset", command = lambda: cpbutton.reset ()).grid (row = 1, column = 0)

    entry = ttk.Entry (root)
    entry.grid (row = 0, column = 1)

    def get ():
        entry.delete (0, "end")
        entry.insert (0, cpbutton.get ())

    ttk.Button (root, text = "Get", command = get).grid (row = 1, column = 1)

    root.mainloop ()
