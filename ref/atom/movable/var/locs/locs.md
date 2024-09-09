[]{#/atom/movable/var/locs}    
## locs list var (movable atom) {#locs-list-var-movable-atom byondver="490"}    
**See also:**    
:   [bound_x var (movable atom)](ref/atom/movable/var/bound_x)    
:   [bound_y var (movable atom)](ref/atom/movable/var/bound_y)    
:   [bound_width var (movable atom)](ref/atom/movable/var/bound_width)    
:   [bound_height var (movable atom)](ref/atom/movable/var/bound_height)    
:   [step_x var (movable atom)](ref/atom/movable/var/step_x)    
:   [step_y var (movable atom)](ref/atom/movable/var/step_y)    
:   [loc var (atom)](ref/atom/var/loc)    
:   [contents list var (atom)](ref/atom/var/contents)    
<!-- -->    
**Default value:**    
:   list(src.loc)    
This read-only var tells which turfs are being physically covered by the    
atom\'s bounding box. The purpose of this is for cases where you set the    
atom\'s bounds to change its physical size so that it ends up covering    
more than one turf.    
This is different from the loc var in that every atom still has only one    
\"true\" location. A movable atom may cover multiple turfs, but only one    
turf is its loc. The loc var can be thought of as an anchor point, while    
the actual physical footprint is in locs.    
For every turf in locs, this atom will also be in that turf\'s contents    
list.    
If loc is not a turf, it will be the only item in the locs list. If loc    
is null, locs will be empty.  