
## Find (proc)

**Format:**
+   Find(haystack, Start=1, End=0)

**Arguments:**
+   haystack: The text to be searched
+   Start: The start position (in bytes) to search; defaults to 1, or to src.next if this is a global pattern
+   End: The position of the byte after the end of the search; 0 is the end. The actual match is allowed to extend past End.

**Returns:**
+   The position of the matched text, or 0 if no match was found.
***
Finds the regular expression pattern within the "haystack" text. The following vars are set by the match:

In a global expression (using the "g" flag), Find() can be called repeatedly on the same piece of text and the Start position will be advanced automatically unless you specify it.

Note: In strings containing non-ASCII characters, byte position and character position are not the same thing. Use `Find_char()` to work with character counts instead of bytes, at a performance cost. See the <a href="#/{notes}/Unicode">Unicode</a> section for more information.
***
**Related Pages:**
+    [Regular expressions](/ref/{notes}/regex)
+    [regex datum](/ref/regex)
+    [Replace proc (regex)](/ref/regex/proc/Replace)
+    [regex vars](/ref/regex/var)
+    [regex proc](/ref/proc/regex)
+    [findtext proc](/ref/proc/findtext)
