## Pixel movement 
###### BYOND Version 490



Pixel movement is a concept that allows atoms to escape the
constraints of BYOND\'s historically tile-based movement, and move in
smaller steps. In the past this had to be done with soft code, but that
was sometimes inconvenient and it did not perform as well in projects
with many objects moving. 

The key to understanding pixel
movement is to use the bound and step vars. You use the bound family of
vars to define a bounding box for a movable atom, instead of just making
it one full tile in size. The step vars can give it a movement speed and
offset it from the corner of the tile it\'s standing on.
-   bound_x: The left edge of the bounding box
-   bound_y: The bottom edge of the bounding box
-   bound_width: Width of the bounding box
-   bound_height: Height of the bounding box
-   step_size: default movement speed
-   step_x: x offset from the corner of loc
-   step_y: y offset from the corner of loc


Those are for movable atoms only; they do not apply to turfs.


If [world.movement_mode](/ref/world/var/movement_mode.md)  is
set to `TILED_MOVEMENT_MODE`, all movable atoms must be aligned to the
tile grid: their step_x/y/size values must be multiples of the icon
size, and their bounds must also land on tile boundaries although the
atom can be bigger than one tile. In other movement modes you can
specify that only specific atoms use this behavior, by giving them the
[TILE_MOVER](/ref/atom/var/appearance_flags.md)  appearance flag.

### Bounding boxes

As an example, if your players\' mobs have icons that only
cover the center 24×24 pixels of a regular 32×32 icon, then you would
set the mobs\' bound_x and bound_y to 4\--because there are 4 pixels
unused to the left and bottom\--and bound_width and bound_height to 24.

The mob\'s physical location on the map depends on four things:
Its loc, its step_x/y values, its bound_x/y values, and its
bound_width/height. The lower left corner of the bounding box, relative
to the turf the mob is actually standing on, begins at step_x+bound_x on
the left and step_y+bound_y on the bottom. 

The physical
position of the bounding box is **not affected** by the pixel_x/y/z
vars. Those are still strictly visual offsets. 

The turfs the
mob is covering can be read from the read-only locs var. The mob will
also appear in the contents of those turfs. 

Note: This means if
an atom is in a turf\'s contents, its loc is *not necessarily* that
turf. The contents list is made to include "overhangers" from another
tile for ease of use.

### Movement

All of the step and walk procs have been upgraded to take an
additional argument, which is the speed at which the atom should move.
If that argument is left out, the atom\'s own step_size is used by
default. The step_size determines how fast the step_x and step_y values
will change when moving. 

Move() has two new arguments that
handle the position change gracefully. These are the step_x and step_y
values for the target location. 

Pixel movement changes the
behavior of the Move() proc, because a lot of things are possible that
were not possible when BYOND only supported moving one tile at a time.
For starters, a Move() is either a "slide" or a "jump" depending on
the distance. A slide is when the move can be stopped partway; a jump is
strictly pass/fail. Anything greater than one tile *and* the mover\'s
regular step_size is considered a jump. Changing z levels is also a
jump, as is moving to/from a non-turf. 

If step_x and step_y
aren\'t within a good range, the new loc and the step_x/y values may be
changed so that the southwest corner of the mover\'s bounding box is
standing on its actual loc, or as close to it as possible.

Enter() and Exit() can be called for several turfs and/or
areas, not just one at a time. It is also possible for them not to be
called at all, if the moving atom moves within a turf but doesn\'t cross
a new turf boundary. Enter() and Exit() are only called when first
attempting to enter or fully exit. The behavior of these procs depends
on [world.movement_mode](/ref/world/var/movement_mode.md) ; in legacy
mode, they look at some of the contents of the turfs as well as the
turfs themselves, to preserve behavior found in older BYOND versions.

Cross() and Uncross() are the equivalent of Enter() and Exit()
but apply to objects the mover will either overlap or stop overlapping.
(For turfs, Enter() and Exit() call these procs by default, since the
mover is both stepping *into* and *onto* a turf.) Likewise Crossed() and
Uncrossed() are the equivalents of Entered() and Exited(). 

If an atom is sliding, its movement can be halted if it encounters an
obstacle partway along its route. Bump() will still be called for any
obstacles the atom runs into, but Move() will return the number of
pixels moved (the most in any direction). When sliding at a speed so
fast that the distance is bigger than the atom itself, the move will be
split up into several smaller slides to avoid skipping over any
obstacles. 

Gliding, which is used to show smooth movement
between atoms in tile movement, is mostly not used in pixel movement. It
only applies when the client uses a higher
[fps](/ref/client/var/fps.md) than the server.

### Pixel procs

The bounds() and obounds() procs have been added to grab a list
of atoms within a given bounding box. That box can be relative to an
atom, or in absolute coordinates. 

bounds_dist() tells the
distance between two atoms, in pixels. If it is positive, that is the
minimum distance the atoms would have to traverse to be touching. At 0,
they are touching but not in collision. A negative value means the two
atoms are in collision.

> [!TIP] 
> **See also:**
>   *Bounding boxes*
> +   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
> +   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y.md) 
> +   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
> +   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) 
> +   [icon_w var (atom)](/ref/atom/var/icon_w.md) 
> +   [icon_z var (atom)](/ref/atom/var/icon_z.md) 

>   *Speed and position*
> +   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 
> +   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
> +   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
> +   [locs list var (movable atom)](/ref/atom/movable/var/locs.md) 
> +   [contents list var (atom)](/ref/atom/var/contents.md) 
> +   [fps var (world)](/ref/world/var/fps.md) 

>   *Movement*
> +   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
> +   [Cross proc (atom)](/ref/atom/proc/Cross.md) 
> +   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) 
> +   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) 
> +   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) 
> +   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
> +   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 

>   *Other topics*
> +   [bounds proc](/ref/proc/bounds.md) 
> +   [bounds_dist proc](/ref/proc/bounds_dist.md) 
> +   [Gliding](/ref/notes/gliding.md) 