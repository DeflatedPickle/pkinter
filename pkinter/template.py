import tkinter as tk
from tkinter import ttk

# link

__title__ = "Template"
__version__ = "1.1.3"
__author__ = "DeflatedPickle"


class Template(ttk.Frame):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    template = Template(parent)
    template.pack()

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    temp = Template(root)
    temp.pack(expand=True, padx=5, pady=5)
    root.mainloop()
