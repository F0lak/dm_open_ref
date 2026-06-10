
## REGEX_QUOTE (proc)

**Format:**
+   REGEX_QUOTE(text)
+   REGEX_QUOTE_REPLACEMENT(text)

**Arguments:**
+   text: The text to escape

**Returns:**
+   REGEX_QUOTE: A version of the text with any special regular expression characters escaped by backslashes.
+   REGEX_QUOTE_REPLACEMENT: A version of the text with $ characters escaped by a second $.
***
Quotes a piece of text so that it can be used inside a regular expression without fear of being treated as pattern instructions.


```dm

proc/FindWord(text, word)
    // The \b pattern is a word break, to search for the word
    // on its own instead of as part of another word.
    var/regex/R = regex("\\b[REGEX_QUOTE(word)]\b", "i")
    // find the pattern in the text
    return R.Find(text)

```

***
**Related Pages:**
+    [regex proc](/ref/proc/regex)
+    [regex datum](/ref/regex)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
