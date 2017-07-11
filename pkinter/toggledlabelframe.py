#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-LabelFrame.html

__title__ = "ToggledLabelFrame"
__version__ = "1.2.5"
__author__ = "DeflatedPickle"


class ToggledLabelFrame(ttk.LabelFrame):
    """
            -----DESCRIPTION-----
    This widget is used to store any other widgets inside of it.
    It can be toggled on or off, so widgets inside of it aren't always shown.

            -----USAGE-----
    toggledFrame = ToggledLabelFrame(parent, on_text=[string], off_text=[string], default_state=[boolean], state="enabled")
    toggledFrame.pack()
    button = Button(toggledFrame.frame).pack()

            -----PARAMETERS-----
    parent         = The parent of the widget.
    on_text        = The text displayed when the button is active.
    off_text       = The text displayed when the button is inactive.
    default_state  = The state the widget starts on.
    state          = The state of the button.

            -----CONTENTS-----
    ---VARIABLES---
    parent         = The parent of the widget.
    _on_text       = The text displayed when the button is active.
    _off_text      = The text displayed when the button is inactive.
    _default_state = The state the widget starts on.
    _state         = The state of the button.

    ---TKINTER VARIABLES---
    variable       = The variable used for the Button.

    ---WIDGETS---
    self
    _fill          = A placeholder.
    _button        = The button that toggles the frame.
    _frame         = The frame which holds widgets.

    ---FUNCTIONS---
    _activate()    = Checks value of variable and shows or hides the frame.
    toggle()       = Switches the label frame to the opposite state.
    """
    def __init__(self, parent, on_text="Active", off_text="Inactive", default_state=False, state="enabled", *args):
        ttk.LabelFrame.__init__(self, parent, labelanchor="n", *args)
        self.parent = parent
        self._on_text = on_text
        self._off_text = off_text
        self._default_state = default_state
        self._state = state

        self._fill = tk.Frame(self, height=5)

        self._variable = tk.IntVar()
        self._variable.set(default_state)

        self._button = ttk.Checkbutton(self, width=11, state=self._state, variable=self._variable, command=self._activate, style="TButton")
        self.configure(labelwidget=self._button)

        self.frame = ttk.Frame(self)

        self._activate()

    def _activate(self):
        if not self._variable.get():
            self._fill.pack()
            self.frame.forget()
            self._button.configure(text=self._off_text)

        if self._variable.get():
            self._fill.forget()
            self.frame.pack(fill="both", expand=True)
            self._button.configure(text=self._on_text)

    def toggle(self):
        """Switches the LabelFrame to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tframe = ToggledLabelFrame(root, on_text="Off", off_text="On", default_state=False, state="enabled")
    tframe.pack(expand=True, padx=5, pady=5)
    for i in range(3):
        ttk.Button(tframe.frame).pack()
    root.mainloop()
