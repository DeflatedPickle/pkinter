#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

from pkinter import ToggleButton

# link

__title__ = "MultipleDocumentInterface"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class MDIFrame(ttk.Frame):
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True)


class MDIWindow(ttk.Frame):
    def __init__(self, mdi, *args, **kwargs):
        tk.Frame.__init__(self, mdi, *args, **kwargs)
        self._mdi = mdi

        self.x = None
        self.y = None
        self.width = None
        self.height = None

        self.is_maximized = False

        self.border_colour = "cyan"

        self.title_size = 16
        self.border_size = 2

        self.button_width = 10
        self.button_height = 12

        self.button_close = ttk.Button(command=self.close)
        self.button_maximize = ToggleButton(None, value_on=self.maximize, value_off=self.minimize, key="command")

        self.border_dict = {}
        self.button_dict = {}
        self.frame_id = None

        for i in ["east", "south", "west"]:
            self.border_dict[i] = self._mdi.canvas.create_line((0, 0, 0, 0), width=self.border_size,
                                                               fill=self.border_colour)

        self.is_drawn = False

    def float(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if not self.is_drawn:
            self.border_dict["north"] = self._mdi.canvas.create_rectangle((0, 0, 0, 0), fill=self.border_colour,
                                                                          outline=self.border_colour)
            self.frame_id = self._mdi.canvas.create_window(0, 0, width=width, height=height, anchor="nw", window=self)
            self.button_dict["close"] = self._mdi.canvas.create_window(0, 0, width=self.button_width,
                                                                       height=self.button_height, anchor="nw",
                                                                       window=self.button_close)
            self.button_dict["maximize"] = self._mdi.canvas.create_window(0, 0, width=self.button_width,
                                                                          height=self.button_height, anchor="nw",
                                                                          window=self.button_maximize)

            self._mdi.canvas.tag_bind(self.border_dict["north"], "<Enter>",
                                      lambda _: self._mdi.canvas.configure(cursor="hand2"), "+")
            self._mdi.canvas.tag_bind(self.border_dict["north"], "<Leave>",
                                      lambda _: self._mdi.canvas.configure(cursor="arrow"), "+")
            self._mdi.canvas.tag_bind(self.border_dict["north"], "<B1-Motion>",
                                      lambda e: (
                                          self.float(e.x, e.y, width, height),
                                          self.minimize() if self.is_maximized else None
                                      ), "+")

            self.is_drawn = True
            self.float(x, y, width, height)

        else:
            self._mdi.canvas.coords(self.border_dict["north"], (x - self.border_size,
                                                                y - self.title_size,
                                                                x - 1 + width + self.border_size,
                                                                y))
            self._mdi.canvas.coords(self.border_dict["east"], (x + width + self.border_size / 2,
                                                               y,
                                                               x + width + self.border_size / 2,
                                                               y + height))
            self._mdi.canvas.coords(self.border_dict["south"], (x - self.border_size,
                                                                y + height + self.border_size / 2,
                                                                x + width + self.border_size,
                                                                y + height + self.border_size / 2))
            self._mdi.canvas.coords(self.border_dict["west"], (x - self.border_size / 2,
                                                               y,
                                                               x - self.border_size / 2,
                                                               y + height))

            self._mdi.canvas.coords(self.button_dict["close"], (x + width - self.button_width,
                                                                y - self.button_height))
            self._mdi.canvas.coords(self.button_dict["maximize"], (x + width - self.button_width * 2,
                                                                   y - self.button_height))

            self._mdi.canvas.coords(self.frame_id, (x, y))

    def close(self):
        self._mdi.canvas.delete("all")

    def maximize(self):
        self.is_maximized = True
        self.button_maximize.turn_on()

        self._mdi.canvas.coords(self.frame_id, (0, self.title_size))
        self._mdi.canvas.itemconfig(self.frame_id, width=self._mdi.canvas.winfo_width(),
                                    height=self._mdi.canvas.winfo_height() - self.title_size)
        self._mdi.canvas.coords(self.border_dict["north"], (0, 0, self._mdi.canvas.winfo_width(), self.title_size))

        self._mdi.canvas.coords(self.button_dict["close"], (self._mdi.canvas.winfo_width() - self.button_width, 0))
        self._mdi.canvas.coords(self.button_dict["maximize"],
                                (self._mdi.canvas.winfo_width() - self.button_width * 2, 0))

    def minimize(self):
        self.is_maximized = False
        self.button_maximize.turn_off()

        self._mdi.canvas.coords(self.frame_id, (self.x, self.y))
        self._mdi.canvas.itemconfig(self.frame_id, width=self.width, height=self.height)
        self.float(self.x, self.y, self.width, self.height)


##################################################

if __name__ == "__main__":
    root = tk.Tk()

    mdi = MDIFrame(root)
    mdi.pack(expand=True, padx=5, pady=5)

    win = MDIWindow(mdi)
    ttk.Button(win).pack()
    win.float(80, 40, 80, 80)

    root.mainloop()
