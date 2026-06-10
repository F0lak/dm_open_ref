
## MeasureText (proc)

**Format:**
+   MeasureText(text, style, width=0)

**Arguments:**
+   text: The text to be measured
+   style: Stylesheet to be used (leave blank to use the default map control's styles, if any)
+   width: Width limit, if you only want to measure height; 0 means no limit

**Returns:**
+   A size value in  format, e.g. "60x16"
***
Because maptext rendering may vary by client, `MeasureText` lets you get a measurement of how text will be laid out, so you can adjust `maptext_width` and `maptext_height` accordingly.
***
**Related Pages:**
+    [maptext](/ref/atom/var/maptext)
+    [maptext_width](/ref/atom/var/maptext_width)
+    [maptext_height](/ref/atom/var/maptext_height)
