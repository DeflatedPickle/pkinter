import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkToggleButton.html

__title__ = "ToggleButton"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class ToggleButton(ttk.Checkbutton):
    """
            -----DESCRIPTION-----
    A Button that can be toggled.

            -----USAGE-----
    toggleButton = ToggleButton(parent, text_on=[string], text_off=[string])
    toggleButton.pack()

            -----PARAMETERS-----
    parent
    text_on    = The text shown when the Button is toggled on.
    text_off   = The text shown when the Button is toggled off.

            -----CONTENTS-----
    ---VARIABLES---
    text_on    = The text shown when the Button is toggled on.
    text_off   = The text shown when the Button is toggled off.
    variable   = The variable used for the Button.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    activate() = Checks value of variable and shows or hides the Frame.
    toggle()   = Switches the LabelFrame to the opposite state.
    """
    def __init__(self, parent, text_on="On", text_off="Off", *args):
        ttk.Checkbutton.__init__(self, parent, style="TButton", *args)
        self.text_on = text_on
        self.text_off = text_off

        self.variable = tk.IntVar()
        self.configure(variable=self.variable, command=self.activate)

        self.activate()

    def activate(self):
        if not self.variable.get():
            self.configure(text=self.text_on)

        if self.variable.get():
            self.configure(text=self.text_off)

    def toggle(self):
        """
        Switches the LabelFrame to the opposite state.
        """
        self.variable.set(not self.variable.get())
        self.activate()

    def on(self):
        """
        Turns the Button on.
        """
        self.variable.set(True)
        self.activate()

    def off(self):
        """
        Turns the Button off.
        """
        self.variable.set(False)
        self.activate()

    def get_state(self):
        """
        Gets the state of the Button.
        """
        if not self.variable.get():
            return False

        elif self.variable.get():
            return True

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbutton = ToggleButton(root)
    tbutton.pack(expand=True, padx=5, pady=5)
    root.mainloop()
