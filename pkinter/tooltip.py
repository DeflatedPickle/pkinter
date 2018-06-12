"""https://code.activestate.com/recipes/576688-tooltip-for-tkinter/
refactored by not7cd"""

import tkinter as tk


class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """

    def __init__(self, widget, msg=None, msg_function=None, delay=1, follow=True):
        """
        Initialize the ToolTip
        
        :param widget: The widget this ToolTip is assigned to
        :param msg:  A static string message assigned to the ToolTip
        :param msg_function: A function that retrieves a string to use as the ToolTip text
        :param delay:   The delay in seconds before the ToolTip appears(may be float)
        :param follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.widget = widget
        self.parent = self.widget.master
        super(ToolTip, self).__init__(self.parent, bg="black", padx=1, pady=1)

        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msg_var will contain the text displayed by the ToolTip
        self.msg_var = tk.StringVar()
        if msg is None:
            self.msg_var.set("No message provided")
        else:
            self.msg_var.set(msg)
        self.msg_function = msg_function
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.last_motion = 0
        # The test of the ToolTip is displayed in a Message widget ???
        tk.Message(self, textvariable=self.msg_var, bg="#FFFFDD", aspect=1000).grid()
        # Add bindings to the widget.  This will NOT override bindings that the widget already has
        self.widget.bind("<Enter>", self.spawn, "+")
        self.widget.bind("<Leave>", self.hide, "+")
        self.widget.bind("<Motion>", self.move, "+")

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.last_motion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        :param event: The event that called this function
        """
        self.last_motion = time()
        # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
        if not self.follow:
            self.withdraw()
            self.visible = 1
        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry("+%i+%i" % (event.x_root + 10, event.y_root + 10))
        try:
            # Try to call the message function.  Will not change the message if the message function is None or the message function fails
            self.msg_var.set(self.msg_function())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        :param event: The event that called this function
        """
        self.visible = 0
        self.withdraw()


if __name__ == "__main__":
    from time import time, localtime, strftime

    root = tk.Tk()

    def print_time():
        """
        Prints the current time in the following format:
        HH:MM:SS.00
        """
        t = time()
        timeString = "time="
        timeString += strftime("%H:%M:", localtime(t))
        timeString += "%.2f" % (t % 60,)
        return timeString

    for i in range(6):
        for j in range(4):
            text = "delay=%i\n" % i
            delay = i
            if j >= 2:
                follow = True
                text += "+follow\n"
            else:
                follow = False
                text += "-follow\n"
            if j % 2 == 0:
                msg = None
                msg_function = print_time
                text += "Message Function"
            else:
                msg = "Button at %s" % str((i, j))
                msg_function = None
                text += "Static Message"

            btn = tk.Button(root, text=text)
            btn.grid(row=i, column=j, sticky=tk.N + tk.S + tk.E + tk.W)

            ToolTip(btn, msg=msg, msg_function=msg_function, follow=follow, delay=delay)

    root.mainloop()
