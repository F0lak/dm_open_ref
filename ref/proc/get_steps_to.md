
## get_steps_to (proc)

**Format:**
+   get_steps_to(Ref, Trg, Min=0)

**Arguments:**
+   Ref: Starting point or object.
+   Trg: An object on the map.
+   Min: The minimum distance between Ref and Trg before movement halts.

**Returns:**
+   A list of directions to step.
***
Calculate a set of steps from `Ref` on a path to `Trg`, taking obstacles into account. The result of the proc is a list of directions that can be used with `step()`, or null if a path could not be found.

If `Ref` is within `Min` steps of `Trg`, no steps are computed. This is also true if the target is too far away (more than twice `world.view` steps). In either case, null is returned.
***
**Related Pages:**
+    [step proc](/ref/proc/step)
+    [step_to proc](/ref/proc/step_to)
+    [walk_to proc](/ref/proc/walk_to)
+    [get_step_to proc](/ref/proc/get_step_to)
