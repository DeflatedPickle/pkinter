#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ToasterBox"
__version__ = "1.2.0"
__author__ = "DeflatedPickle"


class ToasterBox(tk.Toplevel):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    template = ToasterBox(parent)

            -----PARAMETERS-----
    parent = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent = The parent of the widget.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, width=250, height=70, minus_width=5, minus_height=5, extra_height=40, popup_pause=500, popup_padding=5, *args):
        tk.Toplevel.__init__(self, parent, *args)
        self.parent = parent
        self._width = width
        self._height = height
        self._minus_width = minus_width
        self._minus_height = minus_height
        self._extra_height = extra_height
        self._popup_pause = popup_pause
        self._popup_padding = popup_padding

        self.configure(background="green")

        self.attributes("-toolwindow", True, "-topmost", True, "-disable", True)
        self.overrideredirect(True)

        self.update()
        self.geometry("{}x{}".format(self._width, self.winfo_height()))
        self.update()
        self.geometry("+{}+{}".format((self.winfo_screenwidth() - self.winfo_width()) - self._minus_width,
                                      (self.winfo_screenheight() - self.winfo_height()) - self._extra_height - self._minus_height))

    def create_popup(self):
        popup = Popup(self, height=self._height)
        popup.pack(fill="x", pady=self._popup_padding)


class Popup(ttk.Frame):
    def __init__(self, parent, height, *args):
        ttk.Frame.__init__(self, parent, height=height, *args)
        self.parent = parent

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbox = ToasterBox(root)
    tbox.create_popup()
    root.mainloop()
