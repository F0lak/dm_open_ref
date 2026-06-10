
## regex (proc)

**Format:**
+   regex(pattern, flags)
+   regex(Regex)

**Arguments:**
+   pattern: The pattern string to search for
+   flags: (optional) A text string containing any combination of modifier flags
+   Regex: an existing /regex datum to copy

**Returns:**
+   A new /regex datum.
***
Creates a <a href="#/{notes}/regex">regular expression</a>, stored in a /regex datum, that can be used for searching and/or replacing text.
***
**Related Pages:**
+    [Regular expressions](/ref/{notes}/regex)
+    [regex datum](/ref/regex)
+    [regex procs](/ref/regex/proc)
+    [findtext proc](/ref/proc/findtext)
+    [replacetext proc](/ref/proc/replacetext)
+    [splittext proc](/ref/proc/splittext)
+    [REGEX_QUOTE proc](/ref/proc/REGEX_QUOTE)
