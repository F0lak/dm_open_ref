
## obj (info)
***
There are two types of movable atoms: objs and mobs. The difference between them is that a mob can be attached to a human player, and is also typically used for NPCs and creatures. The obj type is a little bit simpler and is typically used for objects in the environment, items in inventory, etc.

Objects are derived from `/obj`, which derives from `/atom/movable`.

The following example defines the obj type `/obj/scooper`.


```dm

obj
  scooper
    desc = "Super pooper scooper."

```

***
**Related Pages:**
+    [atom](/ref/atom)
+    [atom/movable](/ref/atom/movable)
+    [procs (obj)](/ref/obj/proc)
+    [vars (obj)](/ref/obj/var)
