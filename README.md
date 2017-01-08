## Widgets

### ToggledLabelFrame

![Imgur](http://i.imgur.com/QtLlBZf.png)

The toggled label frame can be used to clean up a GUI by hiding widgets inside of it.

**Code:**

```python
toggledFrame = ToggledLabelFrame (parent, ontext = "On", offtext = "Off", defaultstate = False)
toggledFrame.pack ()
```

### LabeledSeparator

![Imgur](http://i.imgur.com/4oXN6WN.png?1)

The labeled separator can be used to separate parts of the GUI with text.

**Code:**

```python
labeledSeparator = LabeledSeparator (parent, text = "Separator", orient = "horizontal", textalign = "", padding = 5)
labeledSeparator.pack (fill = "x")
```

### RoundingScale

The rounding scale works just like a normal one, though it rounds its' value to a solid integer.

**Code:**

```python
roundingScale = RoundingScale (parent, from_ = 0, to = 10)
roundingScale.pack ()
```

### EntryText

![Imgur](http://i.imgur.com/RkUcNZb.png)

The entry text shows a string of text inside of it when the user hasn't input anything.

**Code:**

```python
entryText = EntryText (parent, text = "Password")
entryText.pack ()
```

### LimitedEntry

The limited entry works like a normal one, though the user can only input a certain amount of characters.

**Code:**

```python
limitedEntry = LimitedEntry (parent, maxchars = 10)
limitedEntry.pack ()
```

### About
Pkinter is a set of custom widgets for Tkinter and TTK
