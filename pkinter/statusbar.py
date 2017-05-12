#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "Statusbar"
__version__ = "1.3.3"
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
    parent

    ---WIDGETS---
    self

    ---FUNCTIONS---
    add_label()      = Adds a Label to the Statusbar.
    add_variable()   = Adds a Label with a textvariable.
    bind_widget()    = Binds a widget to change the value of an added variable.
    bind_menu()      = Binds a menu to change the value of an added variable.
    add_sizegrip()   = Adds a SizeGrip to the Statusbar.
    add_separator()  = Adds a Separator to the Statusbar.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

    def add_label(self, text="", image="", side="left"):
        """Adds a Label to the Statusbar."""
        widget = ttk.Label(self, text=text, image=image)
        widget.pack(side=side)

        return widget

    def add_variable(self, textvariable=None, side="left"):
        """Adds a Label controlled by a variable to the Statusbar."""
        widget = ttk.Label(self, textvariable=textvariable)
        widget.pack(side=side)

        return widget

    def add_sizegrip(self, side="right", anchor="s"):
        """Adds a SizeGrip to the Statusbar."""
        widget = ttk.Sizegrip(self)
        widget.pack(side=side, anchor=anchor)

        return widget

    def add_separator(self):
        """Adds a Separator to the Statusbar."""
        widget = ttk.Separator(self, orient="vertical")
        widget.pack(side="left", fill="y", padx=3, pady=1)

        return widget

    def bind_widget(self, widget, variable, enter_text, leave_text):
        """Binds a widget to change the text of a variable."""
        widget.bind("<Enter>", lambda *args: variable.set(enter_text), "+")
        widget.bind("<Leave>", lambda *args: variable.set(leave_text), "+")

    def bind_menu(self, menu, variable, options=[]):
        """Binds a menu to change the text of a variable."""
        menu.bind("<<MenuSelect>>", lambda event: self.menu_select(event, variable=variable, options=options), "+")

    def menu_select(self, event, variable, options):
        index = self.parent.call(event.widget, "index", "active")
        if index != "none":
            try:
                variable.set(options[index])
            except IndexError:
                pass
        else:
            variable.set("")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    button = ttk.Button(root, text="Bound")
    button.pack(padx=5, pady=5)

    menu = tk.Menu(root, type="menubar")
    filemenu = tk.Menu(menu)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Save")
    menu.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menu)
    helpmenu.add_checkbutton(label="About")
    menu.add_cascade(label="Help", menu=helpmenu)
    root.configure(menu=menu)

    sbar = Statusbar(root)
    sbar.pack(expand=True, fill="x", padx=5, pady=5)
    variable = tk.StringVar()
    sbar.add_variable(textvariable=variable)
    sbar.bind_menu(menu, variable, ["Open the File menu.", "Open the Help menu."])
    sbar.bind_menu(filemenu, variable, ["Tear-off the menu.", "Create a new file.", "Save the current file."])
    sbar.bind_menu(helpmenu, variable, ["Tear-off the menu.", "Open the About window."])
    sbar.bind_widget(button, variable, "This is a Button.", "")
    sbar.add_separator()
    sbar.add_label(text="A Label")
    sbar.add_sizegrip(side="right")
    root.mainloop()
