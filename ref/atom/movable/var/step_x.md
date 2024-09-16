## step_x var (movable atom) 
###### BYOND Version 490

**Default value:**
+   0


This var defines the position of the atom (in pixels) relative
to its tile, on the x axis. A step_x of 5 means the atom actually is
shown 5 pixels east of the tile\'s western edge. 

The atom\'s
actual bounding box may not begin at step_x, but can be set even further
in via bound_x. 

Example: A 16×16 smiley face centered in a
32×32 icon should have the following bounds:
-   bound_x = 8
-   bound_y = 8
-   bound_width = 16
-   bound_height = 16


For the smiley to appear at the left edge of the tile it is
standing on, it would need a step_x value of -8. A step_x value of 8
takes it all the way to the rightmost edge of the tile. Anything outside
of the range -8 to 8 will have the atom straddling multiple turfs.

> [!TIP] 
> **See also:**
> +   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
> +   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 
> +   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
> +   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
> +   [locs list var (movable atom)](/ref/atom/movable/var/locs.md) 
> +   [Pixel movement](/ref/notes/pixel-movement.md) <!-- -->