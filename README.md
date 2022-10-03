# VS Code Tricks

(To render this .md file in VS Code editor, CTRL+SHIFT+V. Then CTRL+\ to split editor--drag preview window to newly split screen.)

## Save time and clicks by automating how you check updates to your rendered web code

Install 'Live Server' in VS Code Marketplace for hot reload
```
With HTML file open, click 'Go Live' in blue actions bar (bottom right corner of window).
```
Save / Auto Save#

By default, VS Code requires an explicit action to save your changes to disk, Ctrl+S.

However, it's easy to turn on Auto Save, which will save your changes after a configured delay or when focus leaves the editor. With this option turned on, there is no need to explicitly save the file. The easiest way to turn on Auto Save is with the File > Auto Save toggle that turns on and off save after a delay.

For more control over Auto Save, open User or Workspace settings and find the associated settings:
(CTLR+SHIFT+P > Preferences: Open User Settings)

If error: "Unable to write into user settings. Please open the user settings to correct errors/warnings in it and try again"
```
Open the suggested user settings.json file and make sure the format is:
{
    this.setting: someSetting,
    different.settings: otherSetting
}

Or delete all text and save (VS Code will just use default settings, which you cannot edit)

Or click the 'Workspace' tab to change this for this workspace only (and each other workspace you open, until you fix your VS Code)
```

Change files.autoSave: onWindowChange - to save files when the focus moves out of the VS Code window.

## HTML Automation

CTRL+N to create new (blank) file. 

At top of file type `HTML` and choose 'HTML:5' from the options. This will fill out a proper HTML document template.

When creating new elements (especially with classes), type the first half of the element and complete the '>'--the closing part of the element will autocomplete. If not, change this in user settings.json: 

```
// Configures if the built-in HTML language suggests HTML5 tags, properties and values.
"html.suggest.html5": true
```

Also helpful is auto updating of tags when you decide to change an element, such as `<div>` to `<h1>`:
```
"editor.linkedEditing": true
```
Most helpful--autocomplete for tags with classes.

To make a `<div>` with class name 'title', type `div.title` and press TAB. 


## Use Sass (.scss) instead of CSS

Install Sass extension in VS Code Marketplace for autocomplete/formatting

Install Live Sass Compiler (currently by Glenn Marks)

Create a `styles.scss` file.

In blue action bar, click Watch Sass in directory containing .scss style files.

Use the output .css file as the stylesheet for yoru plain HTML.

*NOTE:* This is not necessary for most projects outside of plain HTML, like node.js, which can install Sass and use .scss directly.