[]{#/var}    
## vars    
**See also:**    
:   [path operators](/ref/operator/path/path.md)    
:   [vars (atom)](/ref/atom/var/var.md)    
:   [vars (client)](/ref/client/var/var.md)    
:   [vars (datum)](/ref/datum/var/var.md)    
:   [vars (mob)](/ref/mob/var/var.md)    
Variables are derived from var.    
**Variable Declaration Format:**    
:   var/Type/Name = Value    
:   var Type/Name = Value    
Value defaults to null.    
The hard-coded types are:    
:   [datum](/ref/datum/datum.md) (ancestor of all objects)    
:   [atom](/ref/atom/atom.md) (all mappable objects)    
:   [atom/movable](/ref/atom/movable/movable.md) (objs and mobs)    
:   [obj](/ref/obj/obj.md)    
:   [mob](/ref/mob/mob.md)    
:   [turf](/ref/turf/turf.md)    
:   [area](/ref/area/area.md)    
:   [savefile](/ref/savefile/savefile.md)    
:   [client](/ref/client/client.md)    
:   [list](/ref/list/list.md)    
:   [world](/ref/world/world.md)    
<!-- -->    
Type modifiers:    
:   [global](/ref/var/global/global.md)    
:   [const](/ref/var/const/const.md)    
:   [tmp](/ref/var/tmp/tmp.md)    
:   [final](/ref/var/final/final.md)    
User types may be derived from anything except for `/world`, `/list`,    
`/client`, and `/savefile`.  