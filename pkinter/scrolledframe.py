#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "ScrolledFrame"
__version__ = "1.0.2"
__author__ = "DeflatedPickle"


class ScrolledFrame(ttk.Frame):
    """
            -----DESCRIPTION-----
    A scroll-able frame.

            -----USAGE-----
    sframe = ScrolledFrame(parent)
    sframe.pack()

            -----PARAMETERS-----
    parent = The parent of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    parent = The parent of the widget.
    _xscrollcommand = The horizontal scroll command.
    _yscrollcommand = The vertical scroll command.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self
    _canvas = The Canvas that the Frame is placed into.
    frame = The Frame that widgets should be placed into.

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, xscrollcommand=None, yscrollcommand=None, *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._xscrollcommand = xscrollcommand
        self._yscrollcommand = yscrollcommand

        self._canvas = tk.Canvas(self, width=0, height=0, borderwidth=0, background="pink", highlightthickness=0, xscrollcommand=self._xscrollcommand, yscrollcommand=self._yscrollcommand)
        self._canvas.pack(fill="both", expand=True)

        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

        self.frame = ttk.Frame(self._canvas, width=0, height=0)
        self._frame_id = self._canvas.create_window(0, 0, window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self._configure_frame)
        # self._canvas.bind("<Configure>", self._configure_canvas)

        self.configure = self._canvas.configure
        self.xview = self._canvas.xview
        self.yview = self._canvas.yview

    def _configure_frame(self, event=None):
        size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
        self._canvas.config(scrollregion="0 0 %s %s" % size)

        if self.frame.winfo_reqwidth() != self._canvas.winfo_width():
            self._canvas.config(width=self.frame.winfo_reqwidth())

        if self.frame.winfo_reqheight() != self._canvas.winfo_height():
            self._canvas.config(height=self.frame.winfo_reqheight())

    def _configure_canvas(self, event=None):
        if self.frame.winfo_reqwidth() != self._canvas.winfo_width():
            self._canvas.itemconfigure(self._frame_id, width=self._canvas.winfo_width())

        if self.frame.winfo_reqheight() != self._canvas.winfo_height():
            self._canvas.itemconfigure(self._frame_id, height=self._canvas.winfo_height())

##################################################

if __name__ == "__main__":
    root = tk.Tk()

    frame = ttk.Frame(root)
    frame.pack(expand=True, padx=5, pady=5)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    hscroll = ttk.Scrollbar(frame, orient="horizontal")
    hscroll.grid(row=1, column=0, sticky="ew")

    vscroll = ttk.Scrollbar(frame)
    vscroll.grid(row=0, column=1, sticky="ns")

    sframe = ScrolledFrame(frame, xscrollcommand=hscroll.set, yscrollcommand=vscroll.set)
    sframe.grid(row=0, column=0, sticky="nesw")

    for i in range(15):
        ttk.Button(sframe.frame, text=i).grid(row=i, column=i)

    hscroll.configure(command=sframe.xview)
    vscroll.configure(command=sframe.yview)

    root.mainloop()
