## Gliding    
**See also:**    
:   [Pixel movement](/%7Bnotes%7D/pixel-movement)    
:   [animate_movement var (movable    
    atom)](/atom/movable/var/animate_movement)    
:   [appearance_flags var (atom)](/atom/var/appearance_flags)    
:   [glide_size var (movable atom)](/atom/movable/var/glide_size)    
:   [bound_x var (movable atom)](/atom/movable/var/bound_x)    
:   [bound_y var (movable atom)](/atom/movable/var/bound_y)    
:   [bound_width var (movable atom)](/atom/movable/var/bound_width)    
:   [bound_height var (movable atom)](/atom/movable/var/bound_height)    
:   [step_size var (movable atom)](/atom/movable/var/step_size)    
:   [step_x var (movable atom)](/atom/movable/var/step_x)    
:   [step_y var (movable atom)](/atom/movable/var/step_y)    
:   [movement_mode var (world)](/world/var/movement_mode)    
:   [fps var (client)](/client/var/fps)    
Gliding is a \"glitz\" effect applied by BYOND to cover up the visual    
sins of tile-based movement, by making objects and the map appear to    
move smoothly from one tile to another instead of immediately jumping.    
It is also available to smooth over small jumps in pixel movement that    
might occur, for instance if the client FPS is set higher than the    
server\'s.    
To control the gliding speed of an atom, set `glide_size` to the value    
of your choice. If this is not set, the client will attempt to adjust    
the speed manually. `glide_size` is measured in server ticks, so if    
`client.fps` is set to a value greater than `world.fps`, it will be    
scaled appropriately.    
Whether an object glides or jumps is based on how far it moves relative    
to its `step_size` value, which by default is a full tile width. If the    
movement goes too far past `step_size` in the X or Y directions, it\'s    
no longer a glide.    
The `animate_movement` var can be used to control the way in which an    
object glides, or suppress gliding altogether.    
By using the `LONG_GLIDE` flag in `appearance_flags`, a diagonal glide    
will take just as long as a cardinal-direction glide by moving a fullt    
`glide_size` pixels in the dominant X or Y direction. Otherwise, gliding    
tries to move by that many pixels in strict Euclidean distance (a    
straight line) and diagonal glides take longer.    
In [LEGACY_MOVEMENT_MODE](/world/var/movement_mode){.code}, gliding is    
turned off if you set any of the bound or step vars for an atom to a    
non-default value. The only gliding that occurs in this case is when    
client.fps is higher than world.fps. All other movement modes base    
gliding on an atom\'s `glide_size` value.  