## step proc

**Format:**
+   step(Ref,Dir,Speed=0)

**Returns:**
+   1 on success; 0 otherwise

**Args:**
+   Ref: A mob or obj.
+   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST,
    SOUTHEAST, SOUTHWEST.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.

Move Ref in the direction Dir.

> [!TIP] 
> **See also:**
> +   [get_step proc](/ref/proc/get_step.md) 
> +   [walk proc](/ref/proc/walk.md) 
> +   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 