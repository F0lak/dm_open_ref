## MeasureText proc (client) 
###### BYOND Version 513

**Format:**
+   MeasureText(text, style, width=0)
<!-- -->
**Args:**
+   text: The text to be measured
+   style: Stylesheet to be used (leave blank to use the default map
    control\'s styles, if any)
+   width: Width limit, if you only want to measure height; 0 means no
    limit
<!-- -->
**Returns:**
+   A size value in `"[width]x[height]"` format, e.g. \"60x16\"


Because maptext rendering may vary by client, `MeasureText`
lets you get a measurement of how text will be laid out, so you can
adjust `maptext_width` and `maptext_height` accordingly.

**See also:**
+   [maptext var (atom)](/ref/atom/var/maptext.md) 
+   [maptext_width var (atom)](/ref/atom/var/maptext_width.md) 
+   [maptext_height var (atom)](/ref/atom/var/maptext_height.md) <!-- -->