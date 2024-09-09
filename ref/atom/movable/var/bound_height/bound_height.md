[]{#/atom/movable/var/bound_height}    
## bound_height var (movable atom) {#bound_height-var-movable-atom byondver="490"}    
**See also:**    
:   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x/bound_x.md)    
:   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y/bound_y.md)    
:   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width/bound_width.md)    
:   [icon_w var (atom)](/ref/atom/var/icon_w/icon_w.md)    
:   [icon_z var (atom)](/ref/atom/var/icon_z/icon_z.md)    
:   [step_x var (movable atom)](/ref/atom/movable/var/step_x/step_x.md)    
:   [step_y var (movable atom)](/ref/atom/movable/var/step_y/step_y.md)    
:   [locs list var (movable atom)](/ref/atom/movable/var/locs/locs.md)    
:   [icon_size var (world)](/ref/world/var/icon_size/icon_size.md)    
:   [map_format var (world)](/ref/world/var/map_format/map_format.md)    
:   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement/pixel-movement.md)    
<!-- -->    
**Default value:**    
:   32 (depends on world.icon_size)    
This var defines the height of the physical atom\'s bounding box, in    
pixels. By default all atoms are assumed to be one tile in physical    
size.    
Example: A 16×16 smiley face centered in a 32×32 icon should have a    
bound_height value of 16.    
The default value depends on world.icon_size and world.map_format. In a    
topdown or tiled map_format, the icon height specified in    
world.icon_size is used. In other modes, height is irrelevant and tile    
\"footprints\" are square, so the icon width is used.  