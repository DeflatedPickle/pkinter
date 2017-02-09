## Pkinter
A set of useful widgets for use with TkInter.

[![PyPI](https://img.shields.io/pypi/v/pkinter.svg)](https://pypi.python.org/pypi/pkinter)
[![PyPI](https://img.shields.io/pypi/pyversions/pkinter.svg)](https://pypi.python.org/pypi/pkinter)

[![PyPI](https://img.shields.io/pypi/dd/pkinter.svg)](https://pypi.python.org/pypi/pkinter)
[![PyPI](https://img.shields.io/pypi/dw/pkinter.svg)](https://pypi.python.org/pypi/pkinter)
[![PyPI](https://img.shields.io/pypi/dm/pkinter.svg)](https://pypi.python.org/pypi/pkinter)

## Installing The Library

First off, you will need to have Python 3 installed and have Python in your system PATH. Then, you will need to open your systems' command prompt and type: `pip install pkinter`, this will install this library to your system.

## Using The Library

To use the library in your code, simply import like so: `import pkinter as pk`.
You will also need to import Tkinter, you can import that like this: `import tkinter as tk`, and if you want native TkInter widgets, also do `from tkinter import ttk`.

## Widgets

### pk.ToggledLabelFrame

<a href="http://imgur.com/j0Spm27"><img src="http://i.imgur.com/j0Spm27.gif" title="ToggledLabelFrame" /></a>

The pk.ToggledLabelFrame can be used to clean up a GUI by hiding widgets inside of it.

**Code:**

```python
toggledFrame = pk.ToggledLabelFrame(parent, ontext="On", offtext="Off", defaultstate=False)
toggledFrame.pack()
```

---

### pk.LabeledSeparator

<a href="http://imgur.com/4oXN6WN"><img src="http://i.imgur.com/4oXN6WN.png?1" title="LabeledSeparator" /></a>

The pk.LabeledSeparator can be used to separate parts of the GUI with text.

**Code:**

```python
labeledSeparator = pk.LabeledSeparator(parent, text="Separator", orient="horizontal", textalign="", padding=5)
labeledSeparator.pack(fill="x")
```

---

### pk.RoundingScale

<a href="http://imgur.com/3R4WBYf"><img src="http://i.imgur.com/3R4WBYf.gif" title="RoundingScale" /></a>

The pk.RoundingScale works just like a normal one, though it rounds its' value to a solid integer.

**Code:**

```python
roundingScale = pk.RoundingScale(parent, from_=0, to=10)
roundingScale.pack()
```

---

### pk.EntryText

<a href="http://imgur.com/WIvFwfl"><img src="http://i.imgur.com/WIvFwfl.gif" title="EntryText" /></a>

The pk.EntryText shows a string of text inside of it when the user hasn't input anything.

**Code:**

```python
entryText = pk.EntryText(parent, text="Password")
entryText.pack()
```

---

### pk.LimitedEntry

<a href="http://imgur.com/ARAI0VN"><img src="http://i.imgur.com/ARAI0VN.gif" title="LimitedEntry" /></a>

The pk.LimitedEntry works like a normal one, though the user can only input a certain amount of characters.

**Code:**

```python
limitedEntry = pk.LimitedEntry(parent, maxchars=10)
limitedEntry.pack()
```

---

### pk.ColourPickerButton

<a href="http://imgur.com/ERKM54a"><img src="http://i.imgur.com/ERKM54a.gif" title="ColourPickerButton" /></a>

The pk.ColourPickerButton allows the user to pick a colour with ease.

```python
colourPickerButton = pk.ColourPickerButton(parent, text="Pick A Colour")
colourPickerButton.pack()
```

---

### pk.EditableLabel

<a href="http://imgur.com/HFR9UJ1"><img src="http://i.imgur.com/HFR9UJ1.gif" title="EditableLabel" /></a>

The pk.EditableLabel allows the user to edit a label and give different text.

```python
editableLabel = pk.EditableLabel(parent, text="Edit", doesresize=False)
editableLabel.pack()
```

---

### pk.CollapsiblePane

<a href="http://imgur.com/GK1erub"><img src="http://i.imgur.com/GK1erub.gif" title="CollapsiblePane" /></a>

The pk.CollapsiblePane frame can be used to clean up a GUI by hiding widgets inside of it.

```python
collapsiblePane = pk.CollapsiblePane(parent, expandedtext="Expanded <<", collapsedtext="Collapsed >>")
collapsiblePane.pack()
```

---

### pk.Hyperlink

<a href="http://imgur.com/85BnW98"><img src="http://i.imgur.com/85BnW98.gif" title="Hyperlink" /></a>

The pk.Hyperlink allows you to place a link to a website that'll take the user to that site upon a click.

```python
hyperlink = pk.Hyperlink(parent, link="https://github.com/DeflatedPickle/pkinter")
hyperlink.pack()
```

---

### pk.PageView

<a href="http://imgur.com/46UgxNK"><img src="http://i.imgur.com/46UgxNK.gif" title="PageView" /></a>

The pk.PageView allows you to add as many pages to a frame, the user can then browse through every page.

```python
pageView = pk.PageView(parent, backtext="< Back", nexttext="Next >")
pageView.pack()
```

---

### pk.Toolbar

The pk.Toolbar adds buttons to activate commands easier than menus.

```python
toolbar = pk.Toolbar(parent)
toolbar.pack()
```

---

### pk.Statusbar

The pk.Statusbar adds labels to show variables easier.

```python
statusbar = pk.Statusbar(parent)
statusbar.pack()
```

---

### pk.LineNumbers

<a href="http://imgur.com/SFkDaFF"><img src="http://i.imgur.com/SFkDaFF.gif" title="LineNumbers" /></a>

The pk.LineNumbers widget is used to show the lines of a Text widget.

```python
text = tk.Text(parent)
scrollbar = ttk.Scrollbar(parent)
linenumbers = pk.LineNumbers(parent, textwidget=text, scrollwidget=scrollbar)
linenumbers.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")
text.pack(side="right", fill="both")
```

---

### pk.BoundButton

<a href="http://imgur.com/tbCqti7"><img src="http://i.imgur.com/tbCqti7.gif" title="BoundButton" /></a>

The pk.BoundButton can be bound to a key.

```python
def function():
    print("Button Pressed")

boundButton = pk.BoundButton(parent, text="Press Return", key="Return", command=function)
boundButton.pack()
```

---

### pk.ValidEntry

<a href="http://imgur.com/kn3qg8x"><img src="http://i.imgur.com/kn3qg8x.gif" title="ValidEntry" /></a>

The pk.ValidEntry can be given a list of strings and shows green text if the text in the Entry is in the list.

```python
validEntry = pk.ValidEntry(parent, valid_list=["foo", "bar", "baz"])
validEntry.pack()
```

---

### pk.ChoiceBook

<a href="http://imgur.com/93B2O8d"><img src="http://i.imgur.com/93B2O8d.gif" title="ChoiceBook" /></a>

The pk.ChoiceBook allows navigation through given frames with a Combobox.

```python
choiceBook = pk.ChoiceBook(parent, combobox_position="top")
choiceBook.pack()
```

---

### pk.PasswordEntry

<a href="http://imgur.com/kdY7QfR"><img src="http://i.imgur.com/kdY7QfR.gif" title="PasswordEntry" /></a>

The pk.PasswordEntry changes any text input into it into a given character.

```python
passwordEntry = pk.PasswordEntry(parent, cover_character="*")
passwordEntry.pack()
```

---

### pk.InvalidEntry

<a href="http://imgur.com/AsP2M49"><img src="http://i.imgur.com/AsP2M49.gif" title="InvalidEntry" /></a>

The pk.InvalidEntry can be given a list of strings and shows red text if the text in the Entry is in the list.

```python
invalidEntry = pk.InvalidEntry(parent, invalid_list=["foo", "bar", "baz"])
invalidEntry.pack()
```

---

### pk.ListBook

<a href="http://imgur.com/ijjKaBJ"><img src="http://i.imgur.com/ijjKaBJ.gif" title="ListBook" /></a>

The pk.ListBook allows navigation through given frames with a Listbox.

```python
listBook = pk.ListBook(parent)
listBook.pack()
```
