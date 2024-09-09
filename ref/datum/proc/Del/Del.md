[]{#/datum/proc/Del}    
## Del proc (datum)    
**See also:**    
:   [del proc](/ref/proc/del/del.md)    
:   [garbage collection](/ref/DM/garbage/garbage.md)    
<!-- -->    
**Format:**    
:   Del()    
<!-- -->    
**When:**    
:   Called when the object is destroyed, for example by using the `del`    
    instruction.    
<!-- -->    
**Default action:**    
:   Delete the object. The contents of atomic objects are also destroyed    
    at this time, as though `del` were called on each one of them.    
When the world is destroyed, the `Del()` proc is not automatically    
called. The only object for which it is called is [/world](/ref/world/world.md). If    
you need the `Del()` proc for a particular object to be called at that    
time, you should explicitly call it from `world/Del()`.    
Note: **Always** call `..()` at the end of the proc if you override it.  