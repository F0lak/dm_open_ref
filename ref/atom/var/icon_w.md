## icon_w var (atom) 
###### BYOND Version 516


**Default value:**
+   0


Defines the anchor point for this icon, from the bottom left.
Higher values of icon_w will offset this icon to the left; lower values
offset it to the right. It acts like a negative pixel_w except it\'s not
inherited by any [overlays](/ref/atom/var/overlays.md) , [images](/ref/image.md) , or
[visual contents](/ref/atom/var/vis_contents.md)  It applies ONLY to this
icon. 

This var is meant to replace the `bound_x` var, which was
applied very inconsistently in old versions.

> [!TIP] 
> **See also:**
> +   [icon_z var (atom)](/ref/atom/var/icon_z.md) 
> +   [pixel_w var (atom)](/ref/atom/var/pixel_w.md) 
> +   [icon var (atom)](/ref/atom/var/icon.md) 