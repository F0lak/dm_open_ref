## next var (regex) 
###### BYOND Version 510


If this is a global pattern (using the \"g\" flag), then after
a call to Find() this var contains the index where next Find() should
begin. 

Replace() on a non-global pattern will also store the
index of the next place to begin a search here. The position to search
will be based on the replaced text, which is stored in the text var.

> [!TIP] 
> **See also:**
> +   [regex datum](/ref/regex.md) 
> +   [Find proc (regex)](/ref/regex/proc/Find.md) 
> +   [Replace proc (regex)](/ref/regex/proc/Replace.md) 
> +   [index var (regex)](/ref/regex/var/index.md) 
> +   [match var (regex)](/ref/regex/var/match.md) 