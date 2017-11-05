#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ToasterBox"
__version__ = "1.7.0"
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
    def __init__(self, parent, width=350, minus_width=5, minus_height=5, extra_height=40, popup_fit=5, popup_pause=500, popup_padding=5, popup_height=100, *args):
        tk.Toplevel.__init__(self, parent, *args)
        self.parent = parent
        self._width = width
        self._minus_width = minus_width
        self._minus_height = minus_height
        self._extra_height = extra_height
        self._popup_fit = popup_fit
        self._popup_pause = popup_pause
        self._popup_padding = popup_padding
        self._popup_height = popup_height

        self.configure(background="green")

        self.attributes("-toolwindow", True, "-topmost", True)
        self.overrideredirect(True)

        self.geometry("{}x{}".format(self._width, self._popup_fit * (self._popup_height + (self._popup_padding * 2))))
        self.update()
        self.geometry("+{}+{}".format((self.winfo_screenwidth() - self.winfo_width()) - self._minus_width,
                                      (self.winfo_screenheight() - self.winfo_height()) - self._extra_height - self._minus_height))

    def create_popup(self, title="", image=None):
        popup = Popup(self, title=title, image=image, height=self._popup_height)
        popup.pack(side="bottom", fill="x", pady=self._popup_padding)

        return popup


class Popup(ttk.Frame):
    def __init__(self, parent, title, image, height, *args):
        ttk.Frame.__init__(self, parent, height=height, *args)
        self.parent = parent
        self._title = title
        self._image = image

        self.grid_propagate(False)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        image = ttk.Label(self, image=self._image)
        image.grid(row=0, column=0, rowspan=2)

        title_frame = ttk.Frame(self)
        title_frame.grid(row=0, column=1, sticky="we")

        label = ttk.Label(title_frame, text=self._title)
        label.pack(side="left", fill="both", expand=True)

        close = ttk.Button(title_frame, text="X", width=3, command=self.remove)
        close.pack(side="right")

    def remove(self, event=None):
        self.pack_forget()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tbox = ToasterBox(root)
    tbox.create_popup("Popup 1")
    tbox.create_popup("Popup 2")
    tbox.create_popup("Popup 3")
    root.mainloop()
