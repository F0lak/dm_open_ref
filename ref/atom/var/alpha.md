## alpha var (atom) 
###### BYOND Version 500
**See also:**
*   [vars (atom)](/ref/atom/var.md) -m
*   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) -m
*   [blend_mode var (atom)](/ref/atom/var/blend_mode.md) -m
*   [color var (atom)](/ref/atom/var/color.md) -m<!-- -->
**Default value:**
*   255 (opaque)
<!-- -->
**Possible values:**
*   0 (transparent) through 255 (opaque)


Controls the opacity of the icon displayed on players\'
screens. A value of 128 means the atom is half-transparent, so it will
have a ghostly appearance. This can be used to fade an atom in and out,
especially when combined with animation. Alpha is also applied to
maptext. 

Overlays and images will also be affected by alpha,
unless they use the RESET_ALPHA value in appearance_flags.