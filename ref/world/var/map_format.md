
## map_format (var)
***
This value says how the world will display maps. In a normal overhead tiled map the value is `TOPDOWN_MAP` for the top-down format. For older games that predate this feature, the value is `TILED_ICON_MAP`.

If you use a map format other than top-down, the HUD will still use a tile format like it would in top-down display. HUD objects are not projected into whatever map_format you use and they are not affected by changing client.dir. The size of the HUD is rounded up to the nearest number of full screen tiles; the size of each tile is defined by world.icon_size.
***