## Widgets

### ToggledLabelFrame

![Imgur](http://i.imgur.com/QtLlBZf.png)

The toggled label frame can be used to clean up a GUI by hiding widgets inside of it.

Code:

```python
toggledFrame = ToggledLabelFrame (parent, ontext = "On", offtext = "Off", defaultstate = False)
toggledFrame.pack ()
```

### LabeledSeparator

![Imgur](http://i.imgur.com/4oXN6WN.png?1)

The labeled separator can be used to separate parts of the GUI with text.

Code:

```python
labeledSeparator = LabeledSeparator (parent, text = "Separator", orient = "horizontal", textalign = "", padding = 5)
labeledSeparator.pack (fill = "x")
```

### About
Pkinter is a set of custom widgets for Tkinter and TTK
