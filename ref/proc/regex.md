## regex proc 
###### BYOND Version 510
**See also:**
*   [Regular expressions](/ref/%7Bnotes%7D/regex.md) -m
*   [regex datum](/ref/regex.md) -m
*   [regex procs](/ref/regex/proc.md) -m
*   [findtext proc](/ref/proc/findtext.md) -m
*   [replacetext proc](/ref/proc/replacetext.md) -m
*   [splittext proc](/ref/proc/splittext.md) -m
*   [REGEX_QUOTE proc](/ref/proc/REGEX_QUOTE.md) -m
<!-- -->
**Format:**
*   regex(pattern, flags)
*   regex(Regex)
<!-- -->
**Returns:**
*   A new /regex datum.
<!-- -->
**Args:**
*   pattern* The pattern string to search for
*   flags* (optional) A text string containing any combination of
    modifier flags
*   Regex* an existing /regex datum to copy


Creates a [regular expression](/ref/%7Bnotes%7D/regex.md) -m stored in
a /regex datum, that can be used for searching and/or replacing text.