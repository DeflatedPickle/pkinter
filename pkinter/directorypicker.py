import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# http://docs.wxwidgets.org/3.1/classwx_dir_picker_ctrl.html

__title__ = "DirectoryPicker"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class DirectoryPicker(ttk.Frame):
    """
            -----DESCRIPTION-----
    A widget used to pick a directory.

            -----USAGE-----
    directoryPicker = DirectoryPicker(parent)
    directoryPicker.pack()

            -----PARAMETERS-----
    parent

            -----CONTENTS-----
    ---VARIABLES---
    variable = Holds the picked directory.

    ---WIDGETS---
    self
    entry    = The Entry used to show the picked directory.
    button   = The Button that lets the user pick a directory.

    ---FUNCTIONS---
    browse() = Opens the directory browser.
    get()    = Returns the value of variable.
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)

        self.variable = tk.StringVar()

        self.entry = ttk.Entry(self, textvariable=self.variable)
        self.entry.pack(side="left", fill="x", expand=True)

        self.button = ttk.Button(self, text="Browse", command=self.browse)
        self.button.pack(side="right")

    def browse(self):
        """
        Opens a directory browser.
        """
        directory = filedialog.askdirectory()
        self.variable.set(directory)

    def get(self):
        """
        Returns the chosen directory.
        """
        return self.variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    dpicker = DirectoryPicker(root)
    dpicker.pack(fill="x", expand=True, padx=5, pady=5)
    variable = tk.StringVar()
    label = ttk.Label(root, textvariable=variable)
    label.pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Get", command=lambda: variable.set(dpicker.get())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
