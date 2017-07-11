#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkSwitch.html

__title__ = "ScaleSwitch"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class ScaleSwitch(ttk.Scale):
    """
            -----DESCRIPTION-----
    A “light switch” style toggle.

            -----USAGE-----
    switch = ScaleSwitch(parent)
    switch.pack()

            -----PARAMETERS-----
    parent      = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent      = The parent of the widget.

    ---TKINTER VARIABLES---
    _variable   = The variable used for the widget.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _activate() = Checks value of variable toggles the Switch.
    toggle()    = Switches the Switch to the opposite state.
    turn_on()   = Changes the Switch to the on state.
    turn_off()  = Changes the Switch to the off state.
    get_state() = Returns the state of the Switch.
    """
    def __init__(self, parent, *args):
        ttk.Scale.__init__(self, parent, from_=0, to=1, *args)
        self.parent = parent

        self._variable = tk.DoubleVar()
        self.configure(variable=self._variable)

        self.bind("<ButtonRelease-1>", self._activate, "+")

    def _activate(self, event=None):
        if self._variable.get() >= 0.5:
            self._variable.set(True)

        else:
            self._variable.set(False)

    def toggle(self):
        """Switches the LabelFrame to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

    def turn_on(self):
        """Turns the Switch on."""
        self._variable.set(True)
        self._activate()

    def turn_off(self):
        """Turns the Switch off."""
        self._variable.set(False)
        self._activate()

    def get_state(self):
        """Gets the state of the Switch."""
        return self._variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    sswitch = ScaleSwitch(root)
    sswitch.pack(expand=True, padx=5, pady=5)
    root.mainloop()
