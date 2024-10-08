## Motion blur filter 
###### BYOND Version 512


Format:
+   filter(type="motion_blur", ...)

Args:
+   x: Blur vector on the X axis (defaults to 0)
+   y: Blur vector on the Y axis (defaults to 0)


Applies Gaussian blur in one direction only. The amount and
direction are both specified by `x` and `y`. The size of the blur is
equal to `sqrt(x*x + y*y)`. 

See [Gaussian blur](/ref/notes/filters/blur.md) for more information.

> [!TIP] 
> **See also:**
> +   [filters var (atom)](/ref/atom/var/filters.md) 
> +   [Gaussian blur (filters)](/ref/notes/filters/blur.md) 