import tkinter as tk
from tkinter import ttk

#https://wxpython.org/Phoenix/docs/html/wx.CollapsiblePane.html

__title__ = "CollapsiblePane"
__version__ = "1.3.1"
__author__ = "DeflatedPickle"

class CollapsiblePane (ttk.Frame):
    """
            -----DESCRIPTION-----
    This widget is used to store any other widgets inside of it.
    It can be toggled on or off, so widgets inside of it aren't always shown.

            -----USAGE-----
    collapsiblePane = CollapsiblePane (parent, expandedtext = [string], collapsedtext = [string])
    collapsiblePane.pack ()
    button = Button (collapsiblePane.subframe).pack ()

            -----CONTENTS-----
    ---VARIABLES---
    expandedtext  = The text shown on the button when the pane is open.
    collapsedtext = The text shown on the button when the pane is closed.
    variable      = The variable used for the button.

    ---WIDGETS---
    Self
    button        = The button that toggles the subframe.
    subframe      = The frame that holds the widget.

    ---FUNCTIONS---
    activate ()   = Checks value of variable and shows or hides the frame.
    toggle ()     = Switches the label frame to the opposite state.
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
        """
        Switches the label frame to the opposite state.
        """
        self.variable.set (not self.variable.get ())
        self.activate ()

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    cpane = CollapsiblePane (root)
    cpane.pack (expand = True, padx = 5, pady = 5)
    for i in range (3):
        ttk.Button (cpane.subframe).pack (side = "left")
    root.mainloop ()
