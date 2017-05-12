#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# http://docs.wxwidgets.org/3.1/classwx_collapsible_pane.html

__title__ = "CollapsiblePane"
__version__ = "1.3.4"
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
    expanded_text   = The text shown on the Button when the pane is open.
    collapsed_text  = The text shown on the Button when the pane is closed.

            -----CONTENTS-----
    ---VARIABLES---
    expanded_text   = The text shown on the Button when the pane is open.
    collapsed_text  = The text shown on the Button when the pane is closed.
    variable        = The variable used for the Button.

    ---WIDGETS---
    self
    button          = The Button that toggles the Frame.
    frame           = The Frame that holds the widget.

    ---FUNCTIONS---
    activate()      = Checks the value of variable and shows or hides the Frame.
    toggle()        = Switches the LabelFrame to the opposite state.
    """
    def __init__(self, parent, expanded_text="Expanded <<", collapsed_text="Collapsed >>", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.columnconfigure(1, weight=1)
        
        self.expanded_text = expanded_text
        self.collapsed_text = collapsed_text

        self.variable = tk.IntVar()
        self.button = ttk.Checkbutton(self, variable=self.variable, command=self.activate, style="TButton")
        self.button.grid(row=0, column=0)
        ttk.Separator(self, orient="horizontal").grid(row=0, column=1, sticky="we")

        self.frame = ttk.Frame(self)

        self.activate()

    def activate(self):
        if not self.variable.get():
            self.frame.grid_forget()
            self.button.configure(text=self.collapsed_text)

        elif self.variable.get():
            self.frame.grid(row=1, column=0, columnspan=2)
            self.button.configure(text=self.expanded_text)

    def toggle(self):
        """Switches the label frame to the opposite state."""
        self.variable.set(not self.variable.get())
        self.activate()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    cpane = CollapsiblePane(root)
    cpane.pack(expand=True, padx=5, pady=5)
    for i in range(3):
        ttk.Button(cpane.frame).pack(side="left")
    root.mainloop()
