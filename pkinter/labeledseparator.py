#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

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
    parent      = The parent of the widget.
    text        = The text shown on the label.
    orient      = The orientation of the separator.
    text_align  = The alignment of the label.
    padding     = The padding around the label.

            -----CONTENTS-----
    ---VARIABLES---
    parent      = The parent of the widget.
    _text       = The text shown on the label.
    _orient     = The orientation of the separator.
    _text_align = The alignment of the label.
    _padding    = The padding around the label.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _separator   = The separator.
    _label       = The label shown on top of the separator.

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, text="", orient="horizontal", text_align="", padding=5, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._text = text
        self._orient = orient
        self._text_align = text_align
        self._padding = padding

        self._separator = ttk.Separator(self, orient=self._orient)
        self._label = ttk.Label(self, text=self._text)

        if self._orient == "horizontal":
            self.grid_columnconfigure(0, weight=1)

            self._separator.grid(row=0, column=0, sticky="we")
            self._label.grid(row=0, column=0, sticky=self._text_align, padx=self._padding)

        elif self._orient == "vertical":
            self.grid_rowconfigure(0, weight=1)

            self._separator.grid(row=0, column=0, sticky="ns")
            self._label.grid(row=0, column=0, sticky=self._text_align, pady=self._padding)

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
