## step_towards proc

**Format:**
+   step_towards(Ref,Trg,Speed)

**Returns:**
+   1 on success; 0 otherwise.

**Args:**
+   Ref: A mob or obj.
+   Trg: An object on the map.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.


Move Ref in the direction of the location Trg.

> [!TIP] 
> **See also:**
> +   [get_step_towards proc](/ref/proc/get_step_towards.md) 
> +   [walk_towards proc](/ref/proc/walk_towards.md) 
> +   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) 