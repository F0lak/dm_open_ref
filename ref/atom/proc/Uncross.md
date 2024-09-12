## Uncross proc (atom) 
###### BYOND Version 490
**See also:**
+   [Enter proc (atom)](/ref/atom/proc/Enter.md) 
+   [Entered proc (atom)](/ref/atom/proc/Entered.md) 
+   [Exit proc (atom)](/ref/atom/proc/Exit.md) 
+   [Exited proc (atom)](/ref/atom/proc/Exited.md) 
+   [Cross proc (atom)](/ref/atom/proc/Cross.md) 
+   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) 
+   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) 
+   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
+   [group var (mob)](/ref/mob/var/group.md) 
+   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) <!-- -->
**Format:**
+   Uncross(atom/movable/O)
<!-- -->
**Returns:**
+   1 to permit; 0 to deny.
<!-- -->
**When:**
+   Called when another object attempts to stop overlapping this one.
<!-- -->
**Args:**
+   O+ the object attempting to get away.
<!-- -->
**Default action:**
+   Allow the object to get away (returning 1)