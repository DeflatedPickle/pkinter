#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

import random

__title__ = "GridCanvas"
__version__ = "1.2.0"
__author__ = "DeflatedPickle"


class GridCanvas(tk.Canvas):
    def __init__(self, parent, cell_width=10, cell_height=10, rows=10, columns=10, *args, **kwargs):
        tk.Canvas.__init__(self, parent, borderwidth=0, highlightthickness=0, *args, **kwargs)
        self.parent = parent

        self._cell_width = cell_width
        self._cell_height = cell_height
        self._rows = rows
        self._columns = columns

        self._hidden = False

        self.cells = {}
        self.cells_contents = {}

        self.draw_grid()

    def draw_grid(self):
        self.delete_grid()

        for r in range(self._rows):
            for c in range(self._columns):
                top = r * self._cell_height
                left = c * self._cell_width
                bottom = top + self._cell_height
                right = left + self._cell_width

                rect = self.create_rectangle(left, top, right, bottom, outline="gray", fill="", tags="grid")
                self.cells[r, c] = self.coords(rect)
                self.cells_contents[self.coords(rect)[0], self.coords(rect)[1]] = None

    def delete_grid(self):
        for i in self.find_withtag("grid"):
            self.delete(i)

    def clear_grid(self):
        for i in self.find("all"):
            if "grid" not in self.itemcget(i, "tags"):
                self.delete(i)

        for k in self.cells_contents.keys():
            self.cells_contents[k] = None

    def toggle_grid(self):
        self.itemconfigure("grid", width=self._hidden)
        self._hidden = not self._hidden

    def place_cell_location(self, thing, loc_x, loc_y, middle=True, replace=True):
        cells = self.find_closest(loc_x, loc_y)

        def place(loc_x, loc_y):
            if middle:
                self.move(thing, x + (self._cell_width // 2), y + (self._cell_height // 2))

            else:
                self.move(thing, x, y)

            if replace:
                self.delete(self.cells_contents[x, y])

            self.cells_contents[x, y] = thing

        for c in cells:
            x = self.coords(c)[0]
            y = self.coords(c)[1]

            if "grid" in self.gettags(c):
                place(x, y)

                return x, y

            if "current" in self.gettags(c):
                self.delete(c)
                close = self.find_closest(loc_x, loc_y)

                x = 0
                y = 0

                for i in close:
                    if "grid" in self.gettags(i):
                        x = self.coords(i)[0]
                        y = self.coords(i)[1]

                place(x, y)

                return x, y

            else:
                self.delete(thing)

    def remove_cell_location(self, loc_x, loc_y):
        cells = self.find_closest(loc_x, loc_y)

        for c in cells:
            x = self.coords(c)[0]
            y = self.coords(c)[1]

            if "grid" in self.gettags(c):
                self.delete(self.cells_contents[x, y])
                self.cells_contents[x, y] = None

    def closest_cell(self, loc_x, loc_y):
        cells = self.find_overlapping(loc_x - 5, loc_y - 5, loc_x + 5, loc_y + 5)

        for c in cells:
            x = self.coords(c)[0]
            y = self.coords(c)[1]

            if "grid" in self.gettags(c):
                return self.cells_contents[x, y]


if __name__ == "__main__":
    root = tk.Tk()

    canvas = GridCanvas(root)
    canvas.pack()

    tk.Button(root, text="Draw", command=canvas.draw_grid).pack()
    tk.Button(root, text="Delete", command=canvas.delete_grid).pack()
    tk.Button(root, text="Clear", command=canvas.clear_grid).pack()
    tk.Button(root, text="Toggle", command=canvas.toggle_grid).pack()

    bind_lamb = lambda event: canvas.place_cell_location(canvas.create_text(0, 0, text="0", font=f"Courier {random.randint(10, 20)}", fill=random.choice(["red", "green", "blue", "yellow", "orange", "purple"])), event.x, event.y)

    canvas.bind("<Button-1>", bind_lamb)
    canvas.bind("<B1-Motion>", bind_lamb)

    root.mainloop()
