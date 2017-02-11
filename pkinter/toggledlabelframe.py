import tkinter as tk
from tkinter import ttk

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-LabelFrame.html

__title__ = "ToggledLabelFrame"
__version__ = "1.2.3"
__author__ = "DeflatedPickle"


class ToggledLabelFrame(ttk.LabelFrame):
    """
            -----DESCRIPTION-----
    This widget is used to store any other widgets inside of it.
    It can be toggled on or off, so widgets inside of it aren't always shown.

            -----USAGE-----
    toggledFrame = ToggledLabelFrame(parent, on_text=[string], off_text=[string], default_state=[boolean], state="enabled")
    toggledFrame.pack()
    button = Button(toggledFrame.frame).pack()

            -----PARAMETERS-----
    parent
    on_text       = The text displayed when the button is active.
    off_text      = The text displayed when the button is inactive.
    default_state = The state the widget starts on.
    state         = The state of the button.

            -----CONTENTS-----
    ---VARIABLES---
    on_text       = The text displayed when the button is active.
    off_text      = The text displayed when the button is inactive.
    variable      = The variable used for the button.

    ---WIDGETS---
    self
    fill          = A placeholder.
    button        = The button that toggles the frame.
    frame         = The frame which holds widgets.

    ---FUNCTIONS---
    activate()    = Checks value of variable and shows or hides the frame.
    toggle()      = Switches the label frame to the opposite state.
    """
    def __init__(self, parent, on_text="Active", off_text="Inactive", default_state=False, state="enabled", *args):
        ttk.LabelFrame.__init__(self, parent, labelanchor="n", *args)
        self.on_text = on_text
        self.off_text = off_text

        self.fill = tk.Frame(self, height=5)

        self.variable = tk.IntVar()
        self.variable.set(default_state)

        self.button = ttk.Checkbutton(self, width=11, state=state, variable=self.variable, command=self.activate, style="TButton")
        self.configure(labelwidget=self.button)

        self.frame = ttk.Frame(self)

        self.activate()

    def activate(self):
        if not self.variable.get():
            self.fill.pack()
            self.frame.forget()
            self.button.configure(text=self.on_text)

        if self.variable.get():
            self.fill.forget()
            self.frame.pack(fill="both", expand=True)
            self.button.configure(text=self.off_text)

    def toggle(self):
        """
        Switches the LabelFrame to the opposite state.
        """
        self.variable.set(not self.variable.get())
        self.activate()

##################################################

if __name__ == "__main__":
    root = tk.Tk()
    tframe = ToggledLabelFrame(root, on_text="Off", off_text="On", default_state=False, state="enabled")
    tframe.pack(expand=True, padx=5, pady=5)
    for i in range(3):
        ttk.Button(tframe.frame).pack()
    root.mainloop()
