[]{#/atom/var/icon_z}    
## icon_z var (atom) {#icon_z-var-atom byondver="516"}    
**See also:**    
:   [icon_w var (atom)](/ref/atom/var/icon_w.md)    
:   [pixel_z var (atom)](/ref/atom/var/pixel_z.md)    
:   [icon var (atom)](/ref/atom/var/icon.md)    
<!-- -->    
**Default value:**    
:   0    
Defines the anchor point for this icon, from the bottom left. Higher    
values of icon_w will offset this icon downward; lower values offset it    
upward. It acts like a negative pixel_z except it\'s not inherited by    
any [overlays](/ref/atom/var/overlays.md), [images](/ref/image.md), or [visual    
contents](/ref/atom/var/vis_contents.md). It applies ONLY to this icon.    
This var is meant to replace the `bound_y` var, which was applied very    
inconsistently in old versions.  