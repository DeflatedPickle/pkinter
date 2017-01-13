import tkinter as tk
from tkinter import ttk

#link

__title__ = "PageView"
__version__ = "1.1.0"
__author__ = "DeflatedPickle"

class PageView (ttk.Frame):
    """
            -----DESCRIPTION-----
    A navigable frame that can hold however many pages you want.

            -----USAGE-----
    pageView = PageView (parent, backtext = [string], nexttext = [string])
    pageView.pack ()

    frame = ttk.Frame (pageView.subframe)
    pageView.add (child = frame)

            -----CONTENTS-----
    ---VARIABLES---
    backtext        = The text on the back button.
    nexttext        = The text on the next button.
    totalpages      = The count of total pages.
    framelist       = A list of all the added pages.
    index           = The current page.
    page            = The current page out of total pages.

    ---WIDGETS---
    Self
    subframe        = Holds the active page.
    navigationframe = Hold the navigational widgets.
    back            = Allows the user to move backwards a page.
    label           = Shows the current frame out of the total frames.
    next            = Allows the user to move forward a page.

    ---FUNCTIONS---
    back ()         = Moves to the page before the active one.
    next ()         = Moves to the page after the active one.
    add ()          = Adds a new page to the widget.
    workoutpages () = Works out how many pages there are in total.
    """
    def __init__ (self, parent, backtext = "< Back", nexttext = "Next >", *args):
        ttk.Frame.__init__ (self, parent, *args)
        self.backtext = backtext
        self.nexttext = nexttext

        self.totalpages = 0
        self.framelist = []
        self.index = tk.IntVar ()
        self.index.set (0)
        self.page = tk.IntVar ()
        self.page.set ("0 / 0")

        self.subframe = ttk.Frame (self)
        self.subframe.pack (side = "top", fill = "both", expand = True)

        self.navigationframe = ttk.Frame (self)
        self.navigationframe.pack (side = "bottom", fill = "x")
        self.navigationframe.columnconfigure (1, weight = 1)

        self.back = ttk.Button (self.navigationframe, text = self.backtext, command = self.back)
        self.back.grid (row = 0, column = 0)

        self.label = ttk.Label (self.navigationframe, textvariable = self.page)
        self.label.grid (row = 0, column = 1)

        self.next = ttk.Button (self.navigationframe, text = self.nexttext, command = self.next)
        self.next.grid (row = 0, column = 2)

    def back (self):
        if self.index.get () != 0:
            for i in range (len (self.framelist)):
                self.framelist [i].pack_forget ()

            self.index.set (self.index.get () - 1)
            self.framelist [self.index.get ()].pack (fill = "both", expand = True)

            self.workoutpages ()

    def next (self):
        if self.index.get () != len (self.framelist) - 1:
            for i in range (len (self.framelist)):
                self.framelist [i].pack_forget ()

            self.index.set (self.index.get () + 1)
            self.framelist [self.index.get ()].pack (fill = "both", expand = True)

            self.workoutpages ()

    def add (self, child = None):
        """
        Adds a new page to the widget.
        """
        self.framelist.append (child)
        self.framelist [self.index.get ()].pack (fill = "both", expand = True)
        self.totalpages = str (len (self.framelist))

        self.workoutpages ()

    def workoutpages (self):
        self.page.set (str (self.index.get () + 1) + "/" + self.totalpages)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    pview = PageView (root)
    pview.pack (fill = "both", expand = True, padx = 5, pady = 5)

    frame1 = ttk.Frame (pview.subframe)
    for i in range (3):
        ttk.Button (frame1, text = i).pack (side = "left")
    frame2 = ttk.Frame (pview.subframe)
    ttk.Checkbutton (frame2, text = "Checkbutton").pack ()
    frame3 = ttk.Frame (pview.subframe)
    ttk.Label (frame3, text = "Frame 3").pack (side = "bottom")

    pview.add (child = frame1)
    pview.add (child = frame2)
    pview.add (child = frame3)
    root.mainloop ()
