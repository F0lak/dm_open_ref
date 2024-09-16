## Enter proc (atom)

<!-- -->
**Format:**
+   Enter(atom/movable/O, atom/oldloc)
<!-- -->
**Returns:**
+   1 to permit; 0 to deny.
<!-- -->
**When:**
+   Called when an object attempts to enter the contents list.
<!-- -->
**Args:**
+   O: the object attempting to enter.
+   oldloc: the old (current) loc of the object attempting to enter.
<!-- -->
**Default action:**
+   Explained below.


Areas, objs, and mobs will always permit anything to enter by
default. 
> [!
> [!NOTE]
> ]
> The following behavior only applies to
[LEGACY_MOVEMENT_MODE](/ref/world/var/movement_mode.md). In all other
movement modes, the turf\'s contents are not taken into account. Only
the result of turf.Cross() matters. 

Turfs will return 1
(permit) or 0 (deny) based on density. In simple terms, if the atom that
is entering is dense, then the turf will deny entry if the turf itself
or its contents (any that take up the full tile) are dense.


What actually happens in turf.Enter() is more detailed: Cross()
is called for the turf, and if it succeeds (movement is permitted), then
Cross() is called for any atoms in turf.contents that cover the entire
tile. If any Cross() call fails, Enter() fails too and will return 0.


If a mob is standing on a turf but its bounding box does not
cover the whole tile, it is ignored by Enter(). Instead, its Cross()
proc is called if there is a danger of the object overlapping it.

> [!TIP] 
> **See also:**
> +   [Entered proc (atom)](/ref/atom/proc/Entered.md) 
> +   [Exit proc (atom)](/ref/atom/proc/Exit.md) 
> +   [Exited proc (atom)](/ref/atom/proc/Exited.md) 
> +   [Cross proc (atom)](/ref/atom/proc/Cross.md) 
> +   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) 
> +   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) 
> +   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) 
> +   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
> +   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
> +   [Pixel movement](/ref/notes/pixel-movement.md) 