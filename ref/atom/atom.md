[]{#/atom}
  ## atom
  **See also:**
  :   [area](ref/area)
  :   [datum](ref/datum)
  :   [mob](ref/mob)
  :   [movable atoms](ref/atom/movable)
  :   [obj](ref/obj)
  :   [procs (atom)](ref/atom/proc)
  :   [turf](ref/turf)
  :   [vars (atom)](ref/atom/var)
  The /atom object type is the ancestor of all mappable objects in the
  game. The types /area, /turf, /obj, and /mob are all derived from /atom.
  You should not create instances of /atom directly but should use /area,
  /turf, /obj, and /mob for actual objects. The /atom object type exists
  for the purpose of defining variables or procedures that are shared by
  all of the other \"physical\" objects. These are also the only objects
  for which verbs may be accessible to the user.
  /atom is derived from /datum, so it inherits the basic properties that
  are shared by all DM objects.