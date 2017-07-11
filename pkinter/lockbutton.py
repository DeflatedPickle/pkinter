#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkLockButton.html

__title__ = "LockButton"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class LockButton(ttk.Checkbutton):
    """
            -----DESCRIPTION-----
    A Button that can be locked.

            -----USAGE-----
    lockButton = LockButton(parent, lock_text=[string], lock_image=[string], unlock_text=[string], unlock_image=[string])
    lockButton.pack()

            -----PARAMETERS-----
    parent               = The parent of the widget.
    lock_text            = The text shown when the Button is unlocked.
    lock_image           = The image shown when the Button is unlocked.
    unlock_text          = The text shown when the Button is locked.
    unlock_image         = The image shown when the Button is locked.

            -----CONTENTS-----
    ---VARIABLES---
    parent               = The parent of the widget.
    _lock_text           = The text shown when the Button is unlocked.
    _lock_image          = The image shown when the Button is unlocked.
    _unlock_text         = The text shown when the Button is locked.
    _unlock_image        = The image shown when the Button is locked.

    ---TKINTER VARIABLES---
    _variable            = The variable used for the Button.

    ---WIDGETS---
    self

    ---FUNCTIONS---
    _activate()          = Checks the value of variable and locks or unlocks the Button.
    give_permissions()   = Gives the user permissions to interact with the Button.
    remove_permissions() = Removes the permission for the user to interact with the Button.
    toggle()             = Switches the Button to the opposite state.
    lock()               = Changes the Button to the locked state.
    unlock()             = Changes the Button to the unlocked state.
    get_state()          = Returns the state of the Button.
    """
    def __init__(self, parent, lock_text="Lock", lock_image="", unlock_text="Unlock", unlock_image="", *args):
        ttk.Checkbutton.__init__(self, parent, compound="left", command=self._activate, style="TButton", *args)
        self.parent = parent
        self._lock_text = lock_text
        self._unlock_text = unlock_text

        self._lock_image = tk.PhotoImage(file=lock_image)
        self._unlock_image = tk.PhotoImage(file=unlock_image)

        self._variable = tk.IntVar()
        self._variable.set(True)

        self.configure(variable=self._variable)

        self._activate()

    def _activate(self):
        if not self._variable.get():
            self.configure(text=self._unlock_text, image=self._unlock_image)

        if self._variable.get():
            self.configure(text=self._lock_text, image=self._lock_image)

    def give_permissions(self):
        """Gives the user permissions to use the Button."""
        self._activate()
        self.configure(state="enabled")

    def remove_permissions(self):
        """Removes the users permissions to use the Button."""
        self._activate()
        self.configure(state="disabled")

    def toggle(self):
        """Switches the LockButton to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

    def lock(self):
        """Locks the Button."""
        self._variable.set(True)
        self._activate()

    def unlock(self):
        """Unlocks the Button."""
        self._variable.set(False)
        self._activate()

    def get_state(self):
        """Gets the state of the Button."""
        if not self._variable.get():
            return "Locked"

        elif self._variable.get():
            return "Unlocked"

##################################################

if __name__ == "__main__":
    def function():
        print("Attempted Unlock")
        lbutton.unlock()

    root = tk.Tk()
    lbutton = LockButton(root)
    lbutton.pack(expand=True, padx=5, pady=5)
    button = ttk.Button(root, text="Get State", command=lambda: print(lbutton.get_state()))
    button.pack(side="left", expand=True, padx=5, pady=5)
    button2 = ttk.Button(root, text="Give Permissions", command=lbutton.give_permissions)
    button2.pack(side="left", expand=True, padx=5, pady=5)
    button3 = ttk.Button(root, text="Remove Permissions", command=lbutton.remove_permissions)
    button3.pack(side="left", expand=True, padx=5, pady=5)
    root.mainloop()
