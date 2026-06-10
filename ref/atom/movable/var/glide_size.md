
## glide_size (var)

**Default Value:**
+   0
***
Note: The way this setting is used depends on <a href="#/world/var/movement_mode">world.movement_mode</a>. See <a href="#/{notes}/gliding">Gliding</a> for more details.

This controls the number of pixels an object is moved in each footstep during animated movement. The default value of 0 chooses automated control over this value, which generally results in a minimum footstep of 4 pixels that is increased when necessary to keep up with motion on the turf grid.

Decimal values are allowed.

Be careful about using small glide sizes. Icons with high contrast pixel-level detail can look pretty ugly when displaced by short distances.

The glide size is measured in server ticks. If you use a different client tick rate by altering <code>client.fps</code> or <code>client.tick_lag</code>, the actual glide used will be scaled appropriately. E.g., if your <code>client.fps</code> is 4 times greater than <code>world.fps</code>, the actual glide amount each client tick will be <code>glide_size/4</code>.

This was renamed from `pixel_step_size`.
***
**Related Pages:**
+    [animate_movement var (movable atom)](/ref/atom/movable/var/animate_movement)
+    [glide_size var (client)](/ref/client/var/glide_size)
+    [pixel_x](/ref/atom/var/pixel_x)
+    [pixel_y](/ref/atom/var/pixel_y)
+    [icon_size var (world)](/ref/world/var/icon_size)
+    [movement_mode var (world)](/ref/world/var/movement_mode)
+    [fps var (client)](/ref/client/var/fps)
+    [Gliding](/ref/{notes}/gliding)
