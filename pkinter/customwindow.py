import tkinter as tk
from tkinter import ttk

# link

__title__ = "CustomWindow"
__version__ = "1.0.3"
__author__ = "DeflatedPickle"


class CustomWindow(tk.Tk):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__(self, bordercolour="dark grey", borderspan=5, *args):
        tk.Tk.__init__(self, *args)
        self.bordercolour = bordercolour
        self.borderspan = borderspan
        self.overrideredirect(True)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Style().configure("Border.TFrame", background=self.bordercolour)

        self.nwf = ttk.Frame(self, width=self.borderspan, height=self.borderspan, style="Border.TFrame")
        self.nwf.grid(row=0, column=0, sticky="nesw")
        self.nf = ttk.Frame(self, height=self.borderspan, style="Border.TFrame")
        self.nf.grid(row=0, column=1, sticky="nesw")
        self.nef = ttk.Frame(self, width=self.borderspan, height=self.borderspan, style="Border.TFrame")
        self.nef.grid(row=0, column=2, sticky="nesw")

        self.wf = ttk.Frame(self, width=self.borderspan, style="Border.TFrame")
        self.wf.grid(row=1, column=0, sticky="nesw")

        self.inf = ttk.Frame(self)
        self.inf.grid(row=1, column=1, sticky="nesw")

        self.ef = ttk.Frame(self, width=self.borderspan, style="Border.TFrame")
        self.ef.grid(row=1, column=2, sticky="nesw")

        self.swf = ttk.Frame(self, width=self.borderspan, height=self.borderspan, style="Border.TFrame")
        self.swf.grid(row=2, column=0, sticky="nesw")
        self.sf = ttk.Frame(self, height=self.borderspan, style="Border.TFrame")
        self.sf.grid(row=2, column=1, sticky="nesw")
        self.sef = ttk.Frame(self, width=self.borderspan, height=self.borderspan, style="Border.TFrame")
        self.sef.grid(row=2, column=2, sticky="nesw")

##################################################

if __name__ == "__main__":
    cwindow = CustomWindow()
    ttk.Button(cwindow.inf).pack()
    cwindow.mainloop()
