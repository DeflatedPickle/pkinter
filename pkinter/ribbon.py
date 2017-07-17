#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "Ribbon"
__version__ = "1.3.0"
__author__ = "DeflatedPickle"


class Ribbon(ttk.Frame):
    """
            -----DESCRIPTION-----
    A template for new widgets.

            -----USAGE-----
    ribbon = Ribbon(parent)
    ribbon.pack()

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
    def __init__(self, parent, empty_labels=False, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self._empty_labels = empty_labels

        self._notebook = ttk.Notebook(self)
        self._notebook.pack(fill="both", expand=True)

    def add_tab(self, text: str=""):
        frame = ttk.Frame(self._notebook)
        self._notebook.add(frame, text=text)

        return frame

    def add_group(self, parent: tk.Widget, text: str="", has_button: bool=False, side: str="left"):
        group = _Group(parent, text=text, has_button=has_button, empty_labels=self._empty_labels)
        group.pack(side=side, fill="both", expand=True, padx=1, pady=1)

        return group


class _Group(ttk.Frame):
    def __init__(self, parent, text: str="", has_button: bool=False, empty_labels: bool=False, *args, **kwargs):
        ttk.Frame.__init__(self, parent, style="TLabelframe", *args, **kwargs)
        self.parent = parent
        self._has_button = has_button

        self._widgets = []

        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill="both", expand=True, padx=1, pady=1)

        ttk.Style().configure("Group.TLabel", background="light gray")

        self._frame_bottom = ttk.Frame(self)
        self._frame_bottom.pack(side="bottom", fill="x", padx=1, pady=1)
        self._frame_bottom.columnconfigure(0, weight=1)

        self._label = ttk.Label(self._frame_bottom, text=text, anchor="center", style="Group.TLabel")
        self._label.grid(row=0, column=0, sticky="ew")

        if self._has_button:
            self._button = _LabelButton(self._frame_bottom, text="\u2198", width=2)
            self._button.grid(row=0, column=1)

    def _check_widgets(self):
        if not self._widgets:
            self._label.grid_remove()

    def add_button(self, important=False, *args):
        button = ttk.Button(self.frame, args)
        button.pack(side="left")

        return button


class _LabelButton(ttk.Label):
    def __init__(self, parent, command=None, *args, **kwargs):
        ttk.Label.__init__(self, parent, anchor="center", style="LabelButtonEnter.TLabel", *args, **kwargs)
        self.parent = parent
        self._command = command

        ttk.Style().configure("LabelButtonEnter.TLabel", background="light gray")
        ttk.Style().configure("LabelButtonButtonPress.TLabel", background="gray")

        self.bind("<ButtonPress-1>", self._button_press)
        self.bind("<ButtonRelease-1>", self._button_release)

    def _button_press(self, event):
        self.configure(style="LabelButtonButtonPress.TLabel")

        if self._command is not None:
            self._command()

    def _button_release(self, event):
        self.configure(style="LabelButtonEnter.TLabel")

##################################################

if __name__ == "__main__":
    root = tk.Tk()

    r = Ribbon(root)
    r.pack(fill="x", expand=True, padx=5, pady=5)

    home = r.add_tab(text="Home")

    clipboard = r.add_group(home, text="Clipboard", has_button=True)
    clipboard.frame.rowconfigure(0, weight=1)
    clipboard.frame.columnconfigure(1, weight=1)

    paste = ttk.Menubutton(clipboard.frame, text="Paste", direction="below")
    paste.grid(row=0, rowspan=3, column=0, sticky="nesw")

    cut = ttk.Button(clipboard.frame, text="Cut", style="Toolbutton")
    cut.grid(row=0, column=1, sticky="ew")

    copy = ttk.Button(clipboard.frame, text="Copy", style="Toolbutton")
    copy.grid(row=1, column=1, sticky="ew")

    format_paint = ttk.Button(clipboard.frame, text="Format Painter", style="Toolbutton")
    format_paint.grid(row=2, column=1, sticky="ew")

    font = r.add_group(home, text="Font", has_button=True)

    drawing = r.add_group(home, text="Drawing", has_button=True)

    editing = r.add_group(home, text="Editing")
    editing.frame.columnconfigure(0, weight=1)

    find = ttk.Button(editing.frame, text="Find", style="Toolbutton")
    find.grid(row=0, column=0, sticky="ew")

    replace = ttk.Menubutton(editing.frame, text="Replace")
    replace.grid(row=1, column=0, sticky="ew")

    select = ttk.Menubutton(editing.frame, text="Select")
    select.grid(row=2, column=0, sticky="ew")

    insert = r.add_tab(text="Insert")

    view = r.add_tab(text="View")

    root.mainloop()
