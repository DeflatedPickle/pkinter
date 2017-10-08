#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font
from html.parser import HTMLParser

# link

__title__ = "Template"
__version__ = "1.3.0"
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

        self._font = font.Font(font=self.cget("font"))

        self.tag_configure("tag", elide=True)
        self.tag_configure("comment", elide=True)

        self.tag_configure("h1", font=self.font_with_change(self._font, ("size", 15)))

        self._parser = HTMLHandler(self)

        self._actual = ""

    def insert(self, index, chars, *args):
        lines = []
        for line in chars.splitlines():
            if line.lstrip() != "":
                lines.append(line.lstrip())
        finished = "\n".join(lines)

        self._actual = finished
        tk.Text.insert(self, index, finished, *args)

    def get_actual(self):
        return self._actual

    def parse(self):
        self._parser.feed(self.get(1.0, "end"))

    @staticmethod
    def font_with_change(font_, change):
        font_[change[0]] = change[1]
        return font_


class HTMLHandler(HTMLParser):
    def __init__(self, text: tk.Text):
        HTMLParser.__init__(self)
        self._text = text

        self._start = 0
        self._end = 0

    def handle_starttag(self, tag, attrs):
        print("Found Start:", "<{}>".format(tag))
        self._start = self._text.search("<{}>".format(tag), "end") + "+{}c".format(len(tag) + 2)
        # self._text.tag_add("tag", self._text.search("<{}>".format(tag), 1.0))
        self.apply_tag(tag, "<{}>", "tag")

    def handle_endtag(self, tag):
        print("Found End:", "</{}>".format(tag))
        self._end = self._text.search("</{}>".format(tag), "end")
        # self._text.tag_add("tag", self._text.search("</{}>".format(tag), 1.0))
        self.apply_tag(tag, "</{}>", "tag")
        if tag == "h1":
            self.apply_tag("", "", "h1", data=True)

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
    </body>
</html>""")
    htext.parse()
    htext.pack(expand=True, padx=5, pady=5)
    root.mainloop()
