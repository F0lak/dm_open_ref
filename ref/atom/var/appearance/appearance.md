[]{#/atom/var/appearance}    
## appearance var (atom) {#appearance-var-atom byondver="508"}    
**See also:**    
:   [vars (atom)](/ref/atom/var/var.md)    
:   [mutable appearance](/ref/mutable_appearance/mutable_appearance.md)    
:   [Understanding the renderer](/ref/%7Bnotes%7D/renderer/renderer.md)    
Every atom or image has an appearance, which controls all of the values    
relating to how it appears on the map. (The overlays and underlays lists    
are lists of appearances.) When read, this var provides a copy of the    
current appearance.    
This value can also be used to change an atom\'s appearance, altering    
multiple values at once. Setting atom.appearance to another appearance    
will change all of the following values to match:    
[alpha](/ref/atom/var/alpha/alpha.md)    
[appearance_flags](/ref/atom/var/appearance_flags/appearance_flags.md)    
[blend_mode](/ref/atom/var/blend_mode/blend_mode.md)    
[color](/ref/atom/var/color/color.md)    
[desc](/ref/atom/var/desc/desc.md)    
[gender](/ref/atom/var/gender/gender.md)    
[icon](/ref/atom/var/icon/icon.md)    
[icon_state](/ref/atom/var/icon_state/icon_state.md)    
[icon_w](/ref/atom/var/icon_w/icon_w.md)    
[icon_z](/ref/atom/var/icon_z/icon_z.md)    
[invisibility](/ref/atom/var/invisibility/invisibility.md)    
[infra_luminosity](/ref/atom/var/infra_luminosity/infra_luminosity.md)    
[filters](/ref/atom/var/filters/filters.md)    
[layer](/ref/atom/var/layer/layer.md)    
[luminosity](/ref/atom/var/luminosity/luminosity.md)    
[maptext](/ref/atom/var/maptext/maptext.md)    
[maptext_width](/ref/atom/var/maptext_width/maptext_width.md),    
[maptext_height](/ref/atom/var/maptext_height/maptext_height.md),    
[maptext_x](/ref/atom/var/maptext_x/maptext_x.md), [maptext_y](/ref/atom/var/maptext_y/maptext_y.md)    
[mouse_over_pointer](/ref/atom/var/mouse_over_pointer/mouse_over_pointer.md),    
[mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer/mouse_drag_pointer.md),    
[mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer/mouse_drop_pointer.md)    
[mouse_drop_zone var](/ref/atom/var/mouse_drop_zone/mouse_drop_zone.md)    
[mouse_opacity var](/ref/atom/var/mouse_opacity/mouse_opacity.md)    
[name](/ref/atom/var/name/name.md)    
[opacity](/ref/atom/var/opacity/opacity.md)    
[overlays](/ref/atom/var/overlays/overlays.md)    
[override](/ref/atom/var/override/override.md) (images only)    
[pixel_x](/ref/atom/var/pixel_x/pixel_x.md), [pixel_y](/ref/atom/var/pixel_y/pixel_y.md),    
[pixel_w](/ref/atom/var/pixel_w/pixel_w.md), [pixel_z](/ref/atom/var/pixel_z/pixel_z.md)    
[plane](/ref/atom/var/plane/plane.md)    
[render_source](/ref/atom/var/render_source/render_source.md),    
[render_target](/ref/atom/var/render_target/render_target.md)    
[suffix](/ref/atom/var/suffix/suffix.md)    
[text](/ref/atom/var/text/text.md)    
[transform](/ref/atom/var/transform/transform.md)    
[underlays](/ref/atom/var/underlays/underlays.md)    
[vis_flags](/ref/atom/var/vis_flags/vis_flags.md)    
Other vars that are technically part of the appearance, but don\'t make    
any sense to change when cloning, are not changed. These include    
`density`, `dir`, `screen_loc`, and `verbs`. However, those vars ARE    
copied when you assign a `/mutable_appearance`.    
If you set `atom.appearance` to another atom, the other atom\'s    
appearance will be copied.  