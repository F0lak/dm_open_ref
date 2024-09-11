## Uncrossed proc (atom) 
###### BYOND Version 490
**See also:**
*   [Enter proc (atom)](/ref/atom/proc/Enter.md) -m
*   [Entered proc (atom)](/ref/atom/proc/Entered.md) -m
*   [Exit proc (atom)](/ref/atom/proc/Exit.md) -m
*   [Exited proc (atom)](/ref/atom/proc/Exited.md) -m
*   [Cross proc (atom)](/ref/atom/proc/Cross.md) -m
*   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) -m
*   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) -m
*   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) -m
*   [group var (mob)](/ref/mob/var/group.md) -m
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) -m<!-- -->
**Format:**
*   Uncrossed(atom/movable/O)
<!-- -->
**When:**
*   Called when an object has stopped overlapping this one through a
    call to Move(). Directly setting the object\'s loc or step_x/y vars
    does not result in a call to Uncrossed() or any other movement
    side-effects. The same goes for deletion of an object.
<!-- -->
**Args:**
*   O* the object that moved and is no longer overlapping.
<!-- -->
**Default action:**
*   none
### Example:

```
 obj/pressure_plate Uncrossed(O) // if no other mobs are
standing on it\... if(!(locate(/mob) in bounds())) // do something
Release() 
```
