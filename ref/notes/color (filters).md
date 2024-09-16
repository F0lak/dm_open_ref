## Color matrix filter 
###### BYOND Version 513

<!-- -->
Format:
+   filter(type="color", ...)
<!-- -->
Args:
+   color: A color matrix
+   space: Value indicating color space: defaults to `FILTER_COLOR_RGB`


Applies a color matrix to this image. Unlike with the
atom.color var, you can apply color conversions other than the regular
RGBA color space, depending on the value of `space`. See [Color
space](/ref/appendix/color-space.md) for more information.

> [!TIP] 
> **See also:**
> +   [color var (atom)](/ref/atom/var/color.md) 
> +   [Color matrix](/ref/notes/color-matrix.md) 
> +   [Color space](/ref/appendix/color-space.md) 