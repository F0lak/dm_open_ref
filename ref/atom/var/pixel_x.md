## pixel_x var (atom)
**See also:**
+   [animate_movement var (movable
    atoms)](/ref/atom/movable/var/animate_movement.md) 
+   [glide_size var (movable atoms)](/ref/atom/movable/var/glide_size.md) 
+   [pixel_y var (atom)](/ref/atom/var/pixel_y.md) 
+   [pixel_w var (atom)](/ref/atom/var/pixel_w.md) 
+   [pixel_z var (atom)](/ref/atom/var/pixel_z.md) 
+   [icon_size var (world)](/ref/world/var/icon_size.md) 
+   [map_format var (world)](/ref/world/var/map_format.md) 
+   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) <!-- -->
**Default value:**
+   0


This displaces the object\'s icon on the x-axis by the
specified number of pixels. In a project with a standard 32x32 tile
size, this can range from -32 to +32. (You can get away with larger
displacements, but they are not guaranteed to work for objects off the
edge of the map.) 

Since overlays and images can each have their
own additional displacements, this makes it possible to create visual
effects that extend beyond the object\'s own cell in the turf grid, but
which automatically move around with the object. 

This effect is
purely visual and does not influence such things as movement bumping or
view() range calculations.