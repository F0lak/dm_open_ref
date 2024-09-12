## locs list var (movable atom) 
###### BYOND Version 490
**See also:**
*   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
*   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y.md) 
*   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
*   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) 
*   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
*   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
*   [loc var (atom)](/ref/atom/var/loc.md) 
*   [contents list var (atom)](/ref/atom/var/contents.md) <!-- -->
**Default value:**
*   list(src.loc)


This read-only var tells which turfs are being physically
covered by the atom\'s bounding box. The purpose of this is for cases
where you set the atom\'s bounds to change its physical size so that it
ends up covering more than one turf. 

This is different from the
loc var in that every atom still has only one \"true\" location. A
movable atom may cover multiple turfs, but only one turf is its loc. The
loc var can be thought of as an anchor point, while the actual physical
footprint is in locs. 

For every turf in locs, this atom will
also be in that turf\'s contents list. 

If loc is not a turf, it
will be the only item in the locs list. If loc is null, locs will be
empty.