import tkinter as tk
from tkinter import ttk

#link

__title__ = "LabeledSeparator"
__version__ = "1.0.4"
__author__ = "DeflatedPickle"

class LabeledSeparator (ttk.Frame):
    """
            -----DESCRIPTION-----
    This widget is used as a better separator for different sections.
    It has a label on the separator which can be customized.

            -----USAGE-----
    labeledSeparator = LabeledSeparator (parent, text = [string], orient = [string], textalign = [string], padding = [integer])
    labeledSeparator.pack (fill = "x")

            -----CONTENTS-----
    ---VARIABLES---
    text      = The text shown on the label.
    orient    = The orientation of the separator.
    textalign = The alignment of the label.
    padding   = The padding around the label.

    ---WIDGETS---
    Self
    separator = The separator.
    label     = The label shown on top of the separator.

    ---FUNCTIONS---
    None
    """
    def __init__ (self, parent, text = "", orient = "horizontal", textalign = "", padding = 5, *args):
        ttk.Frame.__init__ (self, parent, *args)
        self.text = text
        self.orient = orient
        self.textalign = textalign
        self.padding = padding

        self.separator = ttk.Separator (self, orient = self.orient)
        self.label = ttk.Label (self, text = self.text)

        if self.orient == "horizontal":
            self.grid_columnconfigure (0, weight = 1)
            self.separator.grid (row = 0, column = 0, sticky = "we")
            self.label.grid (row = 0, column = 0, sticky = textalign, padx = padding)

        elif self.orient == "vertical":
            self.grid_rowconfigure (0, weight = 1)
            self.separator.grid (row = 0, column = 0, sticky = "ns")
            self.label.grid (row = 0, column = 0, sticky = textalign, pady = padding)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    root.grid_columnconfigure (0, weight = 1)
    hlseparator = LabeledSeparator (root, text = "Horizontal", orient = "horizontal", textalign = "", padding = 5)
    hlseparator.grid (row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)

    root.grid_rowconfigure (1, weight = 1)
    vlseparator = LabeledSeparator (root, text = "LabeledSeparator", orient = "vertical", textalign = "", padding = 5)
    vlseparator.grid (row = 1, column = 0, sticky = "ns", padx = 5, pady = 5)
    root.mainloop ()
