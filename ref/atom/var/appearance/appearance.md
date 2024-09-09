[]{#/atom/var/appearance}
  ## appearance var (atom) {#appearance-var-atom byondver="508"}
  **See also:**
  :   [vars (atom)](ref/atom/var)
  :   [mutable appearance](ref/mutable_appearance)
  :   [Understanding the renderer](ref/%7Bnotes%7D/renderer)
  Every atom or image has an appearance, which controls all of the values
  relating to how it appears on the map. (The overlays and underlays lists
  are lists of appearances.) When read, this var provides a copy of the
  current appearance.
  This value can also be used to change an atom\'s appearance, altering
  multiple values at once. Setting atom.appearance to another appearance
  will change all of the following values to match:
  [alpha](ref/atom/var/alpha)
  [appearance_flags](ref/atom/var/appearance_flags)
  [blend_mode](ref/atom/var/blend_mode)
  [color](ref/atom/var/color)
  [desc](ref/atom/var/desc)
  [gender](ref/atom/var/gender)
  [icon](ref/atom/var/icon)
  [icon_state](ref/atom/var/icon_state)
  [icon_w](ref/atom/var/icon_w)
  [icon_z](ref/atom/var/icon_z)
  [invisibility](ref/atom/var/invisibility)
  [infra_luminosity](ref/atom/var/infra_luminosity)
  [filters](ref/atom/var/filters)
  [layer](ref/atom/var/layer)
  [luminosity](ref/atom/var/luminosity)
  [maptext](ref/atom/var/maptext)
  [maptext_width](ref/atom/var/maptext_width),
  [maptext_height](ref/atom/var/maptext_height),
  [maptext_x](ref/atom/var/maptext_x), [maptext_y](ref/atom/var/maptext_y)
  [mouse_over_pointer](ref/atom/var/mouse_over_pointer),
  [mouse_drag_pointer](ref/atom/var/mouse_drag_pointer),
  [mouse_drop_pointer](ref/atom/var/mouse_drop_pointer)
  [mouse_drop_zone var](ref/atom/var/mouse_drop_zone)
  [mouse_opacity var](ref/atom/var/mouse_opacity)
  [name](ref/atom/var/name)
  [opacity](ref/atom/var/opacity)
  [overlays](ref/atom/var/overlays)
  [override](ref/atom/var/override) (images only)
  [pixel_x](ref/atom/var/pixel_x), [pixel_y](ref/atom/var/pixel_y),
  [pixel_w](ref/atom/var/pixel_w), [pixel_z](ref/atom/var/pixel_z)
  [plane](ref/atom/var/plane)
  [render_source](ref/atom/var/render_source),
  [render_target](ref/atom/var/render_target)
  [suffix](ref/atom/var/suffix)
  [text](ref/atom/var/text)
  [transform](ref/atom/var/transform)
  [underlays](ref/atom/var/underlays)
  [vis_flags](ref/atom/var/vis_flags)
  Other vars that are technically part of the appearance, but don\'t make
  any sense to change when cloning, are not changed. These include
  `density`, `dir`, `screen_loc`, and `verbs`. However, those vars ARE
  copied when you assign a `/mutable_appearance`.
  If you set `atom.appearance` to another atom, the other atom\'s
  appearance will be copied.