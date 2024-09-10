[]{#/appearance var (atom).md}    
## appearance var (atom) {#appearance-var-atom byondver="508"}    
**See also:**    
:   [vars (atom)](/atom/var)    
:   [mutable appearance](/mutable_appearance)    
:   [Understanding the renderer](/%7Bnotes%7D/renderer)    
Every atom or image has an appearance, which controls all of the values    
relating to how it appears on the map. (The overlays and underlays lists    
are lists of appearances.) When read, this var provides a copy of the    
current appearance.    
This value can also be used to change an atom\'s appearance, altering    
multiple values at once. Setting atom.appearance to another appearance    
will change all of the following values to match:    
[alpha](/atom/var/alpha)    
[appearance_flags](/appearance var (atom).md_flags)    
[blend_mode](/atom/var/blend_mode)    
[color](/atom/var/color)    
[desc](/atom/var/desc)    
[gender](/atom/var/gender)    
[icon](/atom/var/icon)    
[icon_state](/atom/var/icon_state)    
[icon_w](/atom/var/icon_w)    
[icon_z](/atom/var/icon_z)    
[invisibility](/atom/var/invisibility)    
[infra_luminosity](/atom/var/infra_luminosity)    
[filters](/atom/var/filters)    
[layer](/atom/var/layer)    
[luminosity](/atom/var/luminosity)    
[maptext](/atom/var/maptext)    
[maptext_width](/atom/var/maptext_width),    
[maptext_height](/atom/var/maptext_height),    
[maptext_x](/atom/var/maptext_x), [maptext_y](/atom/var/maptext_y)    
[mouse_over_pointer](/atom/var/mouse_over_pointer),    
[mouse_drag_pointer](/atom/var/mouse_drag_pointer),    
[mouse_drop_pointer](/atom/var/mouse_drop_pointer)    
[mouse_drop_zone var](/atom/var/mouse_drop_zone)    
[mouse_opacity var](/atom/var/mouse_opacity)    
[name](/atom/var/name)    
[opacity](/atom/var/opacity)    
[overlays](/atom/var/overlays)    
[override](/atom/var/override) (images only)    
[pixel_x](/atom/var/pixel_x), [pixel_y](/atom/var/pixel_y),    
[pixel_w](/atom/var/pixel_w), [pixel_z](/atom/var/pixel_z)    
[plane](/atom/var/plane)    
[render_source](/atom/var/render_source),    
[render_target](/atom/var/render_target)    
[suffix](/atom/var/suffix)    
[text](/atom/var/text)    
[transform](/atom/var/transform)    
[underlays](/atom/var/underlays)    
[vis_flags](/atom/var/vis_flags)    
Other vars that are technically part of the appearance, but don\'t make    
any sense to change when cloning, are not changed. These include    
`density`, `dir`, `screen_loc`, and `verbs`. However, those vars ARE    
copied when you assign a `/mutable_appearance`.    
If you set `atom.appearance` to another atom, the other atom\'s    
appearance will be copied.  