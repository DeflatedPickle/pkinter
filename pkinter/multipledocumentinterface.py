#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "MultipleDocumentInterface"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class MDIFrame(ttk.Frame):
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)


class MDIWindow(ttk.Frame):
    def __init__(self, mdi, *args, **kwargs):
        tk.Frame.__init__(self, mdi, *args, **kwargs)
        self.mdi = mdi

        self.border_colour = "cyan"

        self.title_size = 16
        self.border_size = 2

        self.button_width = 10
        self.button_height = 12

        self.border_dict = {}
        self.button_dict = {}
        self.frame_id = None

        for i in ["east", "south", "west"]:
            self.border_dict[i] = self.mdi.canvas.create_line((0, 0, 0, 0), width=self.border_size, fill=self.border_colour)

        self.is_drawn = False

    def float(self, x, y, width, height):
        if not self.is_drawn:
            self.border_dict["north"] = self.mdi.canvas.create_rectangle((0, 0, 0, 0), fill=self.border_colour, outline=self.border_colour)
            self.frame_id = self.mdi.canvas.create_window(0, 0, width=width, height=height, anchor="nw", window=self)

            self.mdi.canvas.tag_bind(self.border_dict["north"], "<Enter>",
                                     lambda _: self.mdi.canvas.configure(cursor="hand2"), "+")
            self.mdi.canvas.tag_bind(self.border_dict["north"], "<Leave>",
                                     lambda _: self.mdi.canvas.configure(cursor="arrow"), "+")
            self.mdi.canvas.tag_bind(self.border_dict["north"], "<B1-Motion>",
                                     lambda e: self.float(e.x, e.y, width, height), "+")

            self.is_drawn = True
            self.float(x, y, width, height)

        else:
            self.mdi.canvas.coords(self.border_dict["north"], (x - self.border_size,
                                                               y - self.title_size,
                                                               x - 1 + width + self.border_size,
                                                               y))
            self.mdi.canvas.coords(self.border_dict["east"], (x + width + self.border_size / 2,
                                                              y,
                                                              x + width + self.border_size / 2,
                                                              y + height))
            self.mdi.canvas.coords(self.border_dict["south"], (x - self.border_size,
                                                               y + height + self.border_size / 2,
                                                               x + width + self.border_size,
                                                               y + height + self.border_size / 2))
            self.mdi.canvas.coords(self.border_dict["west"], (x - self.border_size / 2,
                                                              y,
                                                              x - self.border_size / 2,
                                                              y + height))

            self.mdi.canvas.coords(self.frame_id, (x, y))


##################################################

if __name__ == "__main__":
    root = tk.Tk()

    mdi = MDIFrame(root)
    mdi.pack(expand=True, padx=5, pady=5)

    win = MDIWindow(mdi)
    ttk.Button(win).pack()
    win.float(80, 40, 80, 80)

    root.mainloop()
