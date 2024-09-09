[]{#/{notes}/topdown toc="Topdown maps"}
  ## Topdown maps
  **See also:**
  :   [map_format var (world)](ref/world/var/map_format)
  :   [icon_size var (world)](ref/world/var/icon_size)
  :   [dir var (client)](ref/client/var/dir)
  :   [layer var (atom)](ref/atom/var/layer)
  :   [plane var (atom)](ref/atom/var/plane)
  :   [screen_loc var (movable atoms)](ref/atom/movable/var/screen_loc)
  :   [Big icons](ref/%7Bnotes%7D/big-icons)
  :   [HUD](ref/%7Bnotes%7D/HUD)
  :   [Isometric maps](ref/%7Bnotes%7D/isometric)
  :   [Side-view maps](ref/%7Bnotes%7D/side)
  :   [Understanding the renderer](ref/%7Bnotes%7D/renderer)
  By default, BYOND displays all maps in top-down format, so
  `world.map_format` is set to `TOPDOWN_MAP` unless you say otherwise.
  This view means players are looking down on the map, and \"north\"
  corresponds to the top of their screen. (This can be changed by setting
  `client.dir`.)
  A related map_format, used by older games, is `TILED_ICON_MAP`. This is
  also topdown but it handles icons differently.
  In this form, the `layer` var behaves exactly as you would expect: Icons
  with a lower layer are drawn beneath icons with a higher layer. The only
  exception is when you use [big icons](ref/%7Bnotes%7D/big-icons), which
  will be drawn above any other icons on the same layer. Also an atom\'s
  underlays will be drawn behind it unless their layer is changed, and its
  overlays will draw in front of it unless otherwise stated.
  Topdown mode also guarantees that `world.view` or `client.view` will set
  the exact screen size used by the HUD, except for HUD objects that
  appear outside of the normal bounds.
  Screen objects (also called the HUD) cannot be intermixed with topdown
  icons. They will appear on top of other icons, unless using a lower
  plane or a special layer like `BACKGROUND_LAYER`.