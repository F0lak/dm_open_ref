# map_format var (world)

**Default value:**
+   TOPDOWN_MAP

**Possible values:**
-   TOPDOWN_MAP
-   ISOMETRIC_MAP
-   SIDE_MAP
-   TILED_ICON_MAP

This value says how the world will display maps. In a normal
overhead tiled map the value is `TOPDOWN_MAP` for the top-down format.
For older games that predate this feature, the value is
`TILED_ICON_MAP`. 
If you use a map format other than top-down,
the HUD will still use a tile format like it would in top-down display.
HUD objects are not projected into whatever map_format you use and they
are not affected by changing client.dir. The size of the HUD is rounded
up to the nearest number of full screen tiles; the size of each tile is
defined by world.icon_size.

### Top-down format
(See more at [Topdown maps](/ref/notes/topdown.md) .) 
This is the default map format. Icons are drawn in a tile form and viewed from
overhead. In this layout, the layer assigned to each atom is very
important. The number of tiles shown is set by client.view or
world.view. 
Because this format is familiar and easy to
understand, it is the default setting. Most of the vars related to maps
and atoms are designed and documented with this format in mind.

### Tiled icon format {#tiled-icon-format deprecated="1"}
(See more at [Tiled icons](/ref/notes/tiled-icons.md) .) In BYOND 4.0 a
new feature was introduced for using \"big\" icons, bigger than the
standard tile size, by splitting them up into states like \"0,0\",
\"1,0\", and so on. This functionality is no longer needed since BYOND
now has the ability to display icons in their natural size. Some games
that were designed before this, however, may still need to make use of
this splitting feature that breaks icons into smaller tile-sized pieces.
When an icon is broken into chunks, each state in the icon is given a
thumbail version of the full image, and then new states are added to
show each chunk. For instance if world.icon_size is the default 32×32,
and the icon is 64×64, then the \"door\" state would become a thumbnail
of the full door image while \"door 0,0\" (the lower left corner),
\"door 1,0\", \"door 0,1\", and \"door 1,1\" were created to show each
smaller section of the image. If the default \"\" state is broken into
chunks, those chunks are just named \"0,0\" and so on without a space.
This format is deprecated. It exists to support older games and allow
them to be compiled without causing them to break, until they can be
redesigned for one of the newer formats.

### Isometric format
(See more at [Isometric maps](/ref/notes/isometric.md) .) 
If map_format is set to `ISOMETRIC_MAP`, the map is displayed in isometric
form. Isometric tiles are displayed in a foreshortened diagonal
perspective, where the \"north\" direction actually displays as
northeast on the player\'s screen, and \"east\" shows up as southeast.
The value of `client.view` or `world.view` is used to calculate the
*minimum* number of tiles to display, and extra tiles to each side will
be shown to fill in the corners. 
In an isometric map, the tile
width set in world.icon_size is the most important factor. This should
be a multiple of 4 for best results. The minimum tile height is half
that value, and any extra height is used to show vertical structures
that \"stick up\" off the map surface. When you draw an isometric tile
icon, start with a flattened diamond shape at the bottom that is only
half as high as it is wide. 
Isometric maps behave differently
during drawing than top-down maps. In isometric, tiles that are nearer
to the viewer\'s perspective are drawn in front of tiles farther back,
regardless of layer. Layers only count within an individual tile. This
means that if you want to have a vertical structure \"stick up\" to
partially hide something behind it, the icon sticking up should always
be on a tile forward from the one being partly covered. E.g. if you have
a wall taking up part of your tile, it needs to be at the \"back\" end
of the tile to properly hide anything on the tiles behind it.
The `pixel_x` and `pixel_y` values, `step_x` and `step_y`
values, and the gliding that happens when moving between tiles, are
based on the width set by `world.icon_size`. If you set
`world.icon_size="64x128"` to show tall buildings, only the 64 matters
for pixel offsets. Use `pixel_w` and `pixel_z` to adjust the position of
atoms (or the client) horizontally or vertically without respect to
`client.dir` or the map format. 
Note: Offsets for x and y also
affect the layering order used to draw the icons. Any object with a
pixel offset onto another tile is considered part of whichever tile is
closer. 
If you use an icon wider than one tile, the
\"footprint\" of the isometric icon (the actual map tiles it takes up)
will always be a square. That is, if your normal tile size is 64 and you
want to show a 128x128 icon, the icon is two tiles wide and so it will
take up a 2×2-tile area on the map. The height of a big icon is
irrelevant\--any excess height beyond width/2 is used to show vertical
features. To draw this icon properly, other tiles on that same ground
will be moved behind it in the drawing order. 
One important
warning about using big icons in isometric mode is that you should only
do this with dense atoms. If part of a big mob icon covers the same tile
as a tall building for instance, the tall building is moved back and it
could be partially covered by other turfs that are actually behind it. A
mob walking onto a very large non-dense turf icon would experience
similar irregularities.

### Side-view format <sub><sup>482</sup></sub>
(See more at [Side-view maps](/ref/notes/side.md) ) 
The
`SIDE_MAP` format is like a cross between `TOPDOWN_MAP` and
`ISOMETRIC_MAP`. It looks very similar to a top-down view but it is
intended for more of a 3/4 perspective, where tiles lower on the screen
are considered closer to the viewer. Because this impacts the way layers
work, most of the layering behavior is the same as with isometric.
In a 3/4 perspective the tiles are often foreshortened, so
pixel offsets are adjusted to account for this. For example, you may set
`world.icon_size` to `"32x24"`, but the tile is considered to be a
perfect square if you look at it from the top down. Because the width is
32 pixels, the virtual height is also 32, so if you use pixel_y=32 the
atom will appear one tile further back than it normally is. (This
adjustment doesn\'t affect screen objects or `pixel_w`/`pixel_z`.)
Changing `client.dir` preserves the same tile size regardless
of orientation.

> [!TIP] 
> **See also:**
> +   [icon_size var (world)](/ref/world/var/icon_size.md) 
> +   [view var (world)](/ref/world/var/view.md) 
> +   [view var (client)](/ref/client/var/view.md) 
> +   [screen_loc var (movable atoms)](/ref/atom/movable/var/screen_loc.md) 
> +   [Topdown maps](/ref/notes/topdown.md) 
> +   [Isometric maps](/ref/notes/isometric.md) 
> +   [Side-view maps](/ref/notes/side.md) 
> +   [Big icons](/ref/notes/big-icons.md) 
> +   [Tiled icons](/ref/notes/tiled-icons.md) 
> +   [Understanding the renderer](/ref/notes/renderer.md) 
