## Exited proc (atom)
**See also:**
*   [Enter proc (atom)](/ref/atom/proc/Enter.md) -m
*   [Entered proc (atom)](/ref/atom/proc/Entered.md) -m
*   [Exit proc (atom)](/ref/atom/proc/Exit.md) -m
*   [Cross proc (atom)](/ref/atom/proc/Cross.md) -m
*   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) -m
*   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) -m
*   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) -m
*   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) -m<!-- -->
**Format:**
*   Exited(atom/movable/Obj, atom/newloc)
<!-- -->
**When:**
*   Called when an object has exited from the contents list through a
    call to Move(). Directly setting the object\'s loc or step_x/y vars
    does not result in a call to Exited() or any other movement
    side-effects. The same goes for deletion of an object.
<!-- -->
**Args:**
*   Obj* the object that exited (a mob or obj).
*   [newloc]{byondver="507"}* the object\'s new location.
<!-- -->
**Default action:**
*   None for most atoms, but turfs will call Uncrossed().