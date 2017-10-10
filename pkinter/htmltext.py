#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk
from tkinter import font
from html.parser import HTMLParser

# link
# https://docs.python.org/3/library/html.parser.html
# https://www.w3schools.com/html

__title__ = "Template"
__version__ = "1.11.1"
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

        self._heading_list = [("h" + str(number + 1)) for number in range(0, 6)]
        self._paragraph_list = ["p", "pre"]
        self._formatting_list = ["b", "strong", "i", "em", "mark", "small", "del", "ins", "sub", "sup"]
        self._quote_cite_list = ["abbr", "address", "bdo", "blockquote", "cite", "q"]

        self.tag_list = self._heading_list + self._paragraph_list + self._formatting_list + self._quote_cite_list

        self.title = ""

        self.resize_list = []

        self._sans_serif = font.Font(family="Arial", size=10)
        self._serif = font.Font(family="Times New Roman", size=10)
        self._mono = font.Font(family="Courier", size=10)
        
        self.configure(font=self._sans_serif)

        ###########################
        self._tag = font.Font(family=self._mono.actual()["family"], size=10)

        self._h1 = font.Font(family=self._sans_serif.actual()["family"], size=32, weight="bold")
        self._h2 = font.Font(family=self._sans_serif.actual()["family"], size=24, weight="bold")
        self._h3 = font.Font(family=self._sans_serif.actual()["family"], size=19, weight="bold")
        self._h4 = font.Font(family=self._sans_serif.actual()["family"], size=16, weight="bold")
        self._h5 = font.Font(family=self._sans_serif.actual()["family"], size=14, weight="bold")
        self._h6 = font.Font(family=self._sans_serif.actual()["family"], size=13, weight="bold")

        self._p = font.Font(family=self._sans_serif.actual()["family"], size=10)
        self._pre = font.Font(family=self._sans_serif.actual()["family"], size=10)

        self._b = font.Font(family=self._sans_serif.actual()["family"], size=10, weight="bold")
        self._strong = font.Font(family=self._serif.actual()["family"], size=10, weight="bold")
        self._i = font.Font(family=self._sans_serif.actual()["family"], size=10, slant="italic")
        self._em = font.Font(family=self._serif.actual()["family"], size=10, slant="italic")
        self._mark = font.Font(family=self._sans_serif.actual()["family"], size=10)
        self._small = font.Font(family=self._sans_serif.actual()["family"], size=8)
        self._del = font.Font(family=self._sans_serif.actual()["family"], size=10, overstrike=True)
        self._ins = font.Font(family=self._sans_serif.actual()["family"], size=10, underline=True)
        self._sub = font.Font(family=self._sans_serif.actual()["family"], size=8)
        self._sup = font.Font(family=self._sans_serif.actual()["family"], size=8)

        self._abbr = font.Font(family=self._sans_serif.actual()["family"], size=10, underline=True)
        self._q = font.Font(family=self._sans_serif.actual()["family"], size=10)
        ###########################

        self.tag_configure("h1", font=self._h1)
        self.tag_configure("h2", font=self._h2)
        self.tag_configure("h3", font=self._h3)
        self.tag_configure("h4", font=self._h4)
        self.tag_configure("h5", font=self._h5)
        self.tag_configure("h6", font=self._h6)

        self.tag_configure("p", font=self._p)
        self.tag_configure("pre", font=self._pre)

        self.tag_configure("b", font=self._b)
        self.tag_configure("strong", font=self._strong)
        self.tag_configure("i", font=self._i)
        self.tag_configure("em", font=self._em)
        self.tag_configure("mark", font=self._mark, background="yellow")
        self.tag_configure("small", font=self._small)
        self.tag_configure("del", font=self._del)
        self.tag_configure("ins", font=self._ins)
        self.tag_configure("sub", font=self._sub, offset=-4)
        self.tag_configure("sup", font=self._sup, offset=4)

        self.tag_configure("abbr", font=self._abbr)
        self.tag_configure("q", font=self._q)

        self.tag_configure("tag", font=self._tag, elide=False)
        self.tag_configure("comment", font=self._tag, elide=False)

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

    def permissive_insert(self, index, chars, *args):
        self.configure(state="normal")
        tk.Text.insert(self, index, chars, *args)
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
        attributes = " ".join(["{}=\"{}\"".format(key, value) for key, value in attrs])
        tag_with_attributes = tag + (" " if attrs else "") + attributes
        print("Found Start:", "<{}{}>".format(tag, (" " if attrs else "") + attributes))

        if tag != "br":
            self._start = self._text.search("<{}>".format(tag_with_attributes), "end") + "+{}c".format((len(tag) + 2) + len(attributes) + (1 if attrs else 0))
        # self._text.tag_add("tag", self._text.search("<{}>".format(tag), 1.0))

        if tag == "hr":
            frame = ttk.Frame(self._text.master)
            frame.pack_propagate(False)
            ttk.Separator(frame).pack(fill="x")
            self._text.resize_list.append(frame)
            self._text.window_create(self._start, window=frame)

        elif tag == "br":
            index = self._text.search("<br>", self._start) + "+4c"
            self._text.permissive_insert(index, "\n")
            self._start = index

        elif tag == "q":
            self._text.permissive_insert(self._text.search("<q>", self._start) + "+3c", "\"")

        self.apply_tag(tag_with_attributes, "<{}>", "tag")

    def handle_endtag(self, tag):
        print("Found End:", "</{}>".format(tag))
        self._end = self._text.search("</{}>".format(tag), "end")
        # self._text.tag_add("tag", self._text.search("</{}>".format(tag), 1.0))

        if tag == "title":
            self._text.title = self._text.get(self._start, self._end)

        elif tag == "q":
            self._text.permissive_insert(self._text.search("</q>", self._start), "\"")

        if tag in self._text.tag_list:
            self._text.tag_add(tag, self._start, self._end)

        self.apply_tag(tag, "</{}>", "tag")

    def handle_comment(self, data):
        print("Found Comment:", "<!--{}-->".format(data))
        self.apply_tag(data, "<!--{}-->", "comment")

    ##########

    def apply_tag(self, type_, search, tag):
        start = self._text.search(search.format(type_), "end")
        # end = self._text.search(search.format(type_), "end") + "+{}c".format(len(type_) + (2 if search == "<{}>" else 3 if search == "</{}>" else 7 if search == "<!--{}-->" else 0))
        end = self._text.search(">", start) + "+1c"

        self._text.tag_add(tag, start, end)
        print("Added Tag: {}".format(type_))


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
        <h1>A heading!</h1>
        <h2>Another heading!</h2>
        <h3>And another one!</h3>
        <h4>And another one!</h4>
        <h5>And another one!</h5>
        <h6>And another one!</h6>
        
        <hr>
        
        <p>I am some<br>text.</p>
        
        <pre>I'm a bit of code</pre>
        
        <b>I'm bold.</b>
        <strong>I'm strong.</strong>
        <i>I'm italic.</i>
        <em>I'm emphasized.</em>
        <mark>I'm marked.</mark>
        <small>I'm small.</small>
        <del>I'm deleted.</del>
        <ins>I'm inserted.</ins>
        I'm <sub>subscript.</sub>
        I'm <sup>superscript.</sup>
        
        I'm an <abbr title="Abbreviation">abbr</abbr>
        <address>
        I'm<br>
        an<br>
        Address.
        </address>
        I'm a <q>quote</q>.
    </body>
</html>""")
    htext.parse()
    htext.pack(fill="both", side="left", expand=True, padx=[5, 0], pady=5)

    scroll = ttk.Scrollbar(root, command=htext.yview)
    scroll.pack(fill="y", side="right", padx=[0, 5], pady=5)
    htext.configure(yscrollcommand=scroll.set)

    root.title(htext.title)
    root.mainloop()
