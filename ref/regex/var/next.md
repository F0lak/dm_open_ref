## next var (regex) {#next-var-regex byondver="510"}    
**See also:**    
:   [regex datum](/regex)    
:   [Find proc (regex)](/regex/proc/Find)    
:   [Replace proc (regex)](/regex/proc/Replace)    
:   [index var (regex)](/regex/var/index)    
:   [match var (regex)](/regex/var/match)    
If this is a global pattern (using the \"g\" flag), then after a call to    
Find() this var contains the index where next Find() should begin.    
Replace() on a non-global pattern will also store the index of the next    
place to begin a search here. The position to search will be based on    
the replaced text, which is stored in the text var.  