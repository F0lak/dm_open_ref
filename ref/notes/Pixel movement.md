[]{#/{notes}/pixel-movement toc="Pixel movement"}    
## Pixel movement {#pixel-movement byondver="490"}    
**See also:**    
:   *Bounding boxes*    
:   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md)    
:   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y.md)    
:   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md)    
:   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md)    
:   [icon_w var (atom)](/ref/atom/var/icon_w.md)    
:   [icon_z var (atom)](/ref/atom/var/icon_z.md)    
:   *Speed and position*    
:   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md)    
:   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md)    
:   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md)    
:   [locs list var (movable atom)](/ref/atom/movable/var/locs.md)    
:   [contents list var (atom)](/ref/atom/var/contents.md)    
:   [fps var (world)](/ref/world/var/fps.md)    
:   *Movement*    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md)    
:   [Cross proc (atom)](/ref/atom/proc/Cross.md)    
:   [Crossed proc (atom)](/ref/atom/proc/Crossed.md)    
:   [Uncross proc (atom)](/ref/atom/proc/Uncross.md)    
:   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md)    
:   [movement_mode var (world)](/ref/world/var/movement_mode.md)    
:   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md)    
:   *Other topics*    
:   [bounds proc](/ref/proc/bounds.md)    
:   [bounds_dist proc](/ref/proc/bounds_dist.md)    
:   [Gliding](/ref/%7Bnotes%7D/gliding.md)    
Pixel movement is a concept that allows atoms to escape the constraints    
of BYOND\'s historically tile-based movement, and move in smaller steps.    
In the past this had to be done with soft code, but that was sometimes    
inconvenient and it did not perform as well in projects with many    
objects moving.    
The key to understanding pixel movement is to use the bound and step    
vars. You use the bound family of vars to define a bounding box for a    
movable atom, instead of just making it one full tile in size. The step    
vars can give it a movement speed and offset it from the corner of the    
tile it\'s standing on.    
-   bound_x: The left edge of the bounding box    
-   bound_y: The bottom edge of the bounding box    
-   bound_width: Width of the bounding box    
-   bound_height: Height of the bounding box    
-   step_size: default movement speed    
-   step_x: x offset from the corner of loc    
-   step_y: y offset from the corner of loc    
Those are for movable atoms only; they do not apply to turfs.    
If [world.movement_mode](/ref/world/var/movement_mode.md){.code} is set to    
`TILED_MOVEMENT_MODE`, all movable atoms must be aligned to the tile    
grid: their step_x/y/size values must be multiples of the icon size, and    
their bounds must also land on tile boundaries although the atom can be    
bigger than one tile. In other movement modes you can specify that only    
specific atoms use this behavior, by giving them the    
[TILE_MOVER](/ref/atom/var/appearance_flags.md){.code} appearance flag.    
### Bounding boxes    
::: {.sidebar .embed-image}    
![](data:image/png;charset=utf-8;base64,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)    
**Left:** The bounding box (blue) is the only part of the mob that    
actually collides with anything. By default, it would cover the whole    
turf (brown). Any turfs covered by the bounding box are in the mob\'s    
locs var. **Right:** The atom\'s true position (shaded) is offset from    
the turf by step_x and step_y.    
:::    
As an example, if your players\' mobs have icons that only cover the    
center 24×24 pixels of a regular 32×32 icon, then you would set the    
mobs\' bound_x and bound_y to 4\--because there are 4 pixels unused to    
the left and bottom\--and bound_width and bound_height to 24.    
The mob\'s physical location on the map depends on four things: Its loc,    
its step_x/y values, its bound_x/y values, and its bound_width/height.    
The lower left corner of the bounding box, relative to the turf the mob    
is actually standing on, begins at step_x+bound_x on the left and    
step_y+bound_y on the bottom.    
The physical position of the bounding box is **not affected** by the    
pixel_x/y/z vars. Those are still strictly visual offsets.    
The turfs the mob is covering can be read from the read-only locs var.    
The mob will also appear in the contents of those turfs.    
Note: This means if an atom is in a turf\'s contents, its loc is *not    
necessarily* that turf. The contents list is made to include    
\"overhangers\" from another tile for ease of use.    
### Movement    
All of the step and walk procs have been upgraded to take an additional    
argument, which is the speed at which the atom should move. If that    
argument is left out, the atom\'s own step_size is used by default. The    
step_size determines how fast the step_x and step_y values will change    
when moving.    
Move() has two new arguments that handle the position change gracefully.    
These are the step_x and step_y values for the target location.    
Pixel movement changes the behavior of the Move() proc, because a lot of    
things are possible that were not possible when BYOND only supported    
moving one tile at a time. For starters, a Move() is either a \"slide\"    
or a \"jump\" depending on the distance. A slide is when the move can be    
stopped partway; a jump is strictly pass/fail. Anything greater than one    
tile *and* the mover\'s regular step_size is considered a jump. Changing    
z levels is also a jump, as is moving to/from a non-turf.    
If step_x and step_y aren\'t within a good range, the new loc and the    
step_x/y values may be changed so that the southwest corner of the    
mover\'s bounding box is standing on its actual loc, or as close to it    
as possible.    
Enter() and Exit() can be called for several turfs and/or areas, not    
just one at a time. It is also possible for them not to be called at    
all, if the moving atom moves within a turf but doesn\'t cross a new    
turf boundary. Enter() and Exit() are only called when first attempting    
to enter or fully exit. The behavior of these procs depends on    
[world.movement_mode](/ref/world/var/movement_mode.md){.code}; in legacy mode,    
they look at some of the contents of the turfs as well as the turfs    
themselves, to preserve behavior found in older BYOND versions.    
Cross() and Uncross() are the equivalent of Enter() and Exit() but apply    
to objects the mover will either overlap or stop overlapping. (For    
turfs, Enter() and Exit() call these procs by default, since the mover    
is both stepping *into* and *onto* a turf.) Likewise Crossed() and    
Uncrossed() are the equivalents of Entered() and Exited().    
If an atom is sliding, its movement can be halted if it encounters an    
obstacle partway along its route. Bump() will still be called for any    
obstacles the atom runs into, but Move() will return the number of    
pixels moved (the most in any direction). When sliding at a speed so    
fast that the distance is bigger than the atom itself, the move will be    
split up into several smaller slides to avoid skipping over any    
obstacles.    
Gliding, which is used to show smooth movement between atoms in tile    
movement, is mostly not used in pixel movement. It only applies when the    
client uses a higher [fps](/ref/client/var/fps.md){.code} than the server.    
### Pixel procs    
The bounds() and obounds() procs have been added to grab a list of atoms    
within a given bounding box. That box can be relative to an atom, or in    
absolute coordinates.    
bounds_dist() tells the distance between two atoms, in pixels. If it is    
positive, that is the minimum distance the atoms would have to traverse    
to be touching. At 0, they are touching but not in collision. A negative    
value means the two atoms are in collision.  