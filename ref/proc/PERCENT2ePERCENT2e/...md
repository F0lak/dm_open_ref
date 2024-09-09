[]{#/proc/%2e%2e toc=".."}    
## .. proc    
**See also:**    
:   [. proc](/ref/proc/%2e.md)    
<!-- -->    
**Format:**    
:   ..(Args)    
<!-- -->    
**Returns:**    
:   The return value of the parent proc.    
<!-- -->    
**Args:**    
:   The arguments to pass to the parent proc. This defaults to the    
    arguments to the current proc.    
If object O is derived from object P, P is called the parent of O. If a    
proc (or verb) is defined in both O and P, O can call P\'s version by    
using ..().    
### Example:    
mob P verb/history() world \<\< \"P\" O history() world \<\< \"O\" ..()    
// call P.history()    
Here O is derived from P. When P calls \"history\", his name is    
displayed. When O calls \"history\", his name is displayed, followed by    
the name of his parent, P.    
If O overrides the same proc more than once, ..() will search for the    
previous version and use that. For instance, you could have two    
O.history() procs; the second overrides the first, but the original    
could still be called via ..(). The original in turn could call ..() to    
reach P.history(). Overriding the same proc more than once in the same    
type should be avoided wherever possible, because it incurs extra    
overhead, it makes the code harder to read, and it isn\'t always clear    
which one gets called first. (Usually, the only time you\'ll want this    
to happen is when using libraries.)    
..() can also be used for predefined procs.    
### Example:    
mob/Move() // override proc world \<\< \"moving\...\" return ..() //    
call default    
This proc will print \"moving\...\" whenever the mob moves.  