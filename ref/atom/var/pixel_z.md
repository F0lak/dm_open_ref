## pixel_z var (atom)

    atoms)](/ref/atom/movable/var/animate_movement.md) 
+   [glide_size var (movable atoms)](/ref/atom/movable/var/glide_size.md) 
+   [pixel_x var (atom)](/ref/atom/var/pixel_x.md) 
+   [pixel_y var (atom)](/ref/atom/var/pixel_y.md) 
+   [pixel_w var (atom)](/ref/atom/var/pixel_w.md) 
+   [icon_size var (world)](/ref/world/var/icon_size.md) 
+   [map_format var (world)](/ref/world/var/map_format.md) <!-- -->
**Default value:**
+   0


This displaces the object\'s icon vertically by the specified
number of pixels. This is meant to be used in situations where
world.map_format is used to display something other than a top-down
form, for instance in an isometric or side-view display. In a top-down
mode pixel_z behaves the same as pixel_y, except that it does not rotate
with changes to client.dir. 

This effect is purely visual and
does not influence such things as movement bumping or view() range
calculations.

> [!TIP] 
> **See also:**
> +   [animate_movement var (movable