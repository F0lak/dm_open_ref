## Exit proc (atom)
**See also:**
+   [Enter proc (atom)](/ref/atom/proc/Enter.md) 
+   [Entered proc (atom)](/ref/atom/proc/Entered.md) 
+   [Exited proc (atom)](/ref/atom/proc/Exited.md) 
+   [Cross proc (atom)](/ref/atom/proc/Cross.md) 
+   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) 
+   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) 
+   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) 
+   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
+   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
<!-- -->
**Format:**
+   Exit(atom/movable/O, atom/newloc)
<!-- -->
**Returns:**
+   1 to permit; 0 to deny.
<!-- -->
**When:**
+   Called when an object attempts to exit the contents list.
<!-- -->
**Args:**
+   O: the object attempting to exit.
+   [newloc]{byondver="507"}: the object\'s new location.
<!-- -->
**Default action:**
+   Turfs will call Uncross() and return that value (1 by default). All
    others allow the object to exit (returning 1).


By default, every atom returns 1 to allow exit, except for
turfs which call Uncross() to handle it for them. 
> [!NOTE]
> The following
behavior only applies to
[LEGACY_MOVEMENT_MODE](/ref/world/var/movement_mode.md). In all other
movement modes, the turf\'s contents are not taken into account. Only
the result of turf.Uncross() matters. 

In the default Exit
handler for turfs, Uncross() is called for the turf itself and then
Uncross() will also be called for any atoms in turf.contents that cover
the entire tile. If any Uncross() call fails, Exit() fails too and will
return 0. In games using pixel movement, Uncross() is usually called
separately, but this allows projects using tile-based movement instead
to benefit from Cross() and Uncross().