
## Replace (proc)

**Format:**
+   Replace(haystack, replacement, Start=1, End=0)

**Arguments:**
+   haystack: The text to be searched
+   replacement: A piece of text, OR a proc, that will be used to replace the match
+   Start: The start position (in bytes) to search; defaults to 1, or to src.next if this is a global pattern
+   End: The position of the byte after the end of the search; 0 is the end. The actual match is allowed to extend past End.

**Returns:**
+   The original haystack string with the first match replaced.  If using the "g" flag, all matches are replaced.
***
Finds the regular expression pattern within the "haystack" text, and replaces the match with the given replacement value.

In a non-global expression (not using the "g" flag), the values of src.index and src.next are set as they would be in a global Find(). See the Find() proc for more info.

Note: In strings containing non-ASCII characters, byte position and character position are not the same thing. Use `Replace_char()` to work with character counts instead of bytes. See the <a href="#/{notes}/Unicode">Unicode</a> section for more information.

If the replacement value is text, the $ character is treated as special. If you want to use the actual dollar sign, it must be escaped with a second dollar sign. Otherwise, the $ character is one of these special values:
***
**Related Pages:**
+    [Regular expressions](/ref/{notes}/regex)
+    [regex datum](/ref/regex)
+    [Find proc (regex)](/ref/regex/proc/Find)
+    [regex vars](/ref/regex/var)
+    [regex proc](/ref/proc/regex)
+    [replacetext proc](/ref/proc/replacetext)
