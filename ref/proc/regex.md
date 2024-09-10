## regex proc {#regex-proc byondver="510"}    
**See also:**    
:   [Regular expressions](/%7Bnotes%7D/regex)    
:   [regex datum](/regex)    
:   [regex procs](/regex/proc)    
:   [findtext proc](/proc/findtext)    
:   [replacetext proc](/proc/replacetext)    
:   [splittext proc](/proc/splittext)    
:   [REGEX_QUOTE proc](/proc/REGEX_QUOTE)    
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
Creates a [regular expression](/%7Bnotes%7D/regex), stored in a /regex    
datum, that can be used for searching and/or replacing text.  