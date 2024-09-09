[]{#/atom/var/maptext_height}
  ## maptext_height var (atom) {#maptext_height-var-atom byondver="494"}
  **See also:**
  :   [maptext var (atom)](ref/atom/var/maptext)
  :   [maptext_width var (atom)](ref/atom/var/maptext_width)
  :   [maptext_x var (atom)](ref/atom/var/maptext_x)
  :   [maptext_y var (atom)](ref/atom/var/maptext_y)
  :   [icon_size var (world)](ref/world/var/icon_size)
  :   [map_format var (world)](ref/world/var/map_format)
  <!-- -->
  **Default value:**
  :   32 (depends on world.icon_size)
  This is the height of the text shown in the maptext var. The default
  value depends on world.icon_size and world.map_format. In a topdown
  (default) or tiled map_format, the icon height is used. In other map
  views, tile \"footprints\" are square and height is irrelevant, so the
  default will be the icon width instead.)