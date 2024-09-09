[]{#/atom/proc/Uncrossed}    
## Uncrossed proc (atom) {#uncrossed-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](/ref/atom/proc/Enter/Enter.md)    
:   [Entered proc (atom)](/ref/atom/proc/Entered/Entered.md)    
:   [Exit proc (atom)](/ref/atom/proc/Exit/Exit.md)    
:   [Exited proc (atom)](/ref/atom/proc/Exited/Exited.md)    
:   [Cross proc (atom)](/ref/atom/proc/Cross/Cross.md)    
:   [Crossed proc (atom)](/ref/atom/proc/Crossed/Crossed.md)    
:   [Uncross proc (atom)](/ref/atom/proc/Uncross/Uncross.md)    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move/Move.md)    
:   [group var (mob)](/ref/mob/var/group/group.md)    
:   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement/pixel-movement.md)    
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