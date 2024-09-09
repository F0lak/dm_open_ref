[]{#/regex/var/text}    
## text var (regex) {#text-var-regex byondver="510"}    
**See also:**    
:   [regex datum](/ref/regex.md)    
:   [Find proc (regex)](/ref/regex/proc/Find.md)    
:   [index var (regex)](/ref/regex/var/index.md)    
:   [match var (regex)](/ref/regex/var/match.md)    
:   [next var (regex)](/ref/regex/var/next.md)    
If this is a global pattern (using the \"g\" flag), then after a call to    
Find() this var contains the text that was searched. If that same text    
is searched again, the next var is the default starting position.    
Replace() on a non-global pattern will store the text *after*    
replacement here.  