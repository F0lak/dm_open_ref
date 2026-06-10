
## ascii2text (proc)

**Format:**
+   ascii2text(N)

**Arguments:**
+   N: A number.

**Returns:**
+   A text string.
***
ASCII codes are numerical values corresponding to keyboard and special characters. Among other things, they are used to represent many symbols in HTML. This proc converts an ASCII code to its corresponding text representation.


```dm

T = ascii2text(65)  // = "A"

```


BYOND now supports <a href="#/{notes}/Unicode">Unicode</a> via UTF-8 encoding, so you can use the character code for any valid Unicode character, not just ASCII.
***
**Related Pages:**
+    [entities (text)](/ref/DM/text/entities)
+    [text2ascii proc](/ref/proc/text2ascii)
