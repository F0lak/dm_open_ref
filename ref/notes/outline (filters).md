## Outline filter 
###### BYOND Version 512

Format:
+   filter(type=\"outline\", \...)
<!-- -->
Args:
+   size: Width in pixels (defaults to 1)
+   color: Outline color (defaults to black)
+   flags: Defaults to 0 (see below)


Applies an outline to this image. 

At larger sizes, the
outline is less accurate and will take more passes to produce.
Performance and appearance are best at sizes close to 1 or less.


`flags` can be a combination of the following values:
0
+   Ordinary outline
OUTLINE_SHARP
+   Avoid antialiasing in the outline
OUTLINE_SQUARE
+   Extend the outline sharply from corner pixels; for a box this will
    maintain a box shape without rounded corners

> [!TIP] 
> **See also:**
> +   [Drop shadow (filters)](/ref/%7Bnotes%7D/filters/drop_shadow.md) <!-- -->