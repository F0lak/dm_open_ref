
## step_away (proc)

**Format:**
+   step_away(Ref,Trg,Max=5,Speed=0)

**Arguments:**
+   Ref: A mob or obj.
+   Trg: An object on the map.
+   Max: The maximum distance between Ref and Targ before movement halts.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.

**Returns:**
+   1 on success; 0 otherwise.
***
Move Ref on a path away from location Trg, taking obstacles into account. If Ref is farther than Max steps from Trg, no action will be taken.
***
**Related Pages:**
+    [get_step_away proc](/ref/proc/get_step_away)
+    [walk_away proc](/ref/proc/walk_away)
+    [step_size var (movable atom)](/ref/atom/movable/var/step_size)
