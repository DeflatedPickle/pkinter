#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from html.parser import HTMLParser

# link

__title__ = "Template"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class HTMLText(tk.Text):
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
    def __init__(self, parent, *args):
        tk.Text.__init__(self, parent, *args)
        self.parent = parent

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    htext = HTMLText(root)
    htext.insert(1.0, """<html>
    <head>
        <title>Test</title>
    </head>

    <body>
        <h1>Parse me!</h1>
    </body>
</html>""")
    htext.pack(expand=True, padx=5, pady=5)
    root.mainloop()
