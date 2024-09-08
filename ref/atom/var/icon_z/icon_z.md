[]{#/atom/var/icon_z}
## icon_z var (atom) {#icon_z-var-atom byondver="516"}
**See also:**
:   [icon_w var (atom)](#/atom/var/icon_w)
:   [pixel_z var (atom)](#/atom/var/pixel_z)
:   [icon var (atom)](#/atom/var/icon)
<!-- -->
**Default value:**
:   0
Defines the anchor point for this icon, from the bottom left. Higher
values of icon_w will offset this icon downward; lower values offset it
upward. It acts like a negative pixel_z except it\'s not inherited by
any [overlays](#/atom/var/overlays), [images](#/image), or [visual
contents](#/atom/var/vis_contents). It applies ONLY to this icon.
This var is meant to replace the `bound_y` var, which was applied very
inconsistently in old versions.