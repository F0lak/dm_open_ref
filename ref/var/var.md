## vars
**See also:**
+   [path operators](/ref/operator/path.md) 
+   [vars (atom)](/ref/atom/var.md) 
+   [vars (client)](/ref/client/var.md) 
+   [vars (datum)](/ref/datum/var.md) 
+   [vars (mob)](/ref/mob/var.md) 


Variables are derived from var.
**Variable Declaration Format:**
+   var/Type/Name = Value
+   var Type/Name = Value


Value defaults to null.
The hard-coded types are:
+   [datum](/ref/datum.md)  (ancestor of all objects)
+   [atom](/ref/atom.md)  (all mappable objects)
+   [atom/movable](/ref/atom/movable.md)  (objs and mobs)
+   [obj](/ref/obj.md) 
+   [mob](/ref/mob.md) 
+   [turf](/ref/turf.md) 
+   [area](/ref/area.md) 
+   [savefile](/ref/savefile.md) 
+   [client](/ref/client.md) 
+   [list](/ref/list.md) 
+   [world](/ref/world.md) 
<!-- -->
Type modifiers:
+   [global](/ref/var/global.md) 
+   [const](/ref/var/const.md) 
+   [tmp](/ref/var/tmp.md) 
+   [final](/ref/var/final.md) 

User types may be derived from anything except for `/world`,
`/list`, `/client`, and `/savefile`.