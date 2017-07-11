#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkAccelLabel.html

__title__ = "AccelLabel"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class AccelLabel(ttk.Frame):
    """
            -----DESCRIPTION-----
    A Label which displays an accelerator key on the right of the text.

            -----USAGE-----
    accelLabel = AccelLabel(parent, label=[string], accelerator=[string])
    accelLabel.pack()

            -----PARAMETERS-----
    parent            = The parent of the widget.
    label_text        = The text used for the Label.
    accelerator_text  = The text used for the accelerator Label.
    has_separator     = Whether or not the Separator is shown.

            -----CONTENTS-----
    ---VARIABLES---
    parent            = The parent of the widget.
    _label_text       = The text used for the Label.
    _accelerator_text = The text used for the accelerator Label.
    _has_separator    = Whether or not the Separator is shown.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _label            = The Label widget.
    _accelerator      = The accelerator Label widget.

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, label_text="", accelerator_text="", has_separator=False, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

        self._label_text = label_text
        self._accelerator_text = accelerator_text
        self._has_separator = has_separator

        self._label = ttk.Label(self, text=self._label_text).pack(side="left", fill="x")
        self._accelerator = ttk.Label(self, text=self._accelerator_text).pack(side="right")

        if self._has_separator:
            self._separator = ttk.Separator(self, orient="vertical").pack(side="right", fill="y")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    alabel = AccelLabel(root, label_text="Select All", accelerator_text="Ctrl+A")
    alabel.pack(fill="x", expand=True, padx=5, pady=5)
    root.mainloop()
