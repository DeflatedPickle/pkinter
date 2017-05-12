#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkSwitch.html

__title__ = "ScaleSwitch"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class ScaleSwitch(ttk.Scale):
    """
            -----DESCRIPTION-----
    A “light switch” style toggle.

            -----USAGE-----
    switch = ScaleSwitch(parent)
    switch.pack()

            -----PARAMETERS-----
    parent

            -----CONTENTS-----
    ---VARIABLES---
    variable    = The variable used for the widget.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    activate()  = Checks value of variable toggles the Switch.
    toggle()    = Switches the Switch to the opposite state.
    on()        = Changes the Button to the on state.
    off()       = Changes the Button to the off state.
    get_state() = Returns the state of the Switch.
    """
    def __init__(self, parent, *args):
        ttk.Scale.__init__(self, parent, from_=0, to=1, *args)

        self.variable = tk.DoubleVar()
        self.configure(variable=self.variable)

        self.bind("<ButtonRelease-1>", self.activate)

    def activate(self, *args):
        if self.variable.get() >= 0.5:
            self.variable.set(True)

        else:
            self.variable.set(False)

    def toggle(self):
        """Switches the LabelFrame to the opposite state."""
        self.variable.set(not self.variable.get())
        self.activate()

    def on(self):
        """Turns the Switch on."""
        self.variable.set(True)
        self.activate()

    def off(self):
        """Turns the Switch off."""
        self.variable.set(False)
        self.activate()

    def get_state(self):
        """Gets the state of the Switch."""
        return self.variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    sswitch = ScaleSwitch(root)
    sswitch.pack(expand=True, padx=5, pady=5)
    root.mainloop()
