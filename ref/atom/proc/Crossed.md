## Crossed proc (atom) 
###### BYOND Version 490
**See also:**
*   [Enter proc (atom)](/ref/atom/proc/Enter.md) -m
*   [Entered proc (atom)](/ref/atom/proc/Entered.md) -m
*   [Exit proc (atom)](/ref/atom/proc/Exit.md) -m
*   [Exited proc (atom)](/ref/atom/proc/Exited.md) -m
*   [Cross proc (atom)](/ref/atom/proc/Cross.md) -m
*   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) -m
*   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) -m
*   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) -m
*   [group var (mob)](/ref/mob/var/group.md) -m
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) -m<!-- -->
**Format:**
*   Crossed(atom/movable/O)
<!-- -->
**When:**
*   Called when an object has overlapped this one through Move().
    Directly setting the object\'s loc or step_x/y vars does not result
    in a call to Crossed() or any other movement side-effects. The same
    goes for creation or deletion of an object at a location.
<!-- -->
**Args:**
*   O* the object that moved and is now overlapping.
<!-- -->
**Default action:**
*   none
### Example:

```
 obj/landmine Crossed(O) O \<\< \"You stepped on a land
mine!\" Explode() 
```
