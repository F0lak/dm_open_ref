## Uncross proc (atom) 
###### BYOND Version 490
**See also:**
*   [Enter proc (atom)](/ref/atom/proc/Enter.md) -m
*   [Entered proc (atom)](/ref/atom/proc/Entered.md) -m
*   [Exit proc (atom)](/ref/atom/proc/Exit.md) -m
*   [Exited proc (atom)](/ref/atom/proc/Exited.md) -m
*   [Cross proc (atom)](/ref/atom/proc/Cross.md) -m
*   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) -m
*   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) -m
*   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) -m
*   [group var (mob)](/ref/mob/var/group.md) -m
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) -m<!-- -->
**Format:**
*   Uncross(atom/movable/O)
<!-- -->
**Returns:**
*   1 to permit; 0 to deny.
<!-- -->
**When:**
*   Called when another object attempts to stop overlapping this one.
<!-- -->
**Args:**
*   O* the object attempting to get away.
<!-- -->
**Default action:**
*   Allow the object to get away (returning 1)