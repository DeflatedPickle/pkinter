import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# http://docs.wxwidgets.org/3.1/classwx_file_picker_ctrl.html

__title__ = "FilePicker"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


class FilePicker(ttk.Frame):
    """
            -----DESCRIPTION-----
    A widget used to pick a file.

            -----USAGE-----
    filePicker = FilePicker(parent)
    filePicker.pack()

            -----PARAMETERS-----
    parent
    filetypes = The types of files the user can select.

            -----CONTENTS-----
    ---VARIABLES---
    variable  = Holds the picked file.

    ---WIDGETS---
    self
    entry     = The Entry used to show the picked file.
    button    = The Button that lets the user pick a file.

    ---FUNCTIONS---
    browse()  = Opens the file browser.
    get()     = Returns the value of variable.
    """
    def __init__(self, parent, filetypes=(("All Files", "*.*"), ("", "")), *args):
        ttk.Frame.__init__(self, parent, *args)
        self.filetypes = filetypes

        self.variable = tk.StringVar()

        self.entry = ttk.Entry(self, textvariable=self.variable)
        self.entry.pack(side="left", fill="x", expand=True)

        self.button = ttk.Button(self, text="Browse", command=self.browse)
        self.button.pack(side="right")

    def browse(self):
        file = filedialog.askopenfile(filetype=self.filetypes)
        self.variable.set(file.name)

    def get(self):
        return self.variable.get()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    fpicker = FilePicker(root)
    fpicker.pack(fill="x", expand=True, padx=5, pady=5)
    variable = tk.StringVar()
    label = ttk.Label(root, textvariable=variable)
    label.pack(expand=True, padx=5, pady=5)
    ttk.Button(root, text="Get", command=lambda: variable.set(fpicker.get())).pack(expand=True, padx=5, pady=5)
    root.mainloop()
