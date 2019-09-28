#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import uuid

import tkinter as tk
from tkinter import ttk
from tkinter import font

from pkinter import ToggleButton

# link

__title__ = "MultipleDocumentInterface"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


# TODO: Use system colours for borders OR find a way to query how windows should look like
# TODO: Theme the buttons after the system title buttons
# TODO: Make the windows resizable using the borders


class MDIFrame(ttk.Frame):
    def __init__(self, parent, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent

        self.window_list = []
        self.focused_window = None

        self.colour_taskbar = "blue"
        self.taskbar_height = 20

        self.minimize_width = 60

        self.gap = 4

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        self.taskbar = self.canvas.create_rectangle((0, 0, 0, 0), fill=self.colour_taskbar,
                                                    outline=self.colour_taskbar)
        self.canvas.itemconfig(self.taskbar, state="hidden")

        self.canvas.bind("<Configure>", lambda e: self.canvas.coords(self.taskbar, (
            0, self.canvas.winfo_height() - self.taskbar_height, self.canvas.winfo_width(),
            self.canvas.winfo_height())))


class MDIWindow(ttk.Frame):
    def __init__(self, mdi, title, *args, **kwargs):
        ttk.Frame.__init__(self, mdi, *args, **kwargs)
        self._mdi = mdi
        self._title = title

        self.id = uuid.uuid4()

        self._mdi.window_list.append(self)

        self.font = font.nametofont(ttk.Style().lookup("TButton", "font")).copy()
        self.font.config(size=8)

        self.x = None
        self.y = None
        self.width = None
        self.height = None

        self.is_maximized = False
        self.is_minimized = False

        self.border_colour_focused = "cyan"
        self.border_colour_unfocused = "white"

        self.title_size = 16
        self.border_size = 2

        self.button_width = 10
        self.button_height = 12

        self.button_list = [ttk.Button(command=self.close),
                            ToggleButton(None, value_on=self.maximize, value_off=self.restore, key="command"),
                            ToggleButton(None, value_on=self.minimize, value_off=self.restore, key="command")]

        self.decoration_dict = {"border": {}, "button": {}}
        self.frame_id = None

        # TODO: Maybe use widgets for the borders so they don't get drawn underneath the content of other windows
        for i in ["east", "south", "west"]:
            self.decoration_dict["border"][i] = self._mdi.canvas.create_line((0, 0, 0, 0), width=self.border_size,
                                                                   fill=self.border_colour_focused, tags=self.id)
        self.decoration_dict["border"]["north"] = self._mdi.canvas.create_rectangle((0, 0, 0, 0),
                                                                                    fill=self.border_colour_focused,
                                                                                    outline=self.border_colour_focused,
                                                                                    tags=(self.id, f"title {self.id}"))

        for k, v in {"close": self.button_list[0], "maximize": self.button_list[1],
                     "minimize": self.button_list[2]}.items():
            self.decoration_dict["button"][k] = self._mdi.canvas.create_window(0, 0, width=self.button_width,
                                                                               height=self.button_height, anchor="w",
                                                                               window=v,
                                                                               tags=self.id)

        self.decoration_dict["border"]["title"] = self._mdi.canvas.create_text((0, 0), text=self._title, font=self.font,
                                                                     anchor="w", tags=(self.id, f"title {self.id}"))

        self._mdi.canvas.tag_bind(f"title {self.id}", "<Button-1>",
                                  lambda e: self.restore() if self.is_minimized else None)

        self.is_drawn = False

    def float(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.focus()

        if not self.is_drawn:
            self.frame_id = self._mdi.canvas.create_window(0, 0, width=width, height=height, anchor="nw", window=self,
                                                           tags=self.id)

            for i in ["north", "title"]:
                self._mdi.canvas.tag_bind(self.decoration_dict["border"][i], "<Enter>",
                                          lambda _: self._mdi.canvas.configure(cursor="hand2"), "+")
                self._mdi.canvas.tag_bind(self.decoration_dict["border"][i], "<Leave>",
                                          lambda _: self._mdi.canvas.configure(cursor="arrow"), "+")
                self._mdi.canvas.tag_bind(self.decoration_dict["border"][i], "<B1-Motion>",
                                          lambda e: (
                                              self.float(e.x, e.y, width, height),
                                              self.restore() if self.is_maximized or self.is_minimized else None,
                                              self.event_generate("<Configure>", when="tail")
                                          ), "+")

                self._mdi.canvas.tag_bind(self.id, "<Button-1>", lambda e: self.focus())
                self.bind("<Button-1>", lambda e: self.focus())

            self.is_drawn = True
            self.float(x, y, width, height)

        else:
            self._mdi.canvas.coords(self.decoration_dict["border"]["north"], (x - self.border_size,
                                                                              y - self.title_size,
                                                                              x - 1 + width + self.border_size,
                                                                              y))
            self._mdi.canvas.coords(self.decoration_dict["border"]["east"], (x + width + self.border_size / 2,
                                                                             y,
                                                                             x + width + self.border_size / 2,
                                                                             y + height))
            self._mdi.canvas.coords(self.decoration_dict["border"]["south"], (x - self.border_size,
                                                                              y + height + self.border_size / 2,
                                                                              x + width + self.border_size,
                                                                              y + height + self.border_size / 2))
            self._mdi.canvas.coords(self.decoration_dict["border"]["west"], (x - self.border_size / 2,
                                                                             y,
                                                                             x - self.border_size / 2,
                                                                             y + height))

            self._mdi.canvas.coords(self.decoration_dict["button"]["close"], (x + width - self.button_width,
                                                                              y - self.button_height / 2))
            self._mdi.canvas.coords(self.decoration_dict["button"]["maximize"], (x + width - self.button_width * 2,
                                                                                 y - self.button_height / 2))
            self._mdi.canvas.coords(self.decoration_dict["button"]["minimize"], (x + width - self.button_width * 3,
                                                                                 y - self.button_height / 2))

            self._mdi.canvas.coords(self.decoration_dict["border"]["title"], (x, y - self.font.metrics("linespace") / 2))

            self._mdi.canvas.coords(self.frame_id, (x, y))

    def close(self):
        self._mdi.canvas.delete(self.id)
        self.event_generate("<Destroy>", when="tail")

    def maximize(self):
        self.restore()

        self.is_maximized = True
        self.is_minimized = False

        self.button_list[1].turn_on()
        self.button_list[2].turn_off()

        self._mdi.canvas.coords(self.frame_id, (0, self.title_size))
        self._mdi.canvas.itemconfig(self.frame_id, width=self._mdi.canvas.winfo_width(),
                                    height=self._mdi.canvas.winfo_height() - self.title_size - self._mdi.taskbar_height)
        self._mdi.canvas.coords(self.decoration_dict["border"]["north"],
                                (0, 0, self._mdi.canvas.winfo_width(), self.title_size))

        self._mdi.canvas.coords(self.decoration_dict["button"]["close"],
                                (self._mdi.canvas.winfo_width() - self.button_width, self.button_height / 2))
        self._mdi.canvas.coords(self.decoration_dict["button"]["maximize"],
                                (self._mdi.canvas.winfo_width() - self.button_width * 2, self.button_height / 2))
        self._mdi.canvas.coords(self.decoration_dict["button"]["minimize"],
                                (self._mdi.canvas.winfo_width() - self.button_width * 3, self.button_height / 2))

        self._mdi.canvas.coords(self.decoration_dict["border"]["title"], (self.border_size, self.font.metrics("linespace") / 2))

        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["east"], state="hidden")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["south"], state="hidden")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["west"], state="hidden")

        self.event_generate("<<Maximize>>", when="tail")

    def restore(self):
        self.is_maximized = False
        self.is_minimized = False

        self.button_list[1].turn_off()
        self.button_list[2].turn_off()

        if self._mdi.focused_window == self:
            self.focus()

        self._mdi.canvas.tag_raise(self.id)

        for i in self._mdi.window_list:
            if i != self and i.is_minimized:
                i.minimize()

        self._mdi.canvas.coords(self.frame_id, (self.x, self.y))
        self._mdi.canvas.itemconfig(self.frame_id, width=self.width, height=self.height)

        self._mdi.canvas.itemconfig(self.frame_id, state="normal")

        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["east"], state="normal")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["south"], state="normal")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["west"], state="normal")

        self._mdi.canvas.itemconfig(self.decoration_dict["button"]["minimize"], state="normal")

        self.float(self.x, self.y, self.width, self.height)

        self.event_generate("<<Restore>>", when="tail")

    def minimize(self):
        self.restore()
        self.unfocus()

        x = 0
        for i in self._mdi.window_list:
            if i != self and i.is_minimized:
                x += self._mdi.minimize_width

                if x != 0:
                    x += self._mdi.gap

        self.is_maximized = False
        self.is_minimized = True

        self.button_list[1].turn_off()
        self.button_list[2].turn_on()

        self._mdi.canvas.coords(self.decoration_dict["border"]["north"], (
            x, self._mdi.canvas.winfo_height() - self._mdi.taskbar_height, x + self._mdi.minimize_width,
            self._mdi.canvas.winfo_height()))

        self._mdi.canvas.coords(self.decoration_dict["button"]["close"],
                                (x + self._mdi.minimize_width - self.button_width,
                                 self._mdi.canvas.winfo_height() - self.button_height))
        self._mdi.canvas.coords(self.decoration_dict["button"]["maximize"],
                                (x + self._mdi.minimize_width - self.button_width * 2,
                                 self._mdi.canvas.winfo_height() - self.button_height))

        self._mdi.canvas.coords(self.decoration_dict["border"]["title"], (
            x + self.border_size, self._mdi.canvas.winfo_height() - self.font.metrics("linespace")))

        self._mdi.canvas.itemconfig(self.frame_id, state="hidden")
        self._mdi.canvas.itemconfig(self.decoration_dict["button"]["minimize"], state="hidden")

        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["east"], state="hidden")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["south"], state="hidden")
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["west"], state="hidden")

        self.event_generate("<<Minimize>>", when="tail")

    def focus(self):
        self._mdi.canvas.tag_raise(self.id)
        self.lift()

        for i in self.button_list:
            i.lift()

        for i in self._mdi.window_list:
            if i != self:
                i.unfocus()

        self._mdi.focused_window = self

        for i in self.decoration_dict["border"]:
            if i != "title":
                self._mdi.canvas.itemconfig(self.decoration_dict["border"][i], fill=self.border_colour_focused)
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["north"], outline=self.border_colour_focused)

        self.event_generate("<FocusIn>", when="tail")

    def unfocus(self):
        if self._mdi.focused_window == self:
            self._mdi.focused_window = None

        for i in self.decoration_dict["border"]:
            if i != "title":
                self._mdi.canvas.itemconfig(self.decoration_dict["border"][i], fill=self.border_colour_unfocused)
        self._mdi.canvas.itemconfig(self.decoration_dict["border"]["north"], outline=self.border_colour_unfocused)

        self.event_generate("<FocusOut>", when="tail")


##################################################

if __name__ == "__main__":
    root = tk.Tk()

    mdi = MDIFrame(root)
    mdi.pack(fill="both", expand=True, padx=5, pady=5)

    win = MDIWindow(mdi, "Win")
    ttk.Button(win).pack()
    win.float(80, 40, 80, 80)
    win.bind("<Configure>", lambda e: print(f"Win was moved to: {e.x, e.y}"))
    win.bind("<Destroy>", lambda e: print("Win was closed"))
    win.bind("<Map>", lambda e: print("Win was made visible"))
    win.bind("<Unmap>", lambda e: print("Win was made invisible"))

    win2 = MDIWindow(mdi, "Win 2")
    ttk.Combobox(win2).pack()
    win2.float(220, 80, 80, 80)

    win3 = MDIWindow(mdi, "Win 3")
    win3.float(160, 140, 80, 80)

    root.mainloop()
