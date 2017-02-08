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
You will also need to import Tkinter, you can import that like this: `import tkinter as tk`.

## Widgets

### ToggledLabelFrame

<a href="http://imgur.com/j0Spm27"><img src="http://i.imgur.com/j0Spm27.gif" title="ToggledLabelFrame" /></a>

The toggled label frame can be used to clean up a GUI by hiding widgets inside of it.

**Code:**

```python
toggledFrame = pk.ToggledLabelFrame(parent, ontext="On", offtext="Off", defaultstate=False)
toggledFrame.pack()
```

---

### LabeledSeparator

<a href="http://imgur.com/4oXN6WN"><img src="http://i.imgur.com/4oXN6WN.png?1" title="LabeledSeparator" /></a>

The labeled separator can be used to separate parts of the GUI with text.

**Code:**

```python
labeledSeparator = pk.LabeledSeparator(parent, text="Separator", orient="horizontal", textalign="", padding=5)
labeledSeparator.pack(fill="x")
```

---

### RoundingScale

<a href="http://imgur.com/3R4WBYf"><img src="http://i.imgur.com/3R4WBYf.gif" title="RoundingScale" /></a>

The rounding scale works just like a normal one, though it rounds its' value to a solid integer.

**Code:**

```python
roundingScale = pk.RoundingScale(parent, from_=0, to=10)
roundingScale.pack()
```

---

### EntryText

<a href="http://imgur.com/WIvFwfl"><img src="http://i.imgur.com/WIvFwfl.gif" title="EntryText" /></a>

The entry text shows a string of text inside of it when the user hasn't input anything.

**Code:**

```python
entryText = pk.EntryText(parent, text="Password")
entryText.pack()
```

---

### LimitedEntry

<a href="http://imgur.com/ARAI0VN"><img src="http://i.imgur.com/ARAI0VN.gif" title="LimitedEntry" /></a>

The limited entry works like a normal one, though the user can only input a certain amount of characters.

**Code:**

```python
limitedEntry = pk.LimitedEntry(parent, maxchars=10)
limitedEntry.pack()
```

---

### ColourPickerButton

<a href="http://imgur.com/ERKM54a"><img src="http://i.imgur.com/ERKM54a.gif" title="ColourPickerButton" /></a>

The colour picker button allows the user to pick a colour with ease.

```python
colourPickerButton = pk.ColourPickerButton(parent, text="Pick A Colour")
colourPickerButton.pack()
```

---

### EditableLabel

<a href="http://imgur.com/HFR9UJ1"><img src="http://i.imgur.com/HFR9UJ1.gif" title="EditableLabel" /></a>

The editable label allows the user to edit a label and give different text.

```python
editableLabel = pk.EditableLabel(parent, text="Edit", doesresize=False)
editableLabel.pack()
```

---

### CollapsiblePane

<a href="http://imgur.com/GK1erub"><img src="http://i.imgur.com/GK1erub.gif" title="CollapsiblePane" /></a>

The collapsible pane frame can be used to clean up a GUI by hiding widgets inside of it.

```python
collapsiblePane = pk.CollapsiblePane(parent, expandedtext="Expanded <<", collapsedtext="Collapsed >>")
collapsiblePane.pack()
```

---

### Hyperlink

<a href="http://imgur.com/85BnW98"><img src="http://i.imgur.com/85BnW98.gif" title="Hyperlink" /></a>

The hyperlink allows you to place a link to a website that'll take the user to that site upon a click.

```python
hyperlink = pk.Hyperlink(parent, link="https://github.com/DeflatedPickle/pkinter")
hyperlink.pack()
```

---

### PageView

<a href="http://imgur.com/46UgxNK"><img src="http://i.imgur.com/46UgxNK.gif" title="PageView" /></a>

The page view allows you to add as many pages to a frame, the user can then browse through every page.

```python
pageView = pk.PageView(parent, backtext="< Back", nexttext="Next >")
pageView.pack()
```

---

### Toolbar

The toolbar adds buttons to activate commands easier than menus.

```python
toolbar = pk.Toolbar(parent)
toolbar.pack()
```

---

### Statusbar

The statusbar adds labels to show variables easier.

```python
statusbar = pk.Statusbar(parent)
statusbar.pack()
```

---

### LineNumbers

The LineNumbers widget is used to show the lines of a Text widget.

```python
text = tk.Text(parent)
scrollbar = ttk.Scrollbar(parent)
linenumbers = pk.LineNumbers(parent, textwidget=text, scrollwidget=scrollbar)
linenumbers.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")
text.pack(side="right", fill="both")
```

---

### BoundButton

The BoundButton can be bound to a key.

```python
def function():
    print("Button Pressed")

boundButton = BoundButton(parent, text="Press Return", key="Return", command=function)
boundButton.pack()
```

---

### ValidEntry

The ValidEntry can be given a list of strings and shows green text if the text in the Entry is in the list.

```python
validEntry = ValidEntry(parent, valid_list=["foo", "bar", "baz"])
validEntry.pack()
```

---

### About
Pkinter is a set of custom widgets for Tkinter and TTK
