
## Bump (proc)

**Format:**
+   Bump(atom/Obstacle)

**Arguments:**
+   Obstacle: The blocking object.

**Called When:**
+   Called when a movement fails due to a dense blockage.

**Default Action:**
+   If the obstacle is a mob and src is in its group, swap their positions.
This is only done if the mobs both move by full tiles and do not use pixel
movement, to preserve the behavior of older games.
******
**Related Pages:**
+    [Move proc (movable atom)](/ref/atom/movable/proc/Move)
+    [Pixel movement](/ref/{notes}/pixel-movement)
