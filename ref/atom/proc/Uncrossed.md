[]{#/Uncrossed proc (atom).md}    
## Uncrossed proc (atom) {#uncrossed-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](/atom/proc/Enter)    
:   [Entered proc (atom)](/atom/proc/Entered)    
:   [Exit proc (atom)](/atom/proc/Exit)    
:   [Exited proc (atom)](/atom/proc/Exited)    
:   [Cross proc (atom)](/atom/proc/Cross)    
:   [Crossed proc (atom)](/atom/proc/Crossed)    
:   [Uncross proc (atom)](/atom/proc/Uncross)    
:   [Move proc (movable atom)](/atom/movable/proc/Move)    
:   [group var (mob)](/mob/var/group)    
:   [Pixel movement](/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Format:**    
:   Uncrossed(atom/movable/O)    
<!-- -->    
**When:**    
:   Called when an object has stopped overlapping this one through a    
    call to Move(). Directly setting the object\'s loc or step_x/y vars    
    does not result in a call to Uncrossed() or any other movement    
    side-effects. The same goes for deletion of an object.    
<!-- -->    
**Args:**    
:   O: the object that moved and is no longer overlapping.    
<!-- -->    
**Default action:**    
:   none    
### Example:    
obj/pressure_plate Uncrossed(O) // if no other mobs are standing on    
it\... if(!(locate(/mob) in bounds())) // do something Release()  