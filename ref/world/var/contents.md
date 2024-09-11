## contents list var (world)
**See also:**
*   [list](/ref/list.md) -m<!-- -->
**Default value:**
*   List of all areas, turfs, mobs, and objs initially in the world.


This is a list of every object in the world. Objects in this
list are in no particular order.
### Example:

```
 proc/ListAreas(mob/M) var/area/A M \<\< \"Areas:\" for (A in
world.contents) M \<\< A 
```
 

This example displays a
list of every area in existence. As a convenient short-hand, one may
simply write for(A) or for(A in world) instead of the full for(A in
world.contents).