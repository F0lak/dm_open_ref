## trimtext proc 
###### BYOND Version 515


**Format:**
+   trimtext(Text)

**Returns:**
+   Text with whitespace trimmed from both ends

**Args:**
+   Text: The text string to trim.


Trims whitespace from both ends of a text string. 

All
[Unicode](/ref/notes/Unicode.md) whitespace characters are counted,
whether they can cause a break or not.

> [!TIP] 
> **See also:**
> +   [copytext proc](/ref/proc/copytext.md) 