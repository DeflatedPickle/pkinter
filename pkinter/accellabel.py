import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkAccelLabel.html

__title__ = "AccelLabel"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class AccelLabel(ttk.Frame):
    """
            -----DESCRIPTION-----
    A Label which displays an accelerator key on the right of the text.

            -----USAGE-----
    accelLabel = AccelLabel(parent, label=[string], accelerator=[string])
    accelLabel.pack()

            -----PARAMETERS-----
    label_text       = The text used for the Label.
    accelerator_text = The text used for the accelerator Label.
    separator        = Whether or not the Separator is shown.

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    self
    label            = The Label widget.
    accelerator      = The accelerator Label widget.

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, label_text="", accelerator_text="", separator=False, *args):
        ttk.Frame.__init__(self, parent, *args)

        self.label = ttk.Label(self, text=label_text).pack(side="left", fill="x")
        self.accelerator = ttk.Label(self, text=accelerator_text).pack(side="right")

        if separator:
            self.separator = ttk.Separator(self, orient="vertical").pack(side="right", fill="y")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    alabel = AccelLabel(root, label_text="Select All", accelerator_text="Ctrl+A")
    alabel.pack(fill="x", expand=True, padx=5, pady=5)
    root.mainloop()
