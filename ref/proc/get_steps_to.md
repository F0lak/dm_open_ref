## get_steps_to proc 
###### BYOND Version 515

**Format:**
+   get_steps_to(Ref, Trg, Min=0)

**Returns:**
+   A list of directions to step.

**Args:**
+   Ref: Starting point or object.
+   Trg: An object on the map.
+   Min: The minimum distance between Ref and Trg before movement halts.

Calculate a set of steps from `Ref` on a path to `Trg`, taking
obstacles into account. The result of the proc is a list of directions
that can be used with `step()`, or null if a path could not be found.

If `Ref` is within `Min` steps of `Trg`, no steps are computed.
This is also true if the target is too far away (more than twice
`world.view` steps). In either case, null is returned.

> [!TIP] 
> **See also:**
> +   [step proc](/ref/proc/step.md) 
> +   [step_to proc](/ref/proc/step_to.md) 
> +   [walk_to proc](/ref/proc/walk_to.md) 
> +   [get_step_to proc](/ref/proc/get_step_to.md) 