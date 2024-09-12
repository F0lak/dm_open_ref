## bound_y var (movable atom) 
###### BYOND Version 490" deprecated="516
**See also:**
*   [icon_z var (atom)](/ref/atom/var/icon_z.md) 
*   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
*   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
*   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) 
*   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
*   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
*   [locs list var (movable atom)](/ref/atom/movable/var/locs.md) 
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) <!-- -->
**Default value:**
*   0
Note* The bound_x/y vars have been deprecated in favor of icon_w/z and
pixel_w/z. It\'s now preferred to use bound_width/height alone to define
a bounding box. New behavior simply subtracts bound_x/y from pixel_w/z
to mimic the old usage. 

This var defines the bottom side of the
physical atom\'s bounding box, in pixels. By default all atoms are
assumed to be one tile in physical size. 

The bottom edge of the
bounding box starts bound_y pixels inward from the bottom edge of the
atom\'s icon (as affected by step_y). A bound_y value of 4 means the
atom has 4 pixels of empty space below it. 

Example* A 16×16
smiley face centered in a 32×32 icon should have a bound_y value of 8,
since there are 8 pixels of empty space below.