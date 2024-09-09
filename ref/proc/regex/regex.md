[]{#/proc/regex}    
## regex proc {#regex-proc byondver="510"}    
**See also:**    
:   [Regular expressions](/ref/%7Bnotes%7D/regex/regex.md)    
:   [regex datum](/ref/regex/regex.md)    
:   [regex procs](/ref/regex/proc/proc.md)    
:   [findtext proc](/ref/proc/findtext/findtext.md)    
:   [replacetext proc](/ref/proc/replacetext/replacetext.md)    
:   [splittext proc](/ref/proc/splittext/splittext.md)    
:   [REGEX_QUOTE proc](/ref/proc/REGEX_QUOTE/REGEX_QUOTE.md)    
<!-- -->    
**Format:**    
:   regex(pattern, flags)    
:   regex(Regex)    
<!-- -->    
**Returns:**    
:   A new /regex datum.    
<!-- -->    
**Args:**    
:   pattern: The pattern string to search for    
:   flags: (optional) A text string containing any combination of    
    modifier flags    
:   Regex: an existing /regex datum to copy    
Creates a [regular expression](/ref/%7Bnotes%7D/regex/regex.md), stored in a /regex    
datum, that can be used for searching and/or replacing text.  