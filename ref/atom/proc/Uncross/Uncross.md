[]{#/atom/proc/Uncross}    
## Uncross proc (atom) {#uncross-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](/ref/atom/proc/Enter/Enter.md)    
:   [Entered proc (atom)](/ref/atom/proc/Entered/Entered.md)    
:   [Exit proc (atom)](/ref/atom/proc/Exit/Exit.md)    
:   [Exited proc (atom)](/ref/atom/proc/Exited/Exited.md)    
:   [Cross proc (atom)](/ref/atom/proc/Cross/Cross.md)    
:   [Crossed proc (atom)](/ref/atom/proc/Crossed/Crossed.md)    
:   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed/Uncrossed.md)    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move/Move.md)    
:   [group var (mob)](/ref/mob/var/group/group.md)    
:   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement/pixel-movement.md)    
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