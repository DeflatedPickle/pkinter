import tkinter as tk
from tkinter import ttk

#https://wxpython.org/Phoenix/docs/html/wx.CollapsiblePane.html

__title__ = "CollapsiblePane"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"

class CollapsiblePane (ttk.Frame):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__ (self, parent, expandedtext = "Expanded <<", collapsedtext = "Collapsed >>", *args):
        ttk.Frame.__init__ (self, parent, *args)
        self.expandedtext = expandedtext
        self.collapsedtext = collapsedtext
        self.columnconfigure (1, weight = 1)

        self.variable = tk.IntVar ()
        self.button = ttk.Checkbutton (self, variable = self.variable, command = self.activate, style = "TButton")
        self.button.grid (row = 0, column = 0)
        ttk.Separator (self, orient = "horizontal").grid (row = 0, column = 1, sticky = "we")

        self.subframe = ttk.Frame (self)

        self.activate ()

    def activate (self):
        if self.variable.get () == False:
            self.subframe.grid_forget ()
            self.button.configure (text = self.expandedtext)

        elif self.variable.get () == True:
            self.subframe.grid (row = 1, column = 0, columnspan = 2)
            self.button.configure (text = self.collapsedtext)

    def toggle (self):
        self.variable.set (not self.variable.get ())
        self.activate ()

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    cpane = CollapsiblePane (root)
    cpane.grid (row = 0, column = 0, padx = 5, pady = 5)
    for i in range (5):
        ttk.Button (cpane.subframe).pack (side = "left")
    root.mainloop ()
