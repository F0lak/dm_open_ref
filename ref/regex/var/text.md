## text var (regex) {#text-var-regex byondver="510"}    
**See also:**    
:   [regex datum](/regex)    
:   [Find proc (regex)](/regex/proc/Find)    
:   [index var (regex)](/regex/var/index)    
:   [match var (regex)](/regex/var/match)    
:   [next var (regex)](/regex/var/next)    
If this is a global pattern (using the \"g\" flag), then after a call to    
Find() this var contains the text that was searched. If that same text    
is searched again, the next var is the default starting position.    
Replace() on a non-global pattern will store the text *after*    
replacement here.  