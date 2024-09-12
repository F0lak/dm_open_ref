## contents list var (atom)
**See also:**
*   [Enter proc (atom)](/ref/atom/proc/Enter.md) 
*   [Entered proc (atom)](/ref/atom/proc/Entered.md) 
*   [Exit proc (atom)](/ref/atom/proc/Exit.md) 
*   [Exited proc (atom)](/ref/atom/proc/Exited.md) 
*   [locs list var (movable atom)](/ref/atom/movable/var/locs.md) 
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) 
*   [list](/ref/list.md) 
*   [loc var (atom)](/ref/atom/var/loc.md) 
<!-- -->
**Default value:**
*   List of contained objects.


Except in the case of areas, this list is always restricted to
objs and mobs (ie movable objects). Only direct contents are listed.
Items inside of a bag object, for example, would not show up in the
mob\'s contents list. 

The contents of areas are a little
different. The turfs contained in the area are in the list along with
any objs or mobs directly contained by those turfs. 

If a
movable atom uses the bound vars to change its physical size, or
`step_x` or `step_y` to change its position, it may cover more than one
turf. In that case, those turfs\' contents won\'t just contain anything
directly in them, but also any atoms overhanging them. I.e., if a turf
is in a mob\'s `locs` list, then the mob is in that turf\'s contents
list. (See [locs](/ref/atom/movable/var/locs.md) .code} for more information.)
Note* Looping through all of the atoms, or even just turfs, in a
particular area actually loops through every turf in the world. E.g.,
`for(var/turf/T in area)`. The engine will check each turf to see if it
belongs to that area, and then includes the turf and/or its contents in
the results depending on what the loop is looking for. This also applies
to any situation where you might grab area.contents as a list, e.g.
`area.contents.Copy()`. Therefore in a large world, it\'s advisable not
to loop through area contents at all.