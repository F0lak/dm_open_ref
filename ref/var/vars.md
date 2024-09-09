[]{#/var}    
## vars    
**See also:**    
:   [path operators](ref/operator/path)    
:   [vars (atom)](ref/atom/var)    
:   [vars (client)](ref/client/var)    
:   [vars (datum)](ref/datum/var)    
:   [vars (mob)](ref/mob/var)    
Variables are derived from var.    
**Variable Declaration Format:**    
:   var/Type/Name = Value    
:   var Type/Name = Value    
Value defaults to null.    
The hard-coded types are:    
:   [datum](ref/datum) (ancestor of all objects)    
:   [atom](ref/atom) (all mappable objects)    
:   [atom/movable](ref/atom/movable) (objs and mobs)    
:   [obj](ref/obj)    
:   [mob](ref/mob)    
:   [turf](ref/turf)    
:   [area](ref/area)    
:   [savefile](ref/savefile)    
:   [client](ref/client)    
:   [list](ref/list)    
:   [world](ref/world)    
<!-- -->    
Type modifiers:    
:   [global](ref/var/global)    
:   [const](ref/var/const)    
:   [tmp](ref/var/tmp)    
:   [final](ref/var/final)    
User types may be derived from anything except for `/world`, `/list`,    
`/client`, and `/savefile`.  