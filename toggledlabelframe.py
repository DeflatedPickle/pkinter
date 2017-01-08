import tkinter as tk
from tkinter import ttk

#http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-LabelFrame.html

__title__ = "ToggledLabelFrame"
__author__ = "DeflatedPickle"
__version__ = "0.1.0"

class ToggledLabelFrame (ttk.LabelFrame):
    """
            -----DESCRIPTION-----
    This widget is used to store any other widgets inside of it.
    It can be toggled on or off, so widgets inside of it aren't always shown.

            -----USAGE-----
    toggledFrame = ToggledLabelFrame (parent, ontext = [string], offtext = [string], defaultstate = [boolean])
    toggledFrame.pack ()
    button = Button (toggledFrame.subframe).pack ()

            -----CONTENTS-----
    ---VARIABLES---
    ontext       = The text displayed when the button is active.
    offtext      = The text displayed when the button is inactive.
    defaultstate = The state the widget starts on.
    state        = The state of the button.
    variable     = The variable used for the button.

    ---WIDGETS---
    Self
    fill         = A placeholder.
    button       = The button that toggles the subframe.
    subframe     = The frame which holds widgets.

    ---FUNCTIONS---
    activate ()  = Checks value of variable and shows or hides the frame.
    toggle ()    = Toggles the button.
    """
    def __init__ (self, parent, ontext = "Active", offtext = "Inactive", defaultstate = False, state = "enabled", *args):
        ttk.LabelFrame.__init__ (self, parent, labelanchor = "n", *args)
        self.ontext = ontext
        self.offtext = offtext
        self.defaultstate = defaultstate
        self.state = state

        self.fill = tk.Frame (self, height = 5)

        self.variable = tk.IntVar ()
        self.variable.set (self.defaultstate)

        self.button = ttk.Checkbutton (self, width = 11, state = self.state, variable = self.variable, command = self.activate, style = "TButton")
        self.configure (labelwidget = self.button)

        self.subframe = ttk.Frame (self)

        self.activate ()

    def activate (self):
        if self.variable.get () == False:
            self.fill.pack ()
            self.subframe.forget ()
            self.button.configure (text = self.ontext)

        if self.variable.get () == True:
            self.fill.forget ()
            self.subframe.pack (fill = "both", expand = True)
            self.button.configure (text = self.offtext)

    def toggle (self):
        self.variable.set (not self.variable.get ())
        self.activate ()

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    tframeoff = ToggledLabelFrame (root, ontext = "Off", offtext = "On", defaultstate = False, state = "enabled")
    tframeoff.grid (row = 0, column = 0, padx = 5, pady = 5)
    ttk.Button (tframeoff.subframe).pack ()
    ttk.Button (tframeoff.subframe).pack ()
    ttk.Button (tframeoff.subframe).pack ()

    tframeon = ToggledLabelFrame (root, ontext = "Off", offtext = "On", defaultstate = True, state = "enabled")
    tframeon.grid (row = 0, column = 1, padx = 5, pady = 5)
    ttk.Button (tframeon.subframe).pack ()
    ttk.Entry (tframeon.subframe).pack ()

    tframeoff = ToggledLabelFrame (root, ontext = "Off", offtext = "On", defaultstate = False, state = "disabled")
    tframeoff.grid (row = 2, column = 0, padx = 5, pady = 5)
    ttk.Button (tframeoff.subframe).pack ()
    ttk.Combobox (tframeoff.subframe).pack ()
    ttk.Button (tframeoff.subframe).pack ()

    togglebutton = ttk.Button (root, text = "Toggle", command = tframeoff.toggle)
    togglebutton.grid (row = 1, column = 0)

    tframeon = ToggledLabelFrame (root, ontext = "Off", offtext = "On", defaultstate = True, state = "disabled")
    tframeon.grid (row = 2, column = 1, padx = 5, pady = 5)
    ttk.Button (tframeon.subframe).pack ()
    root.mainloop ()
