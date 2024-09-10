[]{#/Crossed proc (atom).md}    
## Crossed proc (atom) {#crossed-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)]/atom/proc/Enter    
:   [Entered proc (atom)]/atom/proc/Entered    
:   [Exit proc (atom)]/atom/proc/Exit    
:   [Exited proc (atom)]/atom/proc/Exited    
:   [Cross proc (atom)]/atom/proc/Cross    
:   [Uncross proc (atom)]/atom/proc/Uncross    
:   [Uncrossed proc (atom)]/atom/proc/Uncrossed    
:   [Move proc (movable atom)]/atom/movable/proc/Move    
:   [group var (mob)]/mob/var/group    
:   [Pixel movement]/%7Bnotes%7D/pixel-movement    
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