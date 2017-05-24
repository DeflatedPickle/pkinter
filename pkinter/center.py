#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

__title__ = "Center"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


def center_on_screen(window: tk.Tk or tk.Toplevel):
    """Centers a window on the screen."""
    window.update_idletasks()

    width = window.winfo_width()
    height = window.winfo_height()

    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (width // 2)

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def center_on_parent(window: tk.Toplevel):
    """Centers a Toplevel on it's parent."""
    window.update_idletasks()
    parent = window.master

    width = window.winfo_width()
    height = window.winfo_height()

    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
