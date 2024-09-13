## REGEX_QUOTE proc 
###### BYOND Version 510

**Format:**
+   REGEX_QUOTE(text)
+   REGEX_QUOTE_REPLACEMENT(text)
<!-- -->
**Returns:**
+   REGEX_QUOTE: A version of the text with any special regular
    expression characters escaped by backslashes.
+   REGEX_QUOTE_REPLACEMENT: A version of the text with \$ characters
    escaped by a second \$.
<!-- -->
**Args:**
+   text: The text to escape


Quotes a piece of text so that it can be used inside a regular
expression without fear of being treated as pattern instructions.
### Example:

``` dm
 proc/FindWord(text, word) // The \\b pattern is a word
break, to search for the word // on its own instead of as part of
another word. var/regex/R = regex(\"\\\\b\[REGEX_QUOTE(word)\]\\b\",
\"i\") // find the pattern in the text return R.Find(text) 
```


> [!TIP] 
> **See also:**
> +   [regex proc](/ref/proc/regex.md) 
> +   [regex datum](/ref/regex.md) 
> +   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) <!-- -->