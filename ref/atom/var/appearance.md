## appearance var (atom) 
###### BYOND Version 508
**See also:**
*   [vars (atom)](/ref/atom/var.md) -m
*   [mutable appearance](/ref/mutable_appearance.md) -m
*   [Understanding the renderer](/ref/%7Bnotes%7D/renderer.md) -m


Every atom or image has an appearance, which controls all of
the values relating to how it appears on the map. (The overlays and
underlays lists are lists of appearances.) When read, this var provides
a copy of the current appearance. 

This value can also be used
to change an atom\'s appearance, altering multiple values at once.
Setting atom.appearance to another appearance will change all of the
following values to match:
[alpha](/ref/atom/var/alpha.md) -m
[appearance_flags](/ref/atom/var/appearance_flags.md) -m
[blend_mode](/ref/atom/var/blend_mode.md) -m
[color](/ref/atom/var/color.md) -m
[desc](/ref/atom/var/desc.md) -m
[gender](/ref/atom/var/gender.md) -m
[icon](/ref/atom/var/icon.md) -m
[icon_state](/ref/atom/var/icon_state.md) -m
[icon_w](/ref/atom/var/icon_w.md) -m
[icon_z](/ref/atom/var/icon_z.md) -m
[invisibility](/ref/atom/var/invisibility.md) -m
[infra_luminosity](/ref/atom/var/infra_luminosity.md) -m
[filters](/ref/atom/var/filters.md) -m
[layer](/ref/atom/var/layer.md) -m
[luminosity](/ref/atom/var/luminosity.md) -m
[maptext](/ref/atom/var/maptext.md) -m
[maptext_width](/ref/atom/var/maptext_width.md) -m,
[maptext_height](/ref/atom/var/maptext_height.md) -m,
[maptext_x](/ref/atom/var/maptext_x.md) -m, [maptext_y](/ref/atom/var/maptext_y.md) -m
[mouse_over_pointer](/ref/atom/var/mouse_over_pointer.md) -m,
[mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer.md) -m,
[mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer.md) -m
[mouse_drop_zone var](/ref/atom/var/mouse_drop_zone.md) -m
[mouse_opacity var](/ref/atom/var/mouse_opacity.md) -m
[name](/ref/atom/var/name.md) -m
[opacity](/ref/atom/var/opacity.md) -m
[overlays](/ref/atom/var/overlays.md) -m
[override](/ref/atom/var/override.md) -m (images only)
[pixel_x](/ref/atom/var/pixel_x.md) -m, [pixel_y](/ref/atom/var/pixel_y.md) -m,
[pixel_w](/ref/atom/var/pixel_w.md) -m, [pixel_z](/ref/atom/var/pixel_z.md) -m
[plane](/ref/atom/var/plane.md) -m
[render_source](/ref/atom/var/render_source.md) -m,
[render_target](/ref/atom/var/render_target.md) -m
[suffix](/ref/atom/var/suffix.md) -m
[text](/ref/atom/var/text.md) -m
[transform](/ref/atom/var/transform.md) -m
[underlays](/ref/atom/var/underlays.md) -m
[vis_flags](/ref/atom/var/vis_flags.md) -m

Other vars that are technically part of the appearance, but
don\'t make any sense to change when cloning, are not changed. These
include `density`, `dir`, `screen_loc`, and `verbs`. However, those vars
ARE copied when you assign a `/mutable_appearance`. 

If you set
`atom.appearance` to another atom, the other atom\'s appearance will be
copied.