#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "DocumentMap"
__version__ = "1.10.0"
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
    def __init__(self, parent, text_widget, scroll_widget=None, scroll_fill="orange", text_font=("courier", 3), text_pad=5, collide="harsh", scroll="text", background="white", width=170, *args):
        tk.Canvas.__init__(self, parent, background=background, width=width, *args)
        self.parent = parent
        self._text_widget = text_widget
        self._scroll_widget = scroll_widget
        self._scroll_fill = scroll_fill
        self._text_font = text_font
        self._text_pad = text_pad
        self._collide = collide
        self._scroll = scroll
        self._width = width

        self._widget_text = self.create_text([self._text_pad, self._text_pad], font=self._text_font, anchor="nw", tags="text")

        self._text_widget.update()
        self._box = self._text_widget.bbox(1.0)
        self._handle = self.create_rectangle([0, self._box[1], self._width, self._box[3]], fill=self._scroll_fill, width=0, stipple="gray25", tags="handle")

        self.tag_bind("handle", "<Enter>", lambda event=None: self.configure(cursor="hand2"), "+")
        self.tag_bind("handle", "<Leave>", lambda event=None: self.configure(cursor="arrow"), "+")

        self.bind("<Button-1>", self._move, "+")
        self.bind("<B1-Motion>", self._move, "+")

        if self._collide == "harsh":
            self._harsh_collide()

        elif self._collide == "smooth":
            self._smooth_collide()

        self._text_widget.bind("<<Change>>", self._redraw, "+")
        self._text_widget.bind("<Configure>", self._redraw, "+")
        self._text_widget.bind("<KeyRelease>", self._redraw, "+")

        self._work_out_handle()

    def _redraw(self, event=None):
        self.itemconfigure(self._widget_text, text=self._text_widget.get(1.0, "end"))

        self._work_out_handle()

    def _work_out_handle(self):
        self._handle_start = self._text_widget.index(self._text_widget.index("@0,0"))
        self._handle_end = self._text_widget.index(self._text_widget.index("@0,{}".format(self._text_widget.winfo_height())))

        self._box = (0, float(self._handle_start), self._width, float(self._handle_end) * 4)

        # print(self._handle_start, self._handle_end)

    def _move(self, event=None):
        # self._work_out_handle()

        # print(self._handle_start, self._handle_end)

        self.coords(self._handle, self.coords(self._handle)[0], event.y - self._box[3] / 2, self._box[2], event.y + self._box[3] / 2)

        self.update_idletasks()

        handle = self.coords(self._handle)[1]
        bounds = self.bbox(self._widget_text)
        height = bounds[3] - bounds[1]
        total_lines = int(self._text_widget.index("end-1c").split(".")[0])

        line = (handle / height) * total_lines

        start = float("{}.0".format(round(line)))

        self._text_widget.see(start)
        self._text_widget.see(start + float(self._handle_end))

        if self.coords(self._handle)[1] < 0 and self._handle_start != self._handle_start:
            self.yview("scroll", -1, "units")

        elif self.coords(self._handle)[3] > self.winfo_height() and self._handle_end != self._handle_end:
            self.yview("scroll", 1, "units")

    def _smooth_collide(self, interval=60):
        if self.coords(self._handle)[1] <= 0:
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], c[1] + 1, c[2], c[3] + 1)

        elif self.coords(self._handle)[3] >= self._scroll_height():
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], c[1] - 1, c[2], c[3] - 1)

        self.after(interval, self._smooth_collide)

    def _harsh_collide(self, interval=1, event=None):

        if self.coords(self._handle)[1] <= 0:
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], 0, c[2], self._box[3])

        elif self.coords(self._handle)[3] >= self._scroll_height():
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], self._scroll_height() - self._box[3], c[2], self._scroll_height())

        self.after(interval, self._harsh_collide)

    def _scroll_height(self):
        return self.bbox(self._widget_text)[3] if self._scroll == "text" else self.winfo_height() if self._scroll == "all" else None

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    text = tk.Text(root, width=1, height=1, wrap="none")
    text.pack(side="left", fill="both", expand=True, padx=[5, 0], pady=5)
    with open("documentmap.py") as file:
        text.insert(1.0, file.read())
    vscroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
    vscroll.pack(side="left", fill="y", pady=5)
    text.configure(yscrollcommand=vscroll.set)
    dmap = DocumentMap(root, text_widget=text, scroll_widget=vscroll)
    dmap.pack(side="right", fill="y", padx=[0, 5], pady=5)
    root.mainloop()
