import tkinter as tk
from tkinter import ttk

#link

__title__ = "EditableLabel"
__version__ = "0.1.0"
__author__ = "DeflatedPickle"

class EditableLabel (ttk.Label):
    """
            -----DESCRIPTION-----
    A label that you can edit the text of.

            -----USAGE-----
    editableLabel = EditableLabel (parent, text = [string], doesresize = [boolean])
    editableLabel.pack ()

            -----CONTENTS-----
    ---VARIABLES---
    text       = The text of the label starts with.
    doesresize = Determines whether the entry resizes with to the text.
    variable   = The text inside of the entry.

    ---WIDGETS---
    Self
    entry      = The entry.

    ---FUNCTIONS---
    edit ()    = Opens the entry.
    confirm () = Closes the entry.
    resize ()  = Resizes the entry to the text inside.
    """
    def __init__ (self, parent, text = "Edit", doesresize = False, *args):
        ttk.Label.__init__ (self, parent, *args)
        self.text = text
        self.doesresize = doesresize

        self.variable = tk.StringVar ()
        self.configure (textvariable = self.variable)
        self.variable.set (self.text)

        self.entry = ttk.Entry (self, textvariable = self.variable)

        self.bind ("<Double-Button-1>", self.edit)
        self.bind ("<Enter>", self.configure (cursor = "hand2"))
        self.entry.bind ("<FocusOut>", self.confirm)
        self.entry.bind ("<Return>", self.confirm)

        if self.doesresize == True:
            self.entry.bind ("<Key>", self.resize)
            self.resize ()

        self.configure (width = self.entry.cget ("width"))

    def edit (self, *args):
        self.entry.pack (fill = "both")
        self.entry.focus_force ()
        self.entry.icursor ("end")

    def confirm (self, *args):
        self.entry.pack_forget ()
        self.configure (width = self.entry.cget ("width"))

    def resize (self, *args):
        self.entry.configure (width = len (str (self.variable.get ())) + 1)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    elabel = EditableLabel (root, doesresize = False)
    elabel.grid (row = 0, column = 0, padx = 5, pady = 5)
    root.mainloop ()
