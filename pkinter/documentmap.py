#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "DocumentMap"
__version__ = "1.5.0"
__author__ = "DeflatedPickle"


class DocumentMap(tk.Canvas):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    template = Template(parent)
    template.pack()

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
    def __init__(self, parent, text_widget, scroll_widget=None, scroll_fill="orange", text_font=("courier", 7), text_pad=5, background="white", width=170, *args):
        tk.Canvas.__init__(self, parent, background=background, width=width, *args)
        self.parent = parent
        self._text_widget = text_widget
        self._scroll_widget = scroll_widget
        self._scroll_fill = scroll_fill
        self._text_font = text_font
        self._text_pad = text_pad
        self._width = width

        self._widget_text = self.create_text([self._text_pad, self._text_pad], text=self._text_widget.get(1.0, "end"), font=self._text_font, anchor="nw", tags="text")

        self._handle = self.create_rectangle([0, 0, self._width, 70], fill=self._scroll_fill, width=0, stipple="gray25", tags="handle")
        self.tag_bind("handle", "<Enter>", lambda event=None: self.configure(cursor="hand2"), "+")
        self.tag_bind("handle", "<Leave>", lambda event=None: self.configure(cursor="arrow"), "+")

        self.bind("<Button-1>", self._move, "+")
        self.bind("<B1-Motion>", self._move, "+")

        self._text_widget.bind("<<Change>>", self._redraw, "+")
        self._text_widget.bind("<Configure>", self._redraw, "+")
        self._text_widget.bind("<KeyRelease>", self._redraw, "+")

        self._collide()

    def _redraw(self, event=None):
        self.itemconfigure(self._widget_text, text=self._text_widget.get(1.0, "end"))

    def _move(self, event=None):
        self.coords(self._handle, self.coords(self._handle)[0], event.y - 35, self.coords(self._handle)[0] + self._width, event.y + 35)

    def _collide(self, interval=60):
        # FIXME: Make this a harsh collision.
        if self.coords(self._handle)[1] <= 0:
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], c[1] + 1, c[2], c[3] + 1)

        elif self.coords(self._handle)[3] >= self.winfo_height():
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], c[1] - 1, c[2], c[3] - 1)

        self.after(interval, self._collide)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    text = tk.Text(root, width=1, height=1)
    text.pack(side="left", fill="both", expand=True, padx=[5, 0], pady=5)
    for i in range(0, 100):
        text.insert("{}.0".format(i), "{}\n".format(i))
    vscroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
    vscroll.pack(side="left", fill="y", pady=5)
    text.configure(yscrollcommand=vscroll.set)
    dmap = DocumentMap(root, text_widget=text, scroll_widget=vscroll)
    dmap.pack(side="right", fill="y", padx=[0, 5], pady=5)
    root.mainloop()
