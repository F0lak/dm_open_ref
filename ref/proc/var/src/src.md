[]{#/proc/var/src}    
## src var (proc)    
**See also:**    
:   [usr var (proc)](ref/proc/var/src)    
:   [procs](ref/proc)    
:   [verbs](ref/verb)    
This is a variable equal to the object containing the proc or verb. It    
is defined to have the same type as that object.    
### Example:    
obj/bread verb/eat() world \<\< \"\[usr\] eats \[src\]\"    
If a player named \"Bob\" calls \"eat bread\", the output will be \"Bob    
eats the bread.\"    
Note that `src` has no meaning for global procs, derived from `/proc`,    
unless they are invoked as verbs (by being attached to a [verb    
list](ref/atom/var/verbs)).  