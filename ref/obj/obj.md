## obj
**See also:**
+   [atom](/ref/atom.md) 
+   [movable atoms](/ref/atom/movable.md) 
+   [procs (obj)](/ref/obj/proc.md) 
+   [vars (obj)](/ref/obj/var.md) 

There are two types of movable atoms+ objs and mobs. The
difference between them is that a mob can be attached to a human player,
and is also typically used for NPCs and creatures. The obj type is a
little bit simpler and is typically used for objects in the environment,
items in inventory, etc. 

Objects are derived from `/obj`, which
derives from `/atom/movable`. 

The following example defines the
obj type `/obj/scooper`.
### Example:

```
 obj scooper desc = \"Super pooper scooper.\" 
```
