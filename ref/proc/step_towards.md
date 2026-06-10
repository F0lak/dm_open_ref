
## step_towards (proc)

**Format:**
+   step_towards(Ref,Trg,Speed)

**Arguments:**
+   Ref: A mob or obj.
+   Trg: An object on the map.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.

**Returns:**
+   1 on success; 0 otherwise.
***
Move Ref in the direction of the location Trg.
***
**Related Pages:**
+    [get_step_towards proc](/ref/proc/get_step_towards)
+    [walk_towards proc](/ref/proc/walk_towards)
+    [step_size var (movable atom)](/ref/atom/movable/var/step_size)
