
## glide_size (var)

**Default Value:**
+   0
***
Note: The way this setting is used depends on <a href="#/world/var/movement_mode">world.movement_mode</a>. See <a href="#/{notes}/gliding">Gliding</a> for more details.

This controls the number of pixels the map is moved in each step during scrolling of the map. The default value of 0 chooses automated control over this value, which generally results in a minimum step of 4 pixels that is increased when necessary to keep up with motion of the map.

Be careful about using small step sizes. Icons with high contrast pixel-level detail can look pretty ugly when displaced by short distances.

This was renamed from `pixel_step_size`.
***
**Related Pages:**
+    [eye var (client)](/ref/client/var/eye)
+    [glide_size var (movable atom)](/ref/atom/movable/var/glide_size)
