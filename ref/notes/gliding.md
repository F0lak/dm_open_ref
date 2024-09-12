## Gliding

    atom)](/ref/atom/movable/var/animate_movement.md) 
+   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 
+   [glide_size var (movable atom)](/ref/atom/movable/var/glide_size.md) 
+   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
+   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y.md) 
+   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
+   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) 
+   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 
+   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
+   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
+   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
+   [fps var (client)](/ref/client/var/fps.md) 


Gliding is a \"glitz\" effect applied by BYOND to cover up the
visual sins of tile-based movement, by making objects and the map appear
to move smoothly from one tile to another instead of immediately
jumping. It is also available to smooth over small jumps in pixel
movement that might occur, for instance if the client FPS is set higher
than the server\'s. 

To control the gliding speed of an atom,
set `glide_size` to the value of your choice. If this is not set, the
client will attempt to adjust the speed manually. `glide_size` is
measured in server ticks, so if `client.fps` is set to a value greater
than `world.fps`, it will be scaled appropriately. 

Whether an
object glides or jumps is based on how far it moves relative to its
`step_size` value, which by default is a full tile width. If the
movement goes too far past `step_size` in the X or Y directions, it\'s
no longer a glide. 

The `animate_movement` var can be used to
control the way in which an object glides, or suppress gliding
altogether. 

By using the `LONG_GLIDE` flag in
`appearance_flags`, a diagonal glide will take just as long as a
cardinal-direction glide by moving a fullt `glide_size` pixels in the
dominant X or Y direction. Otherwise, gliding tries to move by that many
pixels in strict Euclidean distance (a straight line) and diagonal
glides take longer. 
> [!NOTE]
> In
[LEGACY_MOVEMENT_MODE](/ref/world/var/movement_mode.md), gliding is
turned off if you set any of the bound or step vars for an atom to a
non-default value. The only gliding that occurs in this case is when
client.fps is higher than world.fps. All other movement modes base
gliding on an atom\'s `glide_size` value.

**See also:**
+   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) 
+   [animate_movement var (movable