#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "PageView"
__version__ = "1.2.3"
__author__ = "DeflatedPickle"


class PageView(ttk.Frame):
    """
            -----DESCRIPTION-----
    A navigable frame that can hold however many pages you want.

            -----USAGE-----
    pageView = PageView(parent, back_text=[string], next_text=[string])
    pageView.pack()

    frame = ttk.Frame(pageView.frame)
    pageView.add(child=frame)

            -----PARAMETERS-----
    parent            = The parent of the widget.
    back_text         = The text on the back Button.
    next_text         = The text on the next Button.

            -----CONTENTS-----
    ---VARIABLES---
    parent            = The parent of the widget.
    _back_text        = The text on the back Button.
    _next_text        = The text on the next Button.
    _total_pages      = The count of total pages.
    _frame_list       = A list of all the added pages.

    ---TKINTER VARIABLES---
    _index            = The current page.
    _page             = The current page out of total pages.

    ---WIDGETS---
    self
    frame             = Holds the active page.
    _navigation_frame = Hold the navigational widgets.
    _back             = Allows the user to move backwards a page.
    _label            = Shows the current frame out of the total frames.
    _next             = Allows the user to move forward a page.

    ---FUNCTIONS---
    _back()           = Moves to the page before the active one.
    _next()           = Moves to the page after the active one.
    add()             = Adds a new page to the widget.
    _work_out_pages() = Works out how many pages there are in total.
    """

    def __init__(self, parent, back_text="< Back", next_text="Next >", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._back_text = back_text
        self._next_text = next_text

        self._total_pages = 0
        self._frame_list = []

        self._index = tk.IntVar()
        self._index.set(0)

        self._page = tk.StringVar()
        self._page.set("0 / 0")

        self.frame = ttk.Frame(self)
        self.frame.pack(side="top", fill="both", expand=True)

        self._navigation_frame = ttk.Frame(self)
        self._navigation_frame.pack(side="bottom", fill="x")
        self._navigation_frame.columnconfigure(1, weight=1)

        self._back = ttk.Button(self._navigation_frame, text=back_text, command=self._back)
        self._back.grid(row=0, column=0)

        self._label = ttk.Label(self._navigation_frame, textvariable=self._page)
        self._label.grid(row=0, column=1)

        self._next = ttk.Button(self._navigation_frame, text=next_text, command=self._next)
        self._next.grid(row=0, column=2)

    def _back(self):
        """Moves the PageView backwards a page."""
        if self._index.get() != 0:
            for i in range(len(self._frame_list)):
                self._frame_list[i].pack_forget()

            self._index.set(self._index.get() - 1)
            self._frame_list[self._index.get()].pack(fill="both", expand=True)

            self._work_out_pages()

    def _next(self):
        """Moves the PageView forwards a page."""
        if self._index.get() != len(self._frame_list) - 1:
            for i in range(len(self._frame_list)):
                self._frame_list[i].pack_forget()

            self._index.set(self._index.get() + 1)
            self._frame_list[self._index.get()].pack(fill="both", expand=True)

            self._work_out_pages()

    def add(self, child=None):
        """Adds a new page to the PageView."""
        self._frame_list.append(child)
        self._frame_list[self._index.get()].pack(fill="both", expand=True)
        self._total_pages = str(len(self._frame_list))

        self._work_out_pages()

    def _work_out_pages(self):
        self._page.set(str(self._index.get() + 1) + "/" + str(self._total_pages))


##################################################

if __name__ == "__main__":
    root = tk.Tk()
    pview = PageView(root)
    pview.pack(expand=True, padx=5, pady=5)

    frame1 = ttk.Frame(pview.frame)
    for i in range(3):
        ttk.Button(frame1, text=i).pack(side="left")
    frame2 = ttk.Frame(pview.frame)
    ttk.Checkbutton(frame2, text="Checkbutton").pack()
    frame3 = ttk.Frame(pview.frame)
    ttk.Label(frame3, text="Frame 3").pack(side="bottom")

    pview.add(child=frame1)
    pview.add(child=frame2)
    pview.add(child=frame3)
    root.mainloop()
