
## text2ascii (proc)

**Format:**
+   text2ascii(T,pos=1)

**Arguments:**
+   T: A text string.
+   pos: The byte position in T to use, starting at 1.

**Returns:**
+   A number representing the character's ASCII or Unicode code.
***
ASCII codes are numerical values corresponding to keyboard and special characters. Among other things, they are used to represent many symbols in HTML. This proc converts a text string to its corresponding ascii representation.


```dm

world << text2ascii("A")  // = 65
world << text2ascii("HAPPY",2)  // = 65

```


With <a href="#/{notes}/Unicode">Unicode</a>, things may get more complicated. DM stores text with UTF-8 encoding, so at this position there might be several bytes strung together to make a single character. The value of `pos` is in bytes, not characters. When the return value is 128 (0x80) or higher, multiple bytes are used for the charcter. In that case the next character position is not `pos + 1` like it is for regular text, but you can use `pos + length(ascii2text(result))` instead. Or, you can determine the byte count from this table:
***
**Related Pages:**
+    [ascii2text proc](/ref/proc/ascii2text)
+    [entities (text)](/ref/DM/text/entities)
+    [Unicode](/ref/{notes}/Unicode)
