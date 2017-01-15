import tkinter as tk
import pkinter as pk

root = tk.Tk ()

tlf = pk.ToggledLabelFrame (root).grid (row = 0, column = 0)
ls = pk.LabeledSeparator (root).grid (row = 0, column = 1)
rs = pk.RoundingScale (root).grid (row = 0, column = 2)
et = pk.EntryText (root).grid (row = 1, column = 0)
le = pk.LimitedEntry (root).grid (row = 1, column = 1)
cpb = pk.ColourPickerButton (root).grid (row = 1, column = 2)
el = pk.EditableLabel (root).grid (row = 2, column = 0)
cp = pk.CollapsiblePane (root).grid (row = 2, column = 1)
hl = pk.Hyperlink (root).grid (row = 2, column = 2)
pv = pk.PageView (root).grid (row = 3, column = 0)

root.mainloop ()
