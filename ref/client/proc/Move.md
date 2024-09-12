## Move proc (client)

**Format:**
+   Move(loc,dir)
<!-- -->
**Returns:**
+   1 on success; 0 on failure
<!-- -->
**When:**
+   Called by the direction procs.
<!-- -->
**Default action:**
+   Calls src.mob.Move(). Also cancels any automated movement by calling
    walk(usr,0).

**See also:**
+   [East proc (client)](/ref/client/proc/East.md) 
+   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
+   [North proc (client)](/ref/client/proc/North.md) 
+   [Northeast proc (client)](/ref/client/proc/Northeast.md) 
+   [Northwest proc (client)](/ref/client/proc/Northwest.md) 
+   [South proc (client)](/ref/client/proc/South.md) 
+   [Southeast proc (client)](/ref/client/proc/Southeast.md) 
+   [Southwest proc (client)](/ref/client/proc/Southwest.md) 
+   [West proc (client)](/ref/client/proc/West.md) <!-- -->