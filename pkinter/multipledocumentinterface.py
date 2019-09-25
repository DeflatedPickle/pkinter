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

        self.window_list = []

        self.colour_taskbar = "blue"
        self.taskbar_height = 20

        self.minimize_width = 60

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True)

        self.taskbar = self.canvas.create_rectangle((0, 0, 0, 0), fill=self.colour_taskbar,
                                                    outline=self.colour_taskbar)

        self.canvas.bind("<Configure>", lambda e: self.canvas.coords(self.taskbar, (
            0, self.canvas.winfo_height() - self.taskbar_height, self.canvas.winfo_width(),
            self.canvas.winfo_height())))


class MDIWindow(ttk.Frame):
    def __init__(self, mdi, *args, **kwargs):
        ttk.Frame.__init__(self, mdi, *args, **kwargs)
        self._mdi = mdi

        self._mdi.window_list.append(self)

        self.x = None
        self.y = None
        self.width = None
        self.height = None

        self.is_maximized = False
        self.is_minimized = False

        self.border_colour = "cyan"

        self.title_size = 16
        self.border_size = 2

        self.button_width = 10
        self.button_height = 12

        self.button_close = ttk.Button(command=self.close)
        self.button_maximize = ToggleButton(None, value_on=self.maximize, value_off=self.restore, key="command")
        self.button_minimize = ToggleButton(None, value_on=self.minimize, value_off=self.restore, key="command")

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

            for k, v in {"close": self.button_close, "maximize": self.button_maximize,
                         "minimize": self.button_minimize}.items():
                self.button_dict[k] = self._mdi.canvas.create_window(0, 0, width=self.button_width,
                                                                     height=self.button_height, anchor="nw",
                                                                     window=v)

            self._mdi.canvas.tag_bind(self.border_dict["north"], "<Enter>",
                                      lambda _: self._mdi.canvas.configure(cursor="hand2"), "+")
            self._mdi.canvas.tag_bind(self.border_dict["north"], "<Leave>",
                                      lambda _: self._mdi.canvas.configure(cursor="arrow"), "+")
            self._mdi.canvas.tag_bind(self.border_dict["north"], "<B1-Motion>",
                                      lambda e: (
                                          self.float(e.x, e.y, width, height),
                                          self.restore() if self.is_maximized or self.is_minimized else None
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
            self._mdi.canvas.coords(self.button_dict["minimize"], (x + width - self.button_width * 3,
                                                                   y - self.button_height))

            self._mdi.canvas.coords(self.frame_id, (x, y))

    def close(self):
        self._mdi.canvas.delete("all")

    def maximize(self):
        self.restore()

        self.is_maximized = True
        self.is_minimized = False

        self.button_maximize.turn_on()
        self.button_minimize.turn_off()

        self._mdi.canvas.coords(self.frame_id, (0, self.title_size))
        self._mdi.canvas.itemconfig(self.frame_id, width=self._mdi.canvas.winfo_width(),
                                    height=self._mdi.canvas.winfo_height() - self.title_size - self._mdi.taskbar_height)
        self._mdi.canvas.coords(self.border_dict["north"], (0, 0, self._mdi.canvas.winfo_width(), self.title_size))

        self._mdi.canvas.coords(self.button_dict["close"], (self._mdi.canvas.winfo_width() - self.button_width, 0))
        self._mdi.canvas.coords(self.button_dict["maximize"],
                                (self._mdi.canvas.winfo_width() - self.button_width * 2, 0))
        self._mdi.canvas.coords(self.button_dict["minimize"],
                                (self._mdi.canvas.winfo_width() - self.button_width * 3, 0))

        self._mdi.canvas.itemconfig(self.border_dict["east"], state="hidden")
        self._mdi.canvas.itemconfig(self.border_dict["south"], state="hidden")
        self._mdi.canvas.itemconfig(self.border_dict["west"], state="hidden")

    def restore(self):
        self.is_maximized = False
        self.is_minimized = False

        self.button_maximize.turn_off()
        self.button_minimize.turn_off()

        for i in self._mdi.window_list:
            if i != self and i.is_minimized:
                i.minimize()

        self._mdi.canvas.coords(self.frame_id, (self.x, self.y))
        self._mdi.canvas.itemconfig(self.frame_id, width=self.width, height=self.height)

        self._mdi.canvas.itemconfig(self.frame_id, state="normal")

        self._mdi.canvas.itemconfig(self.border_dict["east"], state="normal")
        self._mdi.canvas.itemconfig(self.border_dict["south"], state="normal")
        self._mdi.canvas.itemconfig(self.border_dict["west"], state="normal")

        self._mdi.canvas.itemconfig(self.button_dict["minimize"], state="normal")

        self.float(self.x, self.y, self.width, self.height)

    def minimize(self):
        self.restore()

        x = 0
        for i in self._mdi.window_list:
            if i != self and i.is_minimized:
                x += self._mdi.minimize_width

        self.is_maximized = False
        self.is_minimized = True

        self.button_maximize.turn_off()
        self.button_minimize.turn_on()

        self._mdi.canvas.coords(self.border_dict["north"], (
            x, self._mdi.canvas.winfo_height() - self._mdi.taskbar_height, x + self._mdi.minimize_width,
            self._mdi.canvas.winfo_height()))

        self._mdi.canvas.coords(self.button_dict["close"], (x + self._mdi.minimize_width - self.button_width,
                                                            self._mdi.canvas.winfo_height() - self.button_height))
        self._mdi.canvas.coords(self.button_dict["maximize"], (x + self._mdi.minimize_width - self.button_width * 2,
                                                               self._mdi.canvas.winfo_height() - self.button_height))

        self._mdi.canvas.itemconfig(self.frame_id, state="hidden")
        self._mdi.canvas.itemconfig(self.button_dict["minimize"], state="hidden")

        self._mdi.canvas.itemconfig(self.border_dict["east"], state="hidden")
        self._mdi.canvas.itemconfig(self.border_dict["south"], state="hidden")
        self._mdi.canvas.itemconfig(self.border_dict["west"], state="hidden")


##################################################

if __name__ == "__main__":
    root = tk.Tk()

    mdi = MDIFrame(root)
    mdi.pack(fill="both", expand=True, padx=5, pady=5)

    win = MDIWindow(mdi)
    ttk.Button(win).pack()
    win.float(80, 40, 80, 80)

    win2 = MDIWindow(mdi)
    ttk.Combobox(win2).pack()
    win2.float(220, 80, 80, 80)

    root.mainloop()
