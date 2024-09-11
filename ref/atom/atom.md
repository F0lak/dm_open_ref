## atom
**See also:**
*   [area](/ref/area.md) -m
*   [datum](/ref/datum.md) -m
*   [mob](/ref/mob.md) -m
*   [movable atoms](/ref/atom/movable.md) -m
*   [obj](/ref/obj.md) -m
*   [procs (atom)](/ref/atom/proc.md) -m
*   [turf](/ref/turf.md) -m
*   [vars (atom)](/ref/atom/var.md) -m

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