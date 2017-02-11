import tkinter as tk
from tkinter import ttk

# link

__title__ = "PageView"
__version__ = "1.2.2"
__author__ = "DeflatedPickle"


class PageView (ttk.Frame):
    """
            -----DESCRIPTION-----
    A navigable frame that can hold however many pages you want.

            -----USAGE-----
    pageView = PageView(parent, back_text=[string], next_text=[string])
    pageView.pack()

    frame = ttk.Frame(pageView.frame)
    pageView.add(child=frame)

            -----PARAMETERS-----
    back_text        = The text on the back Button.
    next_text        = The text on the next Button.

            -----CONTENTS-----
    ---VARIABLES---
    total_pages      = The count of total pages.
    frame_list       = A list of all the added pages.
    index            = The current page.
    page             = The current page out of total pages.

    ---WIDGETS---
    self
    frame            = Holds the active page.
    navigation_frame = Hold the navigational widgets.
    back             = Allows the user to move backwards a page.
    label            = Shows the current frame out of the total frames.
    next             = Allows the user to move forward a page.

    ---FUNCTIONS---
    back()           = Moves to the page before the active one.
    next()           = Moves to the page after the active one.
    add()            = Adds a new page to the widget.
    work_out_pages() = Works out how many pages there are in total.
    """
    def __init__(self, parent, back_text="< Back", next_text="Next >", *args):
        ttk.Frame.__init__(self, parent, *args)

        self.total_pages = 0
        self.frame_list = []
        self.index = tk.IntVar()
        self.index.set(0)
        self.page = tk.IntVar()
        self.page.set("0 / 0")

        self.frame = ttk.Frame(self)
        self.frame.pack(side="top", fill="both", expand=True)

        self.navigation_frame = ttk.Frame(self)
        self.navigation_frame.pack(side="bottom", fill="x")
        self.navigation_frame.columnconfigure(1, weight=1)

        self.back = ttk.Button(self.navigation_frame, text=back_text, command=self.back)
        self.back.grid(row=0, column=0)

        self.label = ttk.Label(self.navigation_frame, textvariable=self.page)
        self.label.grid(row=0, column=1)

        self.next = ttk.Button(self.navigation_frame, text=next_text, command=self.next)
        self.next.grid(row=0, column=2)

    def back(self):
        if self.index.get() != 0:
            for i in range(len(self.frame_list)):
                self.frame_list[i].pack_forget()

            self.index.set(self.index.get() - 1)
            self.frame_list[self.index.get()].pack(fill="both", expand=True)

            self.work_out_pages()

    def next(self):
        if self.index.get() != len(self.frame_list) - 1:
            for i in range(len(self.frame_list)):
                self.frame_list[i].pack_forget()

            self.index.set(self.index.get() + 1)
            self.frame_list[self.index.get()].pack(fill="both", expand=True)

            self.work_out_pages()

    def add(self, child=None):
        """
        Adds a new page to the PageView.
        """
        self.frame_list.append(child)
        self.frame_list[self.index.get()].pack(fill="both", expand=True)
        self.total_pages = str(len(self.frame_list))

        self.work_out_pages()

    def work_out_pages(self):
        self.page.set(str(self.index.get() + 1) + "/" + str(self.total_pages))

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
