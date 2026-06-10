
## copytext (proc)

**Format:**
+   copytext(T,Start=1,End=0)

**Arguments:**
+   T:     A text string.
+   Start: The text byte position in which to begin the copy.
+   End: The text byte position immediately following the last character to be copied.

**Returns:**
+   A text string.
***
Copy characters in T between Start and End. The default end position of 0 stands for `length(T)+1`, so by default the entire text string is copied.


```dm

pre = copytext("Hi there",1,3))// = "Hi"
post = copytext("Hi there",4)) // = "there"

```


If the start or end position is negative, it counts backwards from the end of the string.


```dm

post = copytext("Hi there",-5)) // = "there"

```


Note: In strings containing non-ASCII characters, byte position and character position are not the same thing. Use `copytext_char()` to work with character counts instead of bytes, at a performance cost. See the <a href="#/{notes}/Unicode">Unicode</a> section for more information.
***
**Related Pages:**
+    [splicetext proc](/ref/proc/splicetext)
+    [findtext proc](/ref/proc/findtext)
+    [splittext proc](/ref/proc/splittext)
+    [trimtext proc](/ref/proc/trimtext)
+    [Copy proc (list)](/ref/list/proc/Copy)
