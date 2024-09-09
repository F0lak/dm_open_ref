[]{#/atom/var/blend_mode}    
## blend_mode var (atom) {#blend_mode-var-atom byondver="501"}    
**See also:**    
:   [vars (atom)](/ref/atom/var.md)    
:   [alpha var (atom)](/ref/atom/var/alpha.md)    
:   [color var (atom)](/ref/atom/var/color.md)    
:   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md)    
<!-- -->    
**Default value:**    
:   0 (none/overlay)    
<!-- -->    
**Possible values:**    
:   BLEND_DEFAULT (0)    
:   BLEND_OVERLAY    
:   BLEND_ADD    
:   BLEND_SUBTRACT[\*]{.small}    
:   BLEND_MULTIPLY[\*†]{.small}    
:   BLEND_INSET_OVERLAY[\*†]{.small}    
\[[\*]{.small} This blend type appears only when using graphics hardware    
mode. It is also not visible in the map editor.\]\    
\[[†]{.small} Since the alpha of the icon underneath is used for alpha    
masking, mouse hits take it into account.\]    
Controls the way the atom\'s icon is blended onto the icons behind it.    
The blend mode used by an atom is inherited by any attached overlays,    
unless they override it. `BLEND_DEFAULT` will use the main atom\'s blend    
mode; for the atom itself, it\'s the same as `BLEND_OVERLAY`.    
`BLEND_OVERLAY` will draw an icon the normal way.    
`BLEND_ADD` will do additive blending, so that the colors in the icon    
are added to whatever is behind it. Light effects like explosions will    
tend to look better in this mode.    
`BLEND_SUBTRACT` is for subtractive blending. This may be useful for    
special effects.    
`BLEND_MULTIPLY` will multiply the icon\'s colors by whatever is behind    
it. This is typically only useful for applying a colored light effect;    
for simply darkening, using a translucent black icon with normal overlay    
blending is a better option.    
`BLEND_INSET_OVERLAY` overlays the icon, but masks it by the image being    
drawn on. This is pretty much not at all useful directly on the map, but    
can be very useful for an overlay for an atom that uses `KEEP_TOGETHER`    
(see [appearance_flags](/ref/atom/var/appearance_flags.md){.code}), or for the    
[layering filter](/ref/%7Bnotes%7D/filters/layer.md).  