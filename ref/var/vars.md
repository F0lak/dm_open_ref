[]{#/var}
## vars
**See also:**
:   [path operators](#/operator/path)
:   [vars (atom)](#/atom/var)
:   [vars (client)](#/client/var)
:   [vars (datum)](#/datum/var)
:   [vars (mob)](#/mob/var)
Variables are derived from var.
**Variable Declaration Format:**
:   var/Type/Name = Value
:   var Type/Name = Value
Value defaults to null.
The hard-coded types are:
:   [datum](#/datum) (ancestor of all objects)
:   [atom](#/atom) (all mappable objects)
:   [atom/movable](#/atom/movable) (objs and mobs)
:   [obj](#/obj)
:   [mob](#/mob)
:   [turf](#/turf)
:   [area](#/area)
:   [savefile](#/savefile)
:   [client](#/client)
:   [list](#/list)
:   [world](#/world)
<!-- -->
Type modifiers:
:   [global](#/var/global)
:   [const](#/var/const)
:   [tmp](#/var/tmp)
:   [final](#/var/final)
User types may be derived from anything except for `/world`, `/list`,
`/client`, and `/savefile`.