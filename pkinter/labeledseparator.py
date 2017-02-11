import tkinter as tk
from tkinter import ttk

# link

__title__ = "LabeledSeparator"
__version__ = "1.0.6"
__author__ = "DeflatedPickle"


class LabeledSeparator(ttk.Frame):
    """
            -----DESCRIPTION-----
    This widget is used as a better separator for different sections.
    It has a label on the separator which can be customized.

            -----USAGE-----
    labeledSeparator = LabeledSeparator(parent, text=[string], orient=[string], text_align=[string], padding=[integer])
    labeledSeparator.pack(fill="x")

            -----PARAMETERS-----
    text       = The text shown on the label.
    orient     = The orientation of the separator.
    text_align = The alignment of the label.
    padding    = The padding around the label.

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    self
    separator  = The separator.
    label      = The label shown on top of the separator.

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, text="", orient="horizontal", text_align="", padding=5, *args):
        ttk.Frame.__init__(self, parent, *args)

        self.separator = ttk.Separator(self, orient=orient)
        self.label = ttk.Label(self, text=text)

        if orient == "horizontal":
            self.grid_columnconfigure(0, weight=1)
            self.separator.grid(row=0, column=0, sticky="we")
            self.label.grid(row=0, column=0, sticky=text_align, padx=padding)

        elif orient == "vertical":
            self.grid_rowconfigure(0, weight=1)
            self.separator.grid(row=0, column=0, sticky="ns")
            self.label.grid(row=0, column=0, sticky=text_align, pady=padding)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    root.grid_columnconfigure(0, weight=1)
    hlseparator = LabeledSeparator(root, text="Horizontal", orient="horizontal", text_align="", padding=5)
    hlseparator.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    root.grid_rowconfigure(1, weight=1)
    vlseparator = LabeledSeparator(root, text="LabeledSeparator", orient="vertical", text_align="", padding=5)
    vlseparator.grid(row=1, column=0, sticky="ns", padx=5, pady=5)
    root.mainloop()
