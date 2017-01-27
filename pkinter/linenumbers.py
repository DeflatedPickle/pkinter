import tkinter as tk
from tkinter import ttk

#link

__title__ = "LineNumbers"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"

class LineNumbers (tk.Listbox):
    """
            -----DESCRIPTION-----
    This widget, once linked to a text widget, shows the line numbers of that widget.

            -----USAGE-----
    text = tk.Text (parent)
    scrollbar = ttk.Scrollbar (parent)
    lineNumbers = pk.LineNumbers (parent, textwidget = text, scrollwidget = scrollbar)
    lineNumbers.pack (side = "left", fill = "y")
    scrollbar.pack (side = "right", fill = "y")
    text.pack (side = "right", fill = "both")

            -----CONTENTS-----
    ---VARIABLES---
    textwidget        = The linked text widget.
    scrollwidget      = The linked vertical scrollbar.

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    redraw ()         = Works out how many lines there are.
    __scrollboth ()   = Scrolls both the text and line numbers.
    __updatescroll () =
    """
    def __init__ (self, parent, textwidget = "", scrollwidget = "", width = 5, *args):
        tk.Listbox.__init__ (self, parent, activestyle = "none", highlightcolor = "SystemButtonFace", width = width, *args)
        self.textwidget = textwidget
        self.scrollwidget = scrollwidget

        self.textwidget.bind ("<<Change>>", self.redraw)
        self.textwidget.bind ("<Configure>", self.redraw)
        self.textwidget.bind ("<KeyRelease>", self.redraw)

        self.textwidget.configure (yscrollcommand = self.__updatescroll)
        self.configure (yscrollcommand = self.__updatescroll)
        self.scrollwidget.configure (command = self.__scrollboth)

    def redraw (self, *args):
        self.delete (0, "end")

        numbers = int (self.textwidget.index ("end-1c").split (".") [0])

        for i in range (numbers):
            self.insert ("end", str (i + 1))

    def __scrollboth (self, action, position, type = None):
        self.textwidget.yview_moveto (position)
        self.yview_moveto (position)

    def __updatescroll (self, first, last, type = None):
        self.textwidget.yview_moveto (first)
        self.yview_moveto (first)
        self.scrollwidget.set (first, last)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    vscroll = ttk.Scrollbar (root, orient = "vertical")
    vscroll.pack (side = "right", fill = "y", padx = [0, 5], pady = 5)
    text = tk.Text (root)
    text.pack (side = "right", fill = "both", expand = True, pady = 5)
    lnumbers = LineNumbers (root, textwidget = text, scrollwidget = vscroll)
    lnumbers.pack (side = "left", fill = "y", padx = [5, 0], pady = 5)
    root.mainloop ()
