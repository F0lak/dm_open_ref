
## findlasttextEx (proc)

**Format:**
+   findlasttextEx(Haystack,Needle,Start=0,End=1)

**Arguments:**
+   Haystack: The text string to search.
+   Needle: The sub-text to search for.
+   Start: The text byte position in Haystack in which to begin the search.
    Because this searches backwards, the default is the end of the string (0).
+   End: The earliest position in Haystack that can be matched as a result.

**Returns:**
+   The last position of Needle in Haystack; 0 if not found.
***
This instruction is sensitive to the case of Haystack and Needle. The case-insensitive version is findlasttext().

If the start or end position is negative, the position is counted backwards from the end of the string.

Note: Unlike findtextEx(), a regular expression may NOT be used as the Needle. Searching backwards is simply too complex for the regular expression engine.

Note: In strings containing non-ASCII characters, byte position and character position are not the same thing. Use `findlasttextEx_char()` to work with character counts instead of bytes, at a performance cost. See the <a href="#/{notes}/Unicode">Unicode</a> section for more information.
***
**Related Pages:**
+    [findtext proc](/ref/proc/findtext)
+    [findtextEx proc](/ref/proc/findtextEx)
+    [findlasttext proc](/ref/proc/findlasttext)
