## bounds_dist proc

**Format:**
+   bounds_dist(Ref, Target)

**Returns:**
+   The distance, in pixels, between Ref\'s and Target\'s bounding
    boxes.

**Args:**
+   **Ref**: A turf, obj, or mob.
+   **Target**: A turf, obj, or mob.

The value returned by bounds_dist() is the number of pixels
that the two objects would have to move closer together (if this is even
possible, of course) to be touching but not overlapping. 

A return value of 12 for instance means the two objects have a gap of 12
pixels between them. 

A return value of 0 means the two objects
are not overlapping, but their bounding boxes touch. 

A return value of -2 means the two objects are overlapping by 2 pixels;
they would have to move 2 pixels apart to separate.

> [!TIP] 
> **See also:**
> +   [bound_x var (movable atom)](/ref/atom/movable/var/bound_x.md) 
> +   [bound_y var (movable atom)](/ref/atom/movable/var/bound_y.md) 
> +   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
> +   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) 
> +   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
> +   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) 
> +   [bounds proc](/ref/proc/bounds.md) 
> +   [Pixel movement](/ref/notes/pixel-movement.md) 