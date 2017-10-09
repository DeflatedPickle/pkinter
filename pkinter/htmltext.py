#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import font
from html.parser import HTMLParser

# link
# https://docs.python.org/3/library/html.parser.html

__title__ = "Template"
__version__ = "1.6.0"
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
        self.configure(state="disabled")

        self.title = ""

        self.resize_list = []

        self._master = font.Font(font=self.cget("font"))
        self.configure(font=self._master)

        # TODO: Clean this up - make it shorter.
        self._h1 = font.Font(font=self.cget("font"))
        self._h1.configure(size=32)

        self._h2 = font.Font(font=self.cget("font"))
        self._h2.configure(size=24)

        self._h3 = font.Font(font=self.cget("font"))
        self._h3.configure(size=19)

        self._h4 = font.Font(font=self.cget("font"))
        self._h4.configure(size=16)

        self._h5 = font.Font(font=self.cget("font"))
        self._h5.configure(size=14)

        self._h6 = font.Font(font=self.cget("font"))
        self._h6.configure(size=13)
        ###########################

        self.tag_configure("tag", elide=True)
        self.tag_configure("comment", elide=True)

        self.tag_configure("h1", font=self._h1)
        self.tag_configure("h2", font=self._h2)
        self.tag_configure("h3", font=self._h3)
        self.tag_configure("h4", font=self._h4)
        self.tag_configure("h5", font=self._h5)
        self.tag_configure("h6", font=self._h6)

        self._parser = HTMLHandler(self)

        self._actual = ""

        self.bind("<Configure>", self.resize_widgets)

    def insert(self, index, chars, *args):
        self.configure(state="normal")
        lines = []
        for line in chars.splitlines():
            if line.lstrip() != "":
                lines.append(line.lstrip())
        finished = "\n".join(lines)

        self._actual = finished
        tk.Text.insert(self, index, finished, *args)
        self.configure(state="disabled")

    def get_actual(self):
        return self._actual

    def parse(self):
        self._parser.feed(self.get(1.0, "end"))

    def resize_widgets(self, event=None):
        for widget in self.resize_list:
            widget.configure(width=self.winfo_width())


class HTMLHandler(HTMLParser):
    def __init__(self, text: HTMLText):
        HTMLParser.__init__(self)
        self._text = text

        self._start = 0
        self._end = 0

    def handle_starttag(self, tag, attrs):
        print("Found Start:", "<{}>".format(tag))
        self._start = self._text.search("<{}>".format(tag), "end") + "+{}c".format(len(tag) + 2)
        # self._text.tag_add("tag", self._text.search("<{}>".format(tag), 1.0))
        # self.apply_tag(tag, "<{}>", "tag")

        if tag == "hr":
            frame = ttk.Frame(self._text.master)
            frame.pack_propagate(False)
            ttk.Separator(frame).pack(fill="x")
            self._text.resize_list.append(frame)
            self._text.window_create(self._start, window=frame)

    def handle_endtag(self, tag):
        print("Found End:", "</{}>".format(tag))
        self._end = self._text.search("</{}>".format(tag), "end")
        # self._text.tag_add("tag", self._text.search("</{}>".format(tag), 1.0))
        # self.apply_tag(tag, "</{}>", "tag")
        if tag == "title":
            self._text.title = self._text.get(self._start, self._end)

        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self._text.tag_add(tag, self._start, self._end)

    def handle_comment(self, data):
        print("Found Comment:", "<!--{}-->".format(data))
        # self.apply_tag(data, "<!--{}-->", "comment")

    ##########

    def apply_tag(self, type_, search, tag, data=False):
        if not data:
            start = self._text.search(search.format(type_), "end")
            end = self._text.search(search.format(type_), "end") + "+{}c".format(len(type_) + (2 if search == "<{}>" else 3 if search == "</{}>" else 7 if search == "<!--{}-->" else 0))

        else:
            start = self._start
            end = self._end

        self._text.tag_add(tag, start, end)


##################################################

if __name__ == "__main__":
    root = tk.Tk()
    htext = HTMLText(root)
    htext.insert(1.0, """<html>
    <head>
        <title>Test</title>
    </head>

    <!-- Ignore Me -->

    <body>
        <h1>Parse me!</h1>
        <h2>Another heading!</h2>
        <h3>Another heading!</h3>
        <h4>Another heading!</h4>
        <h5>Another heading!</h5>
        <h6>Another heading!</h6>
        
        <hr>
    </body>
</html>""")
    htext.parse()
    htext.pack(fill="x", expand=True, padx=5, pady=5)
    root.title(htext.title)
    root.mainloop()
