## step_rand proc

**Format:**
+   step_rand(Ref,Speed=0)

**Returns:**
+   1 on success; 0 otherwise.

**Args:**
+   Ref: A mob or obj.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.


Move Ref randomly.

> [!TIP] 
> **See also:**
> +   [get_step_rand proc](/ref/proc/get_step_rand.md) 
> +   [walk_rand proc](/ref/proc/walk_rand.md) 
> +   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 