#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

import re

# link

__title__ = "DocumentMap"
__version__ = "1.12.2"
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

        self._widget_text = self.create_text([self._text_pad, self._text_pad], font=self._text_font, anchor="nw", tags="original_text")

        self._text_widget.update()
        self._box = self._text_widget.bbox(1.0)
        self._handle = self.create_rectangle([0, self._box[1], self._width, self._box[3]], fill=self._scroll_fill, width=0, stipple="gray25", tags="handle")

        self.tag_bind("handle", "<Enter>", lambda event=None: self.configure(cursor="hand2"), "+")
        self.tag_bind("handle", "<Leave>", lambda event=None: self.configure(cursor="arrow"), "+")

        self.bind("<Button-1>", self._move, "+")
        self.bind("<B1-Motion>", self._move, "+")
        self.bind("<MouseWheel>", lambda e: self._move(e, "self"), "+")

        self._point = 0
        # True = Down
        # False = Up
        self._direction = False
        self.bind("<Button-1>", self._mark_point, "+")
        self.bind("<B1-Motion>", self._move_point, "+")
        self.bind("<MouseWheel>", self._move_point, "+")
        self._text_widget.bind("<MouseWheel>", self._move_point, "+")

        self.offset = 0
        self._height_offset = 0

        if self._collide == "harsh":
            self._harsh_collide()

        elif self._collide == "smooth":
            self._smooth_collide()

        self._text_widget.bind("<<Change>>", self._redraw, "+")
        self._text_widget.bind("<Configure>", self._redraw, "+")
        self._text_widget.bind("<KeyRelease>", self._redraw, "+")
        self._text_widget.bind("<MouseWheel>", self._move, "+")

        # self._work_out_handle()
        self._redraw()

    def _redraw(self, event=None):
        self.itemconfigure(self._widget_text, text=self._text_widget.get(1.0, "end"))

        self._work_out_handle()

    def _work_out_handle(self):
        self._handle_start = self._text_widget.index("@0,0")
        self._handle_end = self._text_widget.index("@0,{}".format(self._text_widget.winfo_height()))

        self._box = (0, float(self._handle_start), self._width, float(self._handle_end) * 4)

        # print(self._handle_start, self._handle_end)

    def _mark_point(self, event=None):
        self._point = self.coords(self._handle)[1]

    def _move_point(self, event=None):
        if event.delta == 0:
            temp = self._point - self.coords((self._handle))[1]

            if temp < 0:
                self._direction = True

            else:
                self._direction = False

            self._point = self.coords((self._handle))[1]

        else:
            if event.delta < 0:
                self._direction = True

            else:
                self._direction = False

    def _move(self, event=None, scroller="text"):
        self.update_idletasks()

        handle_height = self.coords(self._handle)[1]
        bounds = self.bbox(self._widget_text)
        height = bounds[3] - bounds[1]
        total_lines = int(self._text_widget.index("end-1c").split(".")[0])

        line = (handle_height / height) * total_lines

        start = float("{}.0".format(round(line - (self._height_offset / 4))))

        delta = event.delta / (total_lines * self._text_font[1] / 60)

        if self.winfo_height() < (total_lines * self._text_font[1]):
            delta = 0

            if event.delta == 0:
                scroll_amount = self.winfo_height() / (total_lines / self._text_font[1])

            else:
                scroll_amount = (total_lines / self._text_font[1]) / (abs(event.delta) / 16)

            if self._direction and self.offset < (total_lines / (self._text_font[1] / 2)):
                self.offset += 1
                # self.yview_scroll(1, "units")
                self._height_offset -= scroll_amount

            elif not self._direction and self.offset > 0:
                self.offset -= 1
                # self.yview_scroll(-1, "units")
                self._height_offset += scroll_amount

            self.coords(self._widget_text, self._text_pad, self._text_pad + self._height_offset)

        if event.delta != 0:
            c = self.coords(self._handle)
            self.coords(self._handle, c[0], c[1] - delta, c[2], c[3] - delta)

            if scroller == "self":
                self._text_widget.see(start)
                self._text_widget.see(start + float(self._handle_end))

        else:
            self._text_widget.see(start)
            self._text_widget.see(start + float(self._handle_end))

            self.coords(self._handle, self.coords(self._handle)[0], (event.y - self._box[3] / 2), self._box[2], (event.y + self._box[3] / 2))

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
