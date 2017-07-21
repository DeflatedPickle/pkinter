#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import font
from tkinter import ttk
from idlelib.ToolTip import ToolTipBase

# https://en.wikipedia.org/wiki/Ribbon_(computing)
# https://msdn.microsoft.com/en-us/library/windows/desktop/dn742393(v=vs.85).aspx

__title__ = "Ribbon"
__version__ = "1.8.1"
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

        ttk.Style().layout("Ribbon.TMenubutton",
                           [('Menubutton.dropdown', {'sticky': 'ns', 'side': 'right'}), ('Menubutton.button', {'sticky': 'nswe', 'expand': '1', 'children': [('Menubutton.padding', {'sticky': 'we', 'expand': '1', 'children': [('Menubutton.label', {'sticky': 'w'})]})]})])

        ttk.Style().layout("RibbonImportant.TMenubutton",
                           [('Menubutton.dropdown', {'sticky': 'ew', 'side': 'bottom'}), ('Menubutton.button', {'sticky': 'nswe', 'expand': '1', 'children': [('Menubutton.padding', {'sticky': 'we', 'expand': '1', 'children': [('Menubutton.label', {'sticky': ''})]})]})])

        self._notebook = ttk.Notebook(self)
        self._notebook.pack(fill="both", expand=True)

    def add_tab(self, text: str="", type_: str="", context_tab: str=""):  # type_ should either be "core" or "context", if "context", a context tab should be provided (not implemented).
        frame = ttk.Frame(self._notebook)
        self._notebook.add(frame, text=text)

        return frame

    def add_group(self, parent: tk.Widget, text: str="", rows: int=1, has_button: bool=False, side: str="left"):
        group = Group(parent, text=text, rows=rows, has_button=has_button, empty_labels=self._empty_labels)
        group.pack(side=side, fill="both", expand=True, padx=1, pady=1)

        return group


class Group(ttk.Frame):
    def __init__(self, parent, text: str="", rows: int=1, has_button: bool=False, empty_labels: bool=False, *args, **kwargs):
        ttk.Frame.__init__(self, parent, style="TLabelframe", *args, **kwargs)
        self.parent = parent
        self._rows = rows
        self._has_button = has_button
        self._empty_labels = empty_labels

        self._widgets = []
        self._dictionary_rows = {}

        # TODO: Add dynamic placing of widgets instead of specified rows.

        for frame in range(self._rows):
            current_frame = tk.Frame(self)
            current_frame.pack(side="top", fill="both", expand=True, padx=5, pady=1)

            self._dictionary_rows[frame] = current_frame

        ttk.Style().configure("Group.TLabel", background="light gray")

        self._frame_bottom = ttk.Frame(self)
        self._frame_bottom.pack(side="bottom", fill="x", padx=1, pady=1)
        self._frame_bottom.columnconfigure(0, weight=1)

        self._label = ttk.Label(self._frame_bottom, text=text, anchor="center", style="Group.TLabel")
        # self._label.grid(row=0, column=0, sticky="ew")

        if self._has_button:
            self._button = LabelButton(self._frame_bottom, text="\u2198", width=2)
            # self._button.grid(row=0, column=1)

        if not self._empty_labels:
            self._check_widgets()

    def _check_widgets(self):
        if len(self._widgets) > 1:
            self._label.grid(row=0, column=0, sticky="ew")

            if self._has_button:
                self._button.grid(row=0, column=1)

        elif len(self._widgets) == 1:
            self._label.grid_remove()

            if self._has_button:
                self._button.grid_remove()

    def add_button(self, text="", row: int=0, tooltip_title="", tooltip: bool=True, tooltip_description="", tooltip_image: tk.Image=None, tooltip_bind="", image="", important=False):
        self._add_widget(text, row, tooltip, tooltip_title, tooltip_description, tooltip_image, tooltip_bind, image, "button", important=important)

    def add_menubutton(self, text="", row: int=0, tooltip: bool=True, tooltip_title="", tooltip_description="", tooltip_image: tk.Image=None, tooltip_bind="", image="", important=False):
        self._add_widget(text, row, tooltip, tooltip_title, tooltip_description, tooltip_image, tooltip_bind, image, "menubutton", important=important)

    def add_combobox(self, row: int=0, tooltip: bool=False, type_=""):
        self._add_widget(row=row, tooltip=tooltip, type_="combobox" + ("::" + type_ if type_ else ""), important=True)

    def add_buttonbar(self, row: int=0, side="left"):
        widget = ButtonBar(self._dictionary_rows[row])
        widget.pack(side=side, fill="x", padx=1)

        self._widgets.append(widget)

        if not self._empty_labels:
            self._check_widgets()

        return widget

    def add_gallery(self, row: int=0):
        widget = Gallery(self._dictionary_rows[row])
        widget.pack(side="left", fill="both", expand=True)

        self._widgets.append(widget)

        return widget

    def _add_widget(self, text="", row: int=0, tooltip: bool=True, tooltip_title="", tooltip_description="", tooltip_image: tk.Image=None, tooltip_bind="", image="", type_: str="", combobox_type="", important=False):  # important will make the button bigger than others (not implemented).
        widget = None

        if type_ == "button":
            widget = ttk.Button(self._dictionary_rows[row], text=text, image=image, style="Toolbutton")

        elif type_ == "menubutton":
            widget = ttk.Menubutton(self._dictionary_rows[row], text=text, image=image)

            if important:
                widget.configure(style="RibbonImportant.TMenubutton")

            elif not important:
                widget.configure(style="Ribbon.TMenubutton")

        elif "combobox" in type_:
            widget = ttk.Combobox(self._dictionary_rows[row])

            if "font" in type_:
                widget.configure(values=font.families())

            elif "size" in type_:
                widget.configure(width=3, values=[number for number in range(1, 50)])

        if important:
            widget.pack(side="left", fill="y" if "combobox" not in type_ else "x", expand=True)

        else:
            widget.pack(side="top", fill="x", expand=True)

        if tooltip:
            EnhancedToolTip(widget, tooltip_title, tooltip_description, tooltip_image, tooltip_bind)

        self._widgets.append(widget)

        if not self._empty_labels:
            self._check_widgets()

        return widget


class Gallery(ttk.Frame):
    def __init__(self, parent, item_width: int=15, wrap_after: int=3, wrap_width: int=295, *args, **kwargs):
        ttk.Frame.__init__(self, parent, style="TLabelframe", *args, **kwargs)
        self.parent = parent
        self._item_width = item_width
        self._wrap_after = wrap_after
        self._wrap_width = wrap_width

        self._current_row = 0
        self._current_column = 0
        self._current_width = 0

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._frame = ttk.Frame(self, width=self._wrap_width)
        self._frame.grid(row=0, rowspan=3, column=0, sticky="nesw", padx=1, pady=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.grid_propagate(False)
        self._frame.update_idletasks()

        self._button_up = ttk.Button(self, width=1, text="\u2191")
        self._button_up.grid(row=0, column=1)

        self._button_down = ttk.Button(self, width=1, text="\u2193")
        self._button_down.grid(row=1, column=1)

        self._button_show = ttk.Button(self, width=1, text="\u21A1")
        self._button_show.grid(row=2, column=1)

    def _check_width(self):
        self._frame.update_idletasks()

        if self._current_width + 98 > self._frame.winfo_width():
            self._current_column = 0
            self._current_row += 1
            self._current_width = 0

    def add_item(self, text: str="", image: str=""):
        widget = ttk.Radiobutton(self._frame, text=text, image=image, width=self._item_width, style="Toolbutton")
        widget.grid(row=self._current_row, column=self._current_column, sticky="nesw")
        widget.update_idletasks()

        self._current_column += 1
        self._current_width += widget.winfo_width()
        self._check_width()

        return widget


class EnhancedToolTip(ToolTipBase):
    def __init__(self, parent, title="", description="", image: tk.Image=None, bind=""):
        ToolTipBase.__init__(self, parent)
        self.parent = parent
        self._title = title
        self._description = description
        self._image = image
        self._bind = bind

        image_new = tk.PhotoImage(self._image)
        self._image_scale = image_new.zoom(16, 16)

        colour = "white"

        bold = font.nametofont("TkTooltipFont")
        bold.configure(weight="bold")

        ttk.Style().configure("ToolTip.TFrame", background=colour)
        ttk.Style().configure("Main.ToolTip.TFrame", borderwidth=1, relief="solid")
        ttk.Style().configure("ToolTip.TLabel", background=colour)
        ttk.Style().configure("Bold.ToolTip.TLabel", font=bold)

    def showtip(self):
        ToolTipBase.showtip(self)
        self.tipwindow.update()

        self.tipwindow.geometry("{}x{}".format(self.tipwindow.winfo_width() + 50, self.tipwindow.winfo_height()))

    def showcontents(self):
        frame_main = ttk.Frame(self.tipwindow, style="Main.ToolTip.TFrame")
        frame_main.pack(fill="both", expand=True)

        frame_top = ttk.Frame(frame_main, style="ToolTip.TFrame")
        frame_top.pack(fill="both", expand=True, padx=1, pady=[1, 0])

        title = ttk.Label(frame_top, text=self._title, style="Bold.ToolTip.TLabel")
        title.pack(fill="x")

        frame_description = ttk.Frame(frame_top, width=10, style="ToolTip.TFrame")
        frame_description.pack(fill="both", expand=True)

        ttk.Label(frame_description, width=1, style="ToolTip.TLabel").pack(side="left", fill="y")

        description = ttk.Label(frame_description, text=self._description, style="ToolTip.TLabel")
        description.pack(side="left", fill="both")

        ttk.Separator(frame_main, orient="horizontal").pack(fill="x", padx=1)

        frame_bottom = ttk.Frame(frame_main, style="ToolTip.TFrame")
        frame_bottom.pack(fill="x", padx=1, pady=[0, 1])

        image = ttk.Label(frame_bottom, image=self._image_scale, style="ToolTip.TLabel")
        image.pack(side="left")

        bind = ttk.Label(frame_bottom, text=self._bind, style="ToolTip.TLabel")
        bind.pack(side="right", fill="x", expand=True)


class DialogBox(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent


class LabelButton(ttk.Label):
    def __init__(self, parent, command=None, *args, **kwargs):
        ttk.Label.__init__(self, parent, anchor="center", style="LabelButtonEnter.TLabel", *args, **kwargs)
        self.parent = parent
        self._command = command

        ttk.Style().configure("LabelButtonEnter.TLabel", background="light gray")
        ttk.Style().configure("LabelButtonButtonPress.TLabel", background="gray")

        self.bind("<ButtonPress-1>", self._button_press)
        self.bind("<ButtonRelease-1>", self._button_release)

    def _button_press(self, event=None):
        self.configure(style="LabelButtonButtonPress.TLabel")

        if self._command is not None:
            self._command()

    def _button_release(self, event=None):
        self.configure(style="LabelButtonEnter.TLabel")


class ButtonBar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, style="TLabelframe", *args, **kwargs)
        self.parent = parent

        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True, padx=1, pady=1)

    def add_button(self, text="", image=""):
        self._add_widget(text, image, type_="button")

    def add_checkbutton(self, text="", image="", variable: tk.Variable=None):
        self._add_widget(text, image, variable=variable, type_="checkbutton")

    def add_radiobutton(self, text="", image="", variable: tk.Variable=None, value: int=0):
        self._add_widget(text, image, variable=variable, value=value, type_="radiobutton")

    def add_menubutton(self, text="", image=""):
        self._add_widget(text, image, type_="menubutton")

    def _add_widget(self, text="", image="", variable: tk.Variable=None, value: int=0, type_=""):
        widget = None

        if type_ == "button":
            widget = ttk.Button(self.frame, text=text, image=image, style="Toolbutton")

        elif type_ == "checkbutton":
            widget = ttk.Checkbutton(self.frame, text=text, image=image, variable=variable, style="Toolbutton")

        elif type_ == "radiobutton":
            widget = ttk.Radiobutton(self.frame, text=text, image=image, variable=variable, value=value, style="Toolbutton")

        elif type_ == "menubutton":
            widget = ttk.Menubutton(self.frame, text=text, image=image, style="Ribbon.TMenubutton")

        widget.pack(side="left", fill="y", expand=True)

##################################################

if __name__ == "__main__":
    root = tk.Tk()

    r = Ribbon(root)
    r.pack(fill="x", expand=True, padx=5, pady=5)

    home = r.add_tab(text="Home")

    clipboard = r.add_group(home, text="Clipboard", has_button=True)
    clipboard.add_menubutton(text="Paste", important=True)
    clipboard.add_button(text="Cut")
    clipboard.add_button(text="Copy")
    clipboard.add_button(text="Format Painter")

    tab_font = r.add_group(home, text="Font", rows=3, has_button=True)
    tab_font.add_combobox(type_="font")
    tab_font.add_combobox(type_="size")

    fontbar = tab_font.add_buttonbar(row=1)
    fontbar.add_checkbutton(text="B")
    fontbar.add_checkbutton(text="I")
    fontbar.add_menubutton(text="U")
    fontbar.add_checkbutton(text="O")
    variable_string = tk.BooleanVar()
    fontbar.add_radiobutton(text="S", variable=variable_string, value=0)
    fontbar.add_radiobutton(text="S", variable=variable_string, value=1)

    tab_font.add_buttonbar(row=1).add_button(text="Clear")

    colourbar = tab_font.add_buttonbar(row=2)
    colourbar.add_menubutton(text="A")
    colourbar.add_menubutton(text="A")
    colourbar.add_menubutton(text="Aa")

    sizebar = tab_font.add_buttonbar(row=2)
    sizebar.add_menubutton(text="A")
    sizebar.add_menubutton(text="a")

    paragraph = r.add_group(home, text="Paragraph", has_button=True, rows=3)

    listbar = paragraph.add_buttonbar()
    listbar.add_menubutton(text="-")
    listbar.add_menubutton(text="1")
    listbar.add_menubutton(text="-/1")

    dentbar = paragraph.add_buttonbar()
    dentbar.add_button(text="I")
    dentbar.add_button(text="D")

    justifybar = paragraph.add_buttonbar(row=1)
    variable_justify = tk.IntVar()
    justifybar.add_radiobutton(text="=  ", variable=variable_justify, value=0)
    justifybar.add_radiobutton(text=" = ", variable=variable_justify, value=1)
    justifybar.add_radiobutton(text="  =", variable=variable_justify, value=2)
    justifybar.add_radiobutton(text=" = ", variable=variable_justify, value=3)

    paragraph.add_buttonbar(row=1).add_menubutton(text="|=")

    borderbar = paragraph.add_buttonbar(row=2)
    borderbar.add_menubutton(text="Colour")
    borderbar.add_menubutton(text="Style")

    paragraph.add_buttonbar(row=2).add_menubutton(text="AZ|")
    paragraph.add_buttonbar(row=2).add_menubutton(text="\u00B6")

    styles = r.add_group(home, text="Styles", has_button=True)

    stylegallery = styles.add_gallery()
    stylegallery.add_item(text="Style 1")
    stylegallery.add_item(text="Style 2")
    stylegallery.add_item(text="Style 3")
    stylegallery.add_item(text="Style 4")

    styles.add_menubutton(text="Change Styles", important=True)

    editing = r.add_group(home, text="Editing")
    editing.add_button(text="Find", tooltip_title="Find", tooltip_description="Find a string of text.", tooltip_bind="Ctrl+F")
    editing.add_menubutton(text="Replace")
    editing.add_menubutton(text="Select")

    options = r.add_group(home, text="Options")
    options.add_menubutton(text="Options", tooltip=False, important=True)

    insert = r.add_tab(text="Insert")

    view = r.add_tab(text="View")

    root.mainloop()
