
## step_size (var)

**Default Value:**
+   32 (width of default icon; depends on world.icon_size)
***
This var defines how fast, in pixels, an atom will move by default. If you use lower values of `step_size` for most items in your world, you may want to consider raising `world.fps` (at higher performance cost).

When `Move()` is called by a step or walk, or by the built-in client movement verbs, a change of `step_size` is applied to `step_x` and/or `step_y`. Any movement within the speed of `step_size`, or up to one tile in distance (whichever is greater), is considered a slide and may partially succeed if an obstacle is bumped before reaching the final position.
***
**Related Pages:**
+    [step_x var (movable atom)](/ref/atom/movable/var/step_x)
+    [step_y var (movable atom)](/ref/atom/movable/var/step_y)
+    [Move proc (movable atom)](/ref/atom/movable/proc/Move)
+    [locs list var (movable atom)](/ref/atom/movable/var/locs)
+    [fps var (world)](/ref/world/var/fps)
+    [icon_size var (world)](/ref/world/var/icon_size)
+    [Gliding](/ref/{notes}/gliding)
+    [Pixel movement](/ref/{notes}/pixel-movement)
