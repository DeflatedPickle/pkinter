import tkinter as tk
from tkinter import ttk
import pkinter as pk

root = tk.Tk()

menu = tk.Menu(root, type="menubar")
filemenu = tk.Menu(menu)
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
menu.add_cascade(label="File", menu=filemenu)
helpmenu = tk.Menu(menu)
helpmenu.add_checkbutton(label="About")
helpmenu.add_separator()
helpmenu.add_checkbutton(label="Changelog")
menu.add_cascade(label="Help", menu=helpmenu)
root.configure(menu=menu)

##################################################

toolbar = pk.Toolbar(root)
toolbar.pack(side="top", fill="x")
button = toolbar.add_button(text="Button")
toolbar.add_separator()
checkbutton1 = toolbar.add_checkbutton(text="CheckButton 1")
checkbutton2 = toolbar.add_checkbutton(text="CheckButton 2")
toolbar.add_separator()
radiobutton1 = toolbar.add_radiobutton(text="RadioButton 1", value=0)
radiobutton2 = toolbar.add_radiobutton(text="RadioButton 2", value=1)
radiobutton3 = toolbar.add_radiobutton(text="RadioButton 3", value=2)
toolbar.add_separator()

##################################################

statusbar = pk.Statusbar(root)
statusbar.pack(side="bottom", fill="x")
variable = tk.StringVar()
statusbar.bind_widget(button, variable, "A Button", "")
statusbar.bind_widget(checkbutton1, variable, "A Checkbutton", "")
statusbar.bind_widget(checkbutton2, variable, "Another Checkbutton", "")
statusbar.bind_widget(radiobutton1, variable, "A Radiobutton", "")
statusbar.bind_widget(radiobutton2, variable, "Another Radiobutton", "")
statusbar.bind_widget(radiobutton3, variable, "A Third Radiobutton", "")

statusbar.bind_menu(menu, variable, ["Open the File menu.", "Open the Help menu."])
statusbar.bind_menu(filemenu, variable, ["Tear-off the menu.", "Create a new file.", "Save the current file."])
statusbar.bind_menu(helpmenu, variable, ["Tear-off the menu.", "Open the About window.", "", "Open the Changelog."])
statusbar.add_variable(variable=variable)

##################################################

frame = ttk.Frame(root)
frame.pack(fill="both")

##################################################

tlf = pk.ToggledLabelFrame(frame)
tlf.grid(row=0, column=0)

##################################################

for i in range(5):
    ttk.Button(tlf.frame).pack()

ls = pk.LabeledSeparator(frame, text="LabeledSeparator")
ls.grid(row=0, column=1)

##################################################

rs = pk.RoundingScale(frame, from_=0, to=5)
rs.grid(row=0, column=2)

##################################################

et = pk.EntryText(frame, text="EntryText")
et.grid(row=1, column=0)

##################################################

le = pk.LimitedEntry(frame)
le.grid(row=1, column=1)

##################################################

cpb = pk.ColourPickerButton(frame)
cpb.grid(row=1, column=2)

##################################################

el = pk.EditableLabel(frame, text="EditableLabel")
el.grid(row=2, column=0)

##################################################

cp = pk.CollapsiblePane(frame)
cp.grid(row=2, column=1)

for i in range(5):
    ttk.Button(cp.frame).pack()

##################################################

hl = pk.Hyperlink(frame, text="Hyperlink")
hl.grid(row=2, column=2)

##################################################

pv = pk.PageView(frame)
pv.grid(row=3, column=0)

frame1 = ttk.Frame(pv.frame)
for i in range(3):
    ttk.Button(frame1, text=i).pack(side="left")
frame2 = ttk.Frame(pv.frame)
ttk.Checkbutton(frame2, text="Checkbutton").pack()
frame3 = ttk.Frame(pv.frame)
ttk.Label(frame3, text="Frame 3").pack(side="bottom")

pv.add(child=frame1)
pv.add(child=frame2)
pv.add(child=frame3)

##################################################


def func():
    print("Function")

bb = pk.BoundButton(frame, text="BoundButton", key="b", command=func)
bb.grid(row=3, column=1)

##################################################

ve = pk.ValidEntry(frame, valid_list=["validentry", "validEntry", "Validentry", "ValidEntry"])
ve.grid(row=3, column=2)

##################################################

cb = pk.ChoiceBook(frame)
cb.grid(row=4, column=0)

frame1 = ttk.Frame(cb.frame)
for i in range(3):
    ttk.Button(frame1, text=i).pack(side="left")
frame2 = ttk.Frame(cb.frame)
ttk.Checkbutton(frame2, text="Checkbutton").pack()
frame3 = ttk.Frame(cb.frame)
ttk.Label(frame3, text="Frame 3").pack(side="bottom")

cb.add(child=frame1, label="Frame1")
cb.add(child=frame2, label="Frame2")
cb.add(child=frame3, label="Frame3")

##################################################

pe = pk.PasswordEntry(frame, cover_character="*")
pe.grid(row=4, column=1)

##################################################

iv = pk.InvalidEntry(frame, invalid_list=["invalidentry", "invalidEntry", "Invalidentry", "InvalidEntry"])
iv.grid(row=4, column=2)

##################################################

lb = pk.ListBook(frame)
lb.grid(row=5, column=0)

frame1 = ttk.Frame(lb.frame)
for i in range(3):
    ttk.Button(frame1, text=i).pack(side="left")
frame2 = ttk.Frame(lb.frame)
ttk.Checkbutton(frame2, text="Checkbutton").pack()
frame3 = ttk.Frame(lb.frame)
ttk.Label(frame3, text="Frame 3").pack(side="bottom")

lb.add(child=frame1, label="Frame1")
lb.add(child=frame2, label="Frame2")
lb.add(child=frame3, label="Frame3")

##################################################

al = pk.AccelLabel(frame, label_text="AccelLabel", accelerator_text="Ctrl+A")
al.grid(row=5, column=1)

##################################################

ib = pk.InfoBar(frame, title="InfoBar", info="Shows information.")
ib.grid(row=5, column=2)

##################################################

lb = pk.LockButton(frame)
lb.grid(row=6, column=0)

##################################################

tb = pk.ToggleButton(frame)
tb.grid(row=6, column=1)

##################################################

ss = pk.ScaleSwitch(frame)
ss.grid(row=6, column=2)

##################################################

bs = pk.ButtonSwitch(frame)
bs.grid(row=7, column=0)

##################################################

fp = pk.FilePicker(frame)
fp.grid(row=7, column=1)

##################################################

dp = pk.DirectoryPicker(frame)
dp.grid(row=7, column=2)

##################################################

pk.center_on_screen(root)

##################################################

tp = tk.Toplevel(root)
pk.center_on_parent(tp)

##################################################

root.mainloop()
