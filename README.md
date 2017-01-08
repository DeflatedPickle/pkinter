## Widgets

### ToggledLabelFrame

![Image](http://i.imgur.com/QtLlBZf.png)

The toggled label frame can be used to clean up a GUI by hiding widgets inside of it.

Code:

```markdown
toggledFrame = ToggledLabelFrame (parent, ontext = "On", offtext = "Off", defaultstate = False)
toggledFrame.pack ()
```

### LabeledSeparator

![Image](http://i.imgur.com/4oXN6WN.png)

The labeled separator can be used to separate parts of the GUI with text.

Code:

```markdown
labeledSeparator = LabeledSeparator (parent, text = "Separator", orient = "horizontal", textalign = "", padding = 5)
labeledSeparator.pack (fill = "x")
```

### About
Pkinter is a set of custom widgets for Tkinter and TTK
