#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkToggleButton.html

__title__ = "ToggleButton"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class ToggleButton(ttk.Checkbutton):
    """
            -----DESCRIPTION-----
    A Button that can be toggled.

            -----USAGE-----
    toggleButton = ToggleButton(parent, text_on=[string], text_off=[string])
    toggleButton.pack()

            -----PARAMETERS-----
    parent     = The parent of the widget.
    text_on    = The text shown when the Button is toggled on.
    text_off   = The text shown when the Button is toggled off.

            -----CONTENTS-----
    ---VARIABLES---
    parent     = The parent of the widget.
    _text_on   = The text shown when the Button is toggled on.
    _text_off  = The text shown when the Button is toggled off.

    ---TKINTER VARIABLES---
    _variable  = The variable used for the Button.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _activate() = Checks value of variable toggles the Button.
    toggle()    = Switches the Switch to the opposite state.
    turn_on()   = Changes the Button to the on state.
    turn_off()  = Changes the Button to the off state.
    get_state() = Returns the state of the Button.
    """
    def __init__(self, parent, value_on="On", value_off="Off", key="text", *args):
        ttk.Checkbutton.__init__(self, parent, style="TButton", *args)
        self.parent = parent
        self._value_on = value_on
        self._value_off = value_off
        self._key = key

        self._variable = tk.IntVar()
        self.configure(variable=self._variable, command=self._activate)

        self._activate()

    def _activate(self):
        if not self._variable.get():
            if self._key == "command":
                self.configure(command=lambda: (
                    self._value_on(),
                    self._activate()
                ))

            else:
                self.configure(**{self._key: self._value_on})

        if self._variable.get():
            if self._key == "command":
                self.configure(command=lambda: (
                    self._value_off(),
                    self._activate()
                ))

            else:
                self.configure(**{self._key: self._value_off})

    def toggle(self):
        """Switches the ToggleButton to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

    def turn_on(self):
        """Turns the ToggleButton on."""
        self._variable.set(True)
        self._activate()

    def turn_off(self):
        """Turns the ToggleButton off."""
        self._variable.set(False)
        self._activate()

    def get_state(self):
        """Gets the state of the ToggleButton."""
        if not self._variable.get():
            return False

        elif self._variable.get():
            return True

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbutton = ToggleButton(root)
    tbutton.pack(expand=True, padx=5, pady=5)
    root.mainloop()
