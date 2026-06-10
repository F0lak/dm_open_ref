
## step (proc)

**Format:**
+   step(Ref,Dir,Speed=0)
+   step(Ref,Vector)

**Arguments:**
+   Ref: A mob or obj.
+   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST, SOUTHEAST,
     SOUTHWEST.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.
+   Vector: A 2D vector to move by, in pixels.

**Returns:**
+   1 on success; 0 otherwise
***
Move Ref in the direction Dir.

The vector version of this proc takes a 2D vector and tries to move by that amount of pixels.
***
**Related Pages:**
+    [get_step proc](/ref/proc/get_step)
+    [walk proc](/ref/proc/walk)
+    [step_size var (movable atom)](/ref/atom/movable/var/step_size)
+    [vector](/ref/vector)
