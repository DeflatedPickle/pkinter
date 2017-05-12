#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkSwitch.html

__title__ = "ButtonSwitch"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class ButtonSwitch(ttk.Frame):
    """
            -----DESCRIPTION-----
    A “light switch” style toggle.

            -----USAGE-----
    buttonSwitch = ButtonSwitch(parent)
    template.pack()

            -----PARAMETERS-----
    parent

            -----CONTENTS-----
    ---VARIABLES---
    button_variable     = The variable for the placement of the button.
    label_variable      = The variable for the placement of the label.
    label_text_variable = The variable for the text of the label.

    ---WIDGETS---
    self
    button              = The widget used to "flick" the switch.
    label               = The label used to show the state of the switch.

    ---FUNCTIONS---
    switch()            = Switches the Switch to the opposite state.
    get_state()         = Returns the state of the Switch.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.columnconfigure((0, 1), weight=1)

        self.button_variable = tk.BooleanVar()
        self.button_variable.set(False)
        self.label_variable = tk.BooleanVar()
        self.label_variable.set(True)
        self.label_text_variable = tk.StringVar()

        ttk.Style().configure("Switch.TLabel", background="white", foreground="light gray", anchor="center")
        ttk.Style().configure("Label.TLabel", background="light blue", foreground="white", anchor="center")

        self.button = ttk.Label(self, text="| | |", width=4, style="Switch.TLabel")
        self.button.bind("<Button-1>", self.switch)
        self.label = ttk.Label(self, textvariable=self.label_text_variable, width=4, style="Label.TLabel")

        ttk.Style().configure("ButtonSwitch.TFrame", background="light blue")
        self.configure(style="ButtonSwitch.TFrame")

        self.switch()

    def switch(self, *args):
        """Switches the state of the Switch."""
        self.button_variable.set(not self.button_variable.get())
        self.label_variable.set(not self.label_variable.get())

        if self.button_variable.get() is False:
            self.label_text_variable.set("Off")

        elif self.button_variable.get() is True:
            self.label_text_variable.set("On")

        self.button.grid(row=0, column=self.button_variable.get(), padx=1, pady=1, sticky="nesw")
        self.label.grid(row=0, column=self.label_variable.get(), padx=1, pady=1, sticky="nesw")

    def get_state(self):
        """Gets the state of the Switch."""
        return self.button_variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    bswitch = ButtonSwitch(root)
    bswitch.pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Switch", command=lambda: bswitch.switch()).pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Get State", command=lambda: print(bswitch.get_state())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
