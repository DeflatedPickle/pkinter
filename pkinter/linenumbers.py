#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "LineNumbers"
__version__ = "1.0.3"
__author__ = "DeflatedPickle"


class LineNumbers(tk.Listbox):
    """
            -----DESCRIPTION-----
    This widget, once linked to a text widget, shows the line numbers of that widget.

            -----USAGE-----
    text = tk.Text(parent)
    scrollbar = ttk.Scrollbar(parent)
    lineNumbers = pk.LineNumbers(parent, text_widget=text, scroll_widget=scrollbar)
    lineNumbers.pack(side="left", fill="y")
    scrollbar.pack(side="right", fill="y")
    text.pack(side="right", fill="both")

            -----PARAMETERS-----
    parent             = The parent of the widget.
    text_widget        = The linked Text widget.
    scroll_widget      = The linked vertical Scrollbar.
    width              = The width of the LineNumbers.

            -----CONTENTS-----
    ---VARIABLES---
    parent             = The parent of the widget.
    _text_widget       = The linked Text widget.
    _scroll_widget     = The linked vertical Scrollbar.
    _width             = The width of the LineNumbers.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    redraw()          = Works out how many lines there are.
    _scrollboth()    = Scrolls both the Text widget and LineNumbers.
    _updatescroll()  = Moves the text_widget and scroll_widget to the top.
    """
    def __init__(self, parent, text_widget=None, scroll_widget=None, width=5, *args):
        tk.Listbox.__init__(self, parent, activestyle="none", highlightcolor="SystemButtonFace", width=width, *args)
        self.parent = parent
        self._text_widget = text_widget
        self._scroll_widget = scroll_widget
        self._width = width

        self._text_widget.bind("<<Change>>", self._redraw, "+")
        self._text_widget.bind("<Configure>", self._redraw, "+")
        self._text_widget.bind("<KeyRelease>", self._redraw, "+")

        self._text_widget.configure(yscrollcommand=self._updatescroll)
        self.configure(yscrollcommand=self._updatescroll)
        self._scroll_widget.configure(command=self._scrollboth)

    def _redraw(self, event=None):
        """Redraws the lines for the widget."""
        self.delete(0, "end")

        numbers = int(self._text_widget.index("end-1c").split(".")[0])

        for i in range(numbers):
            self.insert("end", str(i + 1))

    def _scrollboth(self, action, position, type=None):
        self._text_widget.yview_moveto(position)
        self.yview_moveto(position)

    def _updatescroll(self, first, last, type=None):
        self._text_widget.yview_moveto(first)
        self.yview_moveto(first)
        self._scroll_widget.set(first, last)

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    vscroll = ttk.Scrollbar(root, orient="vertical")
    vscroll.pack(side="right", fill="y", padx=[0, 5], pady=5)
    text = tk.Text(root, width=1, height=1)
    text.pack(side="right", fill="both", expand=True, pady=5)
    lnumbers = LineNumbers(root, text_widget=text, scroll_widget=vscroll)
    lnumbers.pack(side="left", fill="y", padx=[5, 0], pady=5)
    root.mainloop()
