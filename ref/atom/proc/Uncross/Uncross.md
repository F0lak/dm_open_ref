[]{#/atom/proc/Uncross}    
## Uncross proc (atom) {#uncross-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](ref/atom/proc/Enter)    
:   [Entered proc (atom)](ref/atom/proc/Entered)    
:   [Exit proc (atom)](ref/atom/proc/Exit)    
:   [Exited proc (atom)](ref/atom/proc/Exited)    
:   [Cross proc (atom)](ref/atom/proc/Cross)    
:   [Crossed proc (atom)](ref/atom/proc/Crossed)    
:   [Uncrossed proc (atom)](ref/atom/proc/Uncrossed)    
:   [Move proc (movable atom)](ref/atom/movable/proc/Move)    
:   [group var (mob)](ref/mob/var/group)    
:   [Pixel movement](ref/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Format:**    
:   Uncross(atom/movable/O)    
<!-- -->    
**Returns:**    
:   1 to permit; 0 to deny.    
<!-- -->    
**When:**    
:   Called when another object attempts to stop overlapping this one.    
<!-- -->    
**Args:**    
:   O: the object attempting to get away.    
<!-- -->    
**Default action:**    
:   Allow the object to get away (returning 1)  