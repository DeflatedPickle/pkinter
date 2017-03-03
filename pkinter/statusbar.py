import tkinter as tk
from tkinter import ttk

# link

__title__ = "Statusbar"
__version__ = "1.2.2"
__author__ = "DeflatedPickle"


class Statusbar(ttk.Frame):
    """
            -----DESCRIPTION-----
    The Statusbar can be used to show certain variables.

            -----USAGE-----
    statusbar = Statusbar(parent)
    statusbar.pack()
    statusbar.add_label(text=[string], textvariable=[string], image=[string], side=[string])
    statusbar.add_separator()

            -----PARAMETERS-----
    parent

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    add_label()      = Adds a Label to the Statusbar.
    add_variable()   = Adds a Label with a textvariable.
    bind_widget()    = Binds a widget to a <Enter> and <Leave> event.
    add_sizegrip()   = Adds a SizeGrip to the Statusbar.
    add_separator()  = Adds a Separator to the Statusbar.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)

    def add_label(self, text="", textvariable=None, image="", side="left"):
        """
        Adds a Label to the Statusbar.
        """
        ttk.Label(self, text=text, textvariable=textvariable, image=image).pack(side=side)

    def add_variable(self, textvariable=None, side="left"):
        """
        Adds a Label controlled by a variable to the Statusbar.
        """
        ttk.Label(self, textvariable=textvariable).pack(side=side)

    def bind_widget(self, widget, variable, enter_text, leave_text):
        """
        Binds a widget to change the text of an added variable.
        """
        widget.bind("<Enter>", lambda *args: variable.set(enter_text))
        widget.bind("<Leave>", lambda *args: variable.set(leave_text))

    def add_sizegrip(self, side="right", anchor="s"):
        """
        Adds a SizeGrip to the Statusbar.
        """
        ttk.Sizegrip(self).pack(side=side, anchor=anchor)

    def add_separator(self):
        """
        Adds a Separator to the Statusbar.
        """
        ttk.Separator(self, orient="vertical").pack(side="left", fill="y", padx=3, pady=1)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    button = ttk.Button(root, text="Bound")
    button.pack(padx=5, pady=5)

    sbar = Statusbar(root)
    sbar.pack(expand=True, fill="x", padx=5, pady=5)
    variable = tk.StringVar()
    sbar.add_label(textvariable=variable)
    sbar.bind_widget(button, variable, "This is a Button.", "")
    sbar.add_separator()
    sbar.add_label(text="A Label")
    sbar.add_sizegrip(side="right")
    root.mainloop()
