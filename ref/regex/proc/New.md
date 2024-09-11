## New proc (regex) 
###### BYOND Version 510
**See also:**
*   [Regular expressions](/ref/%7Bnotes%7D/regex.md) -m
*   [regex datum](/ref/regex.md) -m
*   [regex proc](/ref/proc/regex.md) -m<!-- -->
**Format:**
*   regex(pattern, flags)
*   regex(Regex)
<!-- -->
**Args:**
*   pattern* The pattern string to search for
*   flags* (optional) A text string containing any combination of
    modifier flags
*   Regex* an existing /regex datum to copy


Calling new/regex() is the same as calling regex(). It will
create a new /regex datum.