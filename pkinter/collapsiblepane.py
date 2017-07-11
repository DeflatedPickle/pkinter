#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# http://docs.wxwidgets.org/3.1/classwx_collapsible_pane.html

__title__ = "CollapsiblePane"
__version__ = "1.3.5"
__author__ = "DeflatedPickle"


class CollapsiblePane(ttk.Frame):
    """
            -----DESCRIPTION-----
    This widget is used to store any other widgets inside of it.
    It can be toggled on or off, so widgets inside of it aren't always shown.

            -----USAGE-----
    collapsiblePane = CollapsiblePane(parent, expanded_text=[string], collapsed_text=[string])
    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()

            -----PARAMETERS-----
    parent          = The parent of the widget.
    expanded_text   = The text shown on the Button when the pane is open.
    collapsed_text  = The text shown on the Button when the pane is closed.

            -----CONTENTS-----
    ---VARIABLES---
    parent          = The parent of the widget.
    _expanded_text  = The text shown on the Button when the pane is open.
    _collapsed_text = The text shown on the Button when the pane is closed.

    ---TKINTER VARIABLES---
    _variable       = The variable used for the Button.

    ---WIDGETS---
    self
    _button         = The Button that toggles the Frame.
    frame           = The Frame that holds the widget.
    _separator      = The Separator.

    ---FUNCTIONS---
    _activate()     = Checks the value of variable and shows or hides the Frame.
    toggle()        = Switches the LabelFrame to the opposite state.
    """
    def __init__(self, parent, expanded_text="Collapse <<", collapsed_text="Expand >>", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text

        self.columnconfigure(1, weight=1)

        self._variable = tk.IntVar()
        self._button = ttk.Checkbutton(self, variable=self._variable, command=self._activate, style="TButton")
        self._button.grid(row=0, column=0)

        self._separator = ttk.Separator(self, orient="horizontal")
        self._separator.grid(row=0, column=1, sticky="we")

        self.frame = ttk.Frame(self)

        self._activate()

    def _activate(self):
        if not self._variable.get():
            self.frame.grid_forget()
            self._button.configure(text=self._collapsed_text)

        elif self._variable.get():
            self.frame.grid(row=1, column=0, columnspan=2)
            self._button.configure(text=self._expanded_text)

    def toggle(self):
        """Switches the label frame to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    cpane = CollapsiblePane(root)
    cpane.pack(expand=True, padx=5, pady=5)
    for i in range(3):
        ttk.Button(cpane.frame).pack(side="left")
    root.mainloop()
