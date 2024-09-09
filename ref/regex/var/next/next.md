[]{#/regex/var/next}    
## next var (regex) {#next-var-regex byondver="510"}    
**See also:**    
:   [regex datum](/ref/regex/regex.md)    
:   [Find proc (regex)](/ref/regex/proc/Find/Find.md)    
:   [Replace proc (regex)](/ref/regex/proc/Replace/Replace.md)    
:   [index var (regex)](/ref/regex/var/index/index.md)    
:   [match var (regex)](/ref/regex/var/match/match.md)    
If this is a global pattern (using the \"g\" flag), then after a call to    
Find() this var contains the index where next Find() should begin.    
Replace() on a non-global pattern will also store the index of the next    
place to begin a search here. The position to search will be based on    
the replaced text, which is stored in the text var.  