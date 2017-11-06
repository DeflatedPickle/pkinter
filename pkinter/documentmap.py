#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "DocumentMap"
__version__ = "1.1.0"
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
    def __init__(self, parent, text_widget, scroll_widget=None, background="white", text_font=("courier", 7), text_pad=5, width=170, *args):
        tk.Canvas.__init__(self, parent, background=background, width=width, *args)
        self.parent = parent
        self._text_widget = text_widget
        self._scroll_widget = scroll_widget
        self._text_font = text_font
        self._text_pad = text_pad

        self._widget_text = None

        self._text_widget.bind("<<Change>>", self._redraw, "+")
        self._text_widget.bind("<Configure>", self._redraw, "+")
        self._text_widget.bind("<KeyRelease>", self._redraw, "+")

    def _redraw(self, event=None):
        self.delete(self._widget_text)

        self._widget_text = self.create_text([self._text_pad, self._text_pad], text=self._text_widget.get(1.0, "end"), font=self._text_font, anchor="nw")

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    text = tk.Text(root, width=1, height=1)
    text.pack(side="left", fill="both", expand=True, padx=[5, 0], pady=5)
    vscroll = ttk.Scrollbar(root, orient="vertical")
    vscroll.pack(side="left", fill="y", pady=5)
    temp = DocumentMap(root, text_widget=text, scroll_widget=vscroll)
    temp.pack(side="right", fill="y", padx=[0, 5], pady=5)
    root.mainloop()
