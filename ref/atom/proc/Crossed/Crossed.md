[]{#/atom/proc/Crossed}    
## Crossed proc (atom) {#crossed-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](/ref/atom/proc/Enter/Enter.md)    
:   [Entered proc (atom)](/ref/atom/proc/Entered/Entered.md)    
:   [Exit proc (atom)](/ref/atom/proc/Exit/Exit.md)    
:   [Exited proc (atom)](/ref/atom/proc/Exited/Exited.md)    
:   [Cross proc (atom)](/ref/atom/proc/Cross/Cross.md)    
:   [Uncross proc (atom)](/ref/atom/proc/Uncross/Uncross.md)    
:   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed/Uncrossed.md)    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move/Move.md)    
:   [group var (mob)](/ref/mob/var/group/group.md)    
:   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement/pixel-movement.md)    
<!-- -->    
**Format:**    
:   Crossed(atom/movable/O)    
<!-- -->    
**When:**    
:   Called when an object has overlapped this one through Move().    
    Directly setting the object\'s loc or step_x/y vars does not result    
    in a call to Crossed() or any other movement side-effects. The same    
    goes for creation or deletion of an object at a location.    
<!-- -->    
**Args:**    
:   O: the object that moved and is now overlapping.    
<!-- -->    
**Default action:**    
:   none    
### Example:    
obj/landmine Crossed(O) O \<\< \"You stepped on a land mine!\" Explode()  