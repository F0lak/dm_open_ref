## vars
**See also:**
*   [path operators](/ref/operator/path.md) -m
*   [vars (atom)](/ref/atom/var.md) -m
*   [vars (client)](/ref/client/var.md) -m
*   [vars (datum)](/ref/datum/var.md) -m
*   [vars (mob)](/ref/mob/var.md) -m


Variables are derived from var.
**Variable Declaration Format:**
*   var/Type/Name = Value
*   var Type/Name = Value


Value defaults to null.
The hard-coded types are:
*   [datum](/ref/datum.md) -m (ancestor of all objects)
*   [atom](/ref/atom.md) -m (all mappable objects)
*   [atom/movable](/ref/atom/movable.md) -m (objs and mobs)
*   [obj](/ref/obj.md) -m
*   [mob](/ref/mob.md) -m
*   [turf](/ref/turf.md) -m
*   [area](/ref/area.md) -m
*   [savefile](/ref/savefile.md) -m
*   [client](/ref/client.md) -m
*   [list](/ref/list.md) -m
*   [world](/ref/world.md) -m
<!-- -->
Type modifiers:
*   [global](/ref/var/global.md) -m
*   [const](/ref/var/const.md) -m
*   [tmp](/ref/var/tmp.md) -m
*   [final](/ref/var/final.md) -m

User types may be derived from anything except for `/world`,
`/list`, `/client`, and `/savefile`.