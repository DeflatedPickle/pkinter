import tkinter as tk
from tkinter import ttk

# https://developer.gnome.org/gtk3/stable/GtkInfoBar.html

__title__ = "InfoBar"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"


class InfoBar(ttk.Frame):
    """
            -----DESCRIPTION-----
    A bar to show a piece of information.
    Can be closed by the user.

            -----USAGE-----
    infoBar = InfoBar(parent, title=[string], title_command=[function], info=[string], info_command=[function], background=[string])
    infoBar.pack()

            -----PARAMETERS-----
    parent
    title         = The text used for the title Button.
    title_command = The command that will run when the title Button is pressed.
    info          = The text used for the info Button.
    info_command  = The command that will run when the info Button is pressed.
    background    = The background of the widget.

            -----CONTENTS-----
    ---VARIABLES---
    None

    ---WIDGETS---
    self
    title_button  = Shows the title text.
    info_button   = Shows the info text.
    close_button  = The button for closing the widget.

    ---FUNCTIONS---
    close()       = Removes the widget from it's parent.
    """
    def __init__(self, parent, title="", title_command=None, info="", info_command=None, background="SystemButtonFace", *args):
        ttk.Frame.__init__(self, parent, *args)

        self.columnconfigure(1, weight=1)

        style = ttk.Style()
        style.configure("InfoBar.Toolbutton", background=background)
        style.configure("InfoClose.InfoBar.Toolbutton", anchor="center")

        if title != "":
            self.title_button = ttk.Button(self, text=title, style="InfoBar.Toolbutton", command=title_command)
            self.title_button.grid(row=0, column=0)

        self.info_button = ttk.Button(self, text=info, style="InfoBar.Toolbutton", command=info_command)
        self.info_button.grid(row=0, column=1, sticky="we")

        self.close_button = ttk.Button(self, text="x", width=2, style="InfoClose.InfoBar.Toolbutton", command=self.close)
        self.close_button.grid(row=0, column=2)

    def close(self):
        """
        Closes the InfoBar.
        """
        self.forget()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    ibar = InfoBar(root, info="A Piece of Information", background="light blue")
    ibar.pack(fill="x")
    root.mainloop()
