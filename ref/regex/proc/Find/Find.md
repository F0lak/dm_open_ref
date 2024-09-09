[]{#/regex/proc/Find}    
## Find proc (regex) {#find-proc-regex byondver="510"}    
**See also:**    
:   [Regular expressions](ref/%7Bnotes%7D/regex)    
:   [regex datum](ref/regex)    
:   [Replace proc (regex)](ref/regex/proc/Replace)    
:   [regex vars](ref/regex/var)    
:   [regex proc](ref/proc/regex)    
:   [findtext proc](ref/proc/findtext)    
<!-- -->    
**Format:**    
:   Find(haystack, Start=1, End=0)    
<!-- -->    
**Returns:**    
:   The position of the matched text, or 0 if no match was found.    
<!-- -->    
**Args:**    
:   haystack: The text to be searched    
:   Start: The start position (in bytes) to search; defaults to 1, or to    
    src.next if this is a global pattern    
:   End: The position of the byte after the end of the search; 0 is the    
    end. The actual match is allowed to extend past End.    
Finds the regular expression pattern within the \"haystack\" text. The    
following vars are set by the match:    
-   text: The text that was searched.    
-   index: The index where the match was found (same as the return    
    value)    
-   match: The actual matched text    
-   group: If the expression contains capturing groups with the ( )    
    parentheses operator, this is a list that holds the text found in    
    those groups. group\[1\] is the first group, and so on.    
-   next: If the \"g\" flag was used to create thie expression, this is    
    the next index to begin searching.    
In a global expression (using the \"g\" flag), Find() can be called    
repeatedly on the same piece of text and the Start position will be    
advanced automatically unless you specify it.    
Note: In strings containing non-ASCII characters, byte position and    
character position are not the same thing. Use `Find_char()` to work    
with character counts instead of bytes, at a performance cost. See the    
[Unicode](@/%7Bnotes%7D/Unicode) section for more information.  