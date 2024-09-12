## glide_size var (movable atoms) 
###### BYOND Version 490
**See also:**
*   [animate_movement var (movable
    atoms)](/ref/atom/movable/var/animate_movement.md) 
*   [glide_size var (client)](/ref/client/var/glide_size.md) 
*   [pixel_x var (atom)](/ref/atom/var/pixel_x.md) 
*   [pixel_y var (atom)](/ref/atom/var/pixel_y.md) 
*   [icon_size var (world)](/ref/world/var/icon_size.md) 
*   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
*   [fps var (client)](/ref/client/var/fps.md) 
*   [Gliding](/ref/%7Bnotes%7D/gliding.md) 
<!-- -->
**Default value:**
*   0


Note* The way this setting is used depends on
[world.movement_mode](/ref/world/var/movement_mode.md) . See
[Gliding](/ref/%7Bnotes%7D/gliding.md) for more details. 

This
controls the number of pixels an object is moved in each footstep during
animated movement. The default value of 0 chooses automated control over
this value, which generally results in a minimum footstep of 4 pixels
that is increased when necessary to keep up with motion on the turf
grid. 

Decimal values are allowed. 

Be careful about
using small glide sizes. Icons with high contrast pixel-level detail can
look pretty ugly when displaced by short distances. 

The glide
size is measured in server ticks. If you use a different client tick
rate by altering `client.fps` or `client.tick_lag`, the actual glide
used will be scaled appropriately. E.g., if your `client.fps` is 4 times
greater than `world.fps`, the actual glide amount each client tick will
be `glide_size/4`. 

This was renamed from `pixel_step_size`.