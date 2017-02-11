import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

# link

__title__ = "ColourPickerButton"
__version__ = "1.3.4"
__author__ = "DeflatedPickle"


class ColourPickerButton(ttk.Button):
    """
            -----DESCRIPTION-----
    A TTK Button that allows you to choose a colour.
    It then sets the background to that colour.

            -----USAGE-----
    colourPickerButton = ColourPickerButton(root, text=[string])
    colourPickerButton.pick()

            -----PARAMETERS-----
    text           = The text shown on the button.

            -----CONTENTS-----
    ---VARIABLES---
    text           = The text shown on the button.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    pick_colour()  = Opens the colour picker window.
    reset()        = Resets the button.
    get()          = Gets the text of the button.
    """
    def __init__(self, parent, text="Pick A Colour", *args):
        ttk.Button.__init__(self, parent, text=text, command=self.pick_colour, *args)
        self.text = text

        ttk.Style().configure("ColourButton.TButton")

        self.configure(style="ColourButton.TButton")

    def pick_colour(self):
        colour = askcolor()
        self.configure(text=colour[1])
        ttk.Style().configure("ColourButton.TButton", background=colour[1])

    def reset(self):
        """
        Resets the button.
        """
        self.configure(text=self.text)
        ttk.Style().configure("ColourButton.TButton", background=ttk.Style().lookup("TButton", "background"))

    def get(self):
        """
        Gets the text of the button.
        """
        return self["text"]

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    cpbutton = ColourPickerButton(root, text="Pick A Colour")
    cpbutton.pack(expand=True, padx=5, pady=5)
    root.mainloop()
