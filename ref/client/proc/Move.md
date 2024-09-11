## Move proc (client)
**See also:**
*   [East proc (client)](/ref/client/proc/East.md) -m
*   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) -m
*   [North proc (client)](/ref/client/proc/North.md) -m
*   [Northeast proc (client)](/ref/client/proc/Northeast.md) -m
*   [Northwest proc (client)](/ref/client/proc/Northwest.md) -m
*   [South proc (client)](/ref/client/proc/South.md) -m
*   [Southeast proc (client)](/ref/client/proc/Southeast.md) -m
*   [Southwest proc (client)](/ref/client/proc/Southwest.md) -m
*   [West proc (client)](/ref/client/proc/West.md) -m<!-- -->
**Format:**
*   Move(loc,dir)
<!-- -->
**Returns:**
*   1 on success; 0 on failure
<!-- -->
**When:**
*   Called by the direction procs.
<!-- -->
**Default action:**
*   Calls src.mob.Move(). Also cancels any automated movement by calling
    walk(usr,0).