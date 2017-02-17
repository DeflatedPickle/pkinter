import tkinter as tk
from tkinter import ttk
import pkinter as pk

root = tk.Tk()

tlf = pk.ToggledLabelFrame(root)
tlf.grid(row=0, column=0)

##################################################

for i in range(5):
    ttk.Button(tlf.frame).pack()

ls = pk.LabeledSeparator(root, text="LabeledSeparator")
ls.grid(row=0, column=1)

##################################################

rs = pk.RoundingScale(root, from_=0, to=5)
rs.grid(row=0, column=2)

##################################################

et = pk.EntryText(root, text="EntryText")
et.grid(row=1, column=0)

##################################################

le = pk.LimitedEntry(root)
le.grid(row=1, column=1)

##################################################

cpb = pk.ColourPickerButton(root)
cpb.grid(row=1, column=2)

##################################################

el = pk.EditableLabel(root, text="EditableLabel")
el.grid(row=2, column=0)

##################################################

cp = pk.CollapsiblePane(root)
cp.grid(row=2, column=1)

for i in range(5):
    ttk.Button(cp.frame).pack()

##################################################

hl = pk.Hyperlink(root, text="Hyperlink")
hl.grid(row=2, column=2)

##################################################

pv = pk.PageView(root)
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

def function():
    print("Function")

bb = pk.BoundButton(root, text="BoundButton", key="b", command=function)
bb.grid(row=3, column=1)

##################################################

ve = pk.ValidEntry(root, valid_list=["validentry", "validEntry", "Validentry", "ValidEntry"])
ve.grid(row=3, column=2)

##################################################

cb = pk.ChoiceBook(root)
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

pe = pk.PasswordEntry(root, cover_character="*")
pe.grid(row=4, column=1)

##################################################

iv = pk.InvalidEntry(root, invalid_list=["invalidentry", "invalidEntry", "Invalidentry", "InvalidEntry"])
iv.grid(row=4, column=2)

##################################################

lb = pk.ListBook(root)
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

al = pk.AccelLabel(root, label_text="AccelLabel", accelerator_text="Ctrl+A")
al.grid(row=5, column=1)

##################################################

ib = pk.InfoBar(root, title="InfoBar", info="Shows information.")
ib.grid(row=5, column=2)

##################################################

lb = pk.LockButton(root)
lb.grid(row=6, column=0)

##################################################

tb = pk.ToggleButton(root)
tb.grid(row=6, column=1)

##################################################

ss = pk.ScaleSwitch(root)
ss.grid(row=6, column=2)

##################################################

bs = pk.ButtonSwitch(root)
bs.grid(row=7, column=0)

##################################################

fp = pk.FilePicker(root)
fp.grid(row=7, column=1)

##################################################

dp = pk.DirectoryPicker(root)
dp.grid(row=7, column=2)

##################################################

root.mainloop()
