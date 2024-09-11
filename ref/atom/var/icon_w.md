## icon_w var (atom) 
###### BYOND Version 516
**See also:**
*   [icon_z var (atom)](/atom/var/icon_z)
*   [pixel_w var (atom)](/atom/var/pixel_w)
*   [icon var (atom)](/atom/var/icon)
<!-- -->
**Default value:**
*   0


Defines the anchor point for this icon, from the bottom left.
Higher values of icon_w will offset this icon to the left; lower values
offset it to the right. It acts like a negative pixel_w except it\'s not
inherited by any [overlays](/atom/var/overlays), [images](/image), or
[visual contents](/atom/var/vis_contents). It applies ONLY to this
icon. 

This var is meant to replace the `bound_x` var, which was
applied very inconsistently in old versions.