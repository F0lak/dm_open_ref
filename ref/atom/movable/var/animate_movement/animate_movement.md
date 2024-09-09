[]{#/atom/movable/var/animate_movement}    
## animate_movement var (movable atoms)    
**See also:**    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move/Move.md)    
:   [glide_size var (movable atoms)](/ref/atom/movable/var/glide_size/glide_size.md)    
:   [Gliding](/ref/%7Bnotes%7D/gliding/gliding.md)    
<!-- -->    
**Default value:**    
:   FORWARD_STEPS (1)    
<!-- -->    
**Possible values:**    
:   NO_STEPS (0)    
:   FORWARD_STEPS (1)    
:   SLIDE_STEPS (2)    
:   SYNC_STEPS (3)    
Setting this to 0 causes movement between two adjacent positions to be    
displayed as a single discrete jump. Otherwise, objects will be made to    
glide from one position to another, using the movement animation defined    
in the icon file if one is defined.    
By default, movement animation avoids cutting corners, since this can    
look very bad in some games. If you want objects to take the shortest    
(and smoothest) visual path when moving around, use `SLIDE_STEPS`    
instead of the default `FORWARD_STEPS`. This also allows the object to    
be facing in a different direction than it is moving, so make sure this    
is what you want.    
`SYNC_STEPS` is intended for objects that move in unison as part of a    
larger \"conglomerate\" object. You should set the movement animation to    
`SYNC_STEPS` on all but a single \"head\" object, which will serve as    
the leader when choosing pixel step sizes. If you do not use    
`SYNC_STEPS`, there are cases where the pixel offsets of objects may get    
out of sync during motion, causing the object to visually break up.    
Because of the advent of features like big icons, this value is no    
longer of much use.    
Note: This setting has no impact when used with pixel movement, except    
in special cases. See [Gliding](/ref/%7Bnotes%7D/gliding/gliding.md) for more details.  