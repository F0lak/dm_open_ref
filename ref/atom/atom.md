## atom


The /atom object type is the ancestor of all mappable objects
in the game. The types /area, /turf, /obj, and /mob are all derived from
/atom. You should not create instances of /atom directly but should use
/area, /turf, /obj, and /mob for actual objects. The /atom object type
exists for the purpose of defining variables or procedures that are
shared by all of the other \"physical\" objects. These are also the only
objects for which verbs may be accessible to the user. 

/atom is
derived from /datum, so it inherits the basic properties that are shared
by all DM objects.

**See also:**
+   [area](/ref/area.md) 
+   [datum](/ref/datum.md) 
+   [mob](/ref/mob.md) 
+   [movable atoms](/ref/atom/movable.md) 
+   [obj](/ref/obj.md) 
+   [procs (atom)](/ref/atom/proc.md) 
+   [turf](/ref/turf.md) 
+   [vars (atom)](/ref/atom/var.md) 