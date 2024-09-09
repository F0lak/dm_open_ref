[]{#/atom/var/icon_w}    
## icon_w var (atom) {#icon_w-var-atom byondver="516"}    
**See also:**    
:   [icon_z var (atom)](/ref/atom/var/icon_z/icon_z.md)    
:   [pixel_w var (atom)](/ref/atom/var/pixel_w/pixel_w.md)    
:   [icon var (atom)](/ref/atom/var/icon/icon.md)    
<!-- -->    
**Default value:**    
:   0    
Defines the anchor point for this icon, from the bottom left. Higher    
values of icon_w will offset this icon to the left; lower values offset    
it to the right. It acts like a negative pixel_w except it\'s not    
inherited by any [overlays](/ref/atom/var/overlays/overlays.md), [images](/ref/image/image.md), or    
[visual contents](/ref/atom/var/vis_contents/vis_contents.md). It applies ONLY to this    
icon.    
This var is meant to replace the `bound_x` var, which was applied very    
inconsistently in old versions.  