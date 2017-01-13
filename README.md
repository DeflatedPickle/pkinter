## Widgets
<a href="#toggledlabelframe" class="button">ToggledLabelFrame</a>
<a href="#labeledseparator" class="button">LabeledSeparator</a>
<a href="#roundingscale" class="button">RoundingScale</a>
<a href="#entrytext" class="button">EntryText</a>
<a href="#limitedentry" class="button">LimitedEntry</a>
<a href="#colourpickerbutton" class="button">ColourPickerButton</a>
<a href="#editablelabel" class="button">EditableLabel</a>
<a href="#collapsiblepane" class="button">CollapsiblePane</a>
<a href="#hyperlink" class="button">Hyperlink</a>
<a href="#pageview" class="button">PageView</a>
<a href="#about" class="button">About</a>

<a name="toggledlabelframe"></a>

### ToggledLabelFrame

<a href="http://imgur.com/j0Spm27"><img src="http://i.imgur.com/j0Spm27.gif" title="source: imgur.com" /></a>

The toggled label frame can be used to clean up a GUI by hiding widgets inside of it.

**Code:**

```python
toggledFrame = ToggledLabelFrame (parent, ontext = "On", offtext = "Off", defaultstate = False)
toggledFrame.pack ()
```

<a name="labeledseparator"></a>

### LabeledSeparator

![Imgur](http://i.imgur.com/4oXN6WN.png?1)

The labeled separator can be used to separate parts of the GUI with text.
t
**Code:**

```python
labeledSeparator = LabeledSeparator (parent, text = "Separator", orient = "horizontal", textalign = "", padding = 5)
labeledSeparator.pack (fill = "x")
```

<a name="roundingscale"></a>

### RoundingScale

<a href="http://imgur.com/3R4WBYf"><img src="http://i.imgur.com/3R4WBYf.gif" title="source: imgur.com" /></a>

The rounding scale works just like a normal one, though it rounds its' value to a solid integer.

**Code:**

```python
roundingScale = RoundingScale (parent, from_ = 0, to = 10)
roundingScale.pack ()
```

<a name="entrytext"></a>

### EntryText

<a href="http://imgur.com/WIvFwfl"><img src="http://i.imgur.com/WIvFwfl.gif" title="source: imgur.com" /></a>

The entry text shows a string of text inside of it when the user hasn't input anything.

**Code:**

```python
entryText = EntryText (parent, text = "Password")
entryText.pack ()
```

<a name="limitedentry"></a>

### LimitedEntry

<a href="http://imgur.com/ARAI0VN"><img src="http://i.imgur.com/ARAI0VN.gif" title="source: imgur.com" /></a>

The limited entry works like a normal one, though the user can only input a certain amount of characters.

**Code:**

```python
limitedEntry = LimitedEntry (parent, maxchars = 10)
limitedEntry.pack ()
```

<a name="colourpickerbutton"></a>

### ColourPickerButton

<a href="http://imgur.com/ERKM54a"><img src="http://i.imgur.com/ERKM54a.gif" title="source: imgur.com" /></a>

```python
colourPickerButton = ColourPickerButton (parent, text = "Pick A Colour")
colourPickerButton.pack ()
```

<a name="editablelabel"></a>

### EditableLabel

<a href="http://imgur.com/HFR9UJ1"><img src="http://i.imgur.com/HFR9UJ1.gif" title="source: imgur.com" /></a>

```python
editableLabel = EditableLabel (parent, text = "Edit", doesresize = False)
editableLabel.pack ()
```

<a name="collapsiblepane"></a>

### CollapsiblePane

<a href="http://imgur.com/GK1erub"><img src="http://i.imgur.com/GK1erub.gif" title="source: imgur.com" /></a>

```python
collapsiblePane = CollapsiblePane (parent, expandedtext = "Expanded <<", collapsedtext = "Collapsed >>")
collapsiblePane.pack ()
```

<a name="hyperlink"></a>

### Hyperlink

<a href="http://imgur.com/85BnW98"><img src="http://i.imgur.com/85BnW98.gif" title="source: imgur.com" /></a>

```python
hyperlink = Hyperlink (parent, link = "https://github.com/DeflatedPickle/pkinter")
hyperlink.pack ()
```

<a name="pageview"></a>

### PageView

<a href="http://imgur.com/46UgxNK"><img src="http://i.imgur.com/46UgxNK.gif" title="source: imgur.com" /></a>

```python
pageView = PageView (parent, backtext = "< Back", nexttext = "Next >")
pageView.pack ()
```

<a name="about"></a>

### About
Pkinter is a set of custom widgets for Tkinter and TTK
