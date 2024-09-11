## Tiled icons
**See also:**
*   [icon](/icon)
*   [procs (icon)](/icon/proc)
*   [map_format var (world)](/world/var/map_format)
*   [icon_size var (world)](/world/var/icon_size)
*   [Big icons](/%7Bnotes%7D/big-icons)


In BYOND 3.0, any file like a large .bmp would be treated like
a regular icon that had been broken up into several tile-sized icon
states. All tiles then were 32x32 pixels. An image that was 100x100
would therefore take at least 4x4 tiles to display. The icon was padded
to the right and the top with blank space to become an even multiple of
32x32, and then broken up into sections. The lower left section was
given an icon_state of `"0,0"`, the next to the right was `"1,0"`, and
so on, up to the upper right which was `"3,3"`. Another icon state, a
32x32 thumbnail of the big image, was also included. 

BYOND 4.0
expanded on this concept by allowing icons to be defined that had
individual graphics bigger than 32x32, and it would break each one up
into tiles just like 3.0 did. If an icon had a state called `"open"`
then it might break down into `"open 0,0"`, `"open 1,0"`, and so on,
while the actual `"open"` state would be a thumbnail image. To show the
whole image, you would have to have a separate atom or overlay for each
individual tile. 

In newer versions, breaking big icons into
tiles is no longer done by default. Instead, icons are shown and
manipulated in their [native size](/%7Bnotes%7D/big-icons). To use the
old method of breaking icons into tiles, set `world.map_format` to
`TILED_ICON_MAP`. This is the default for all projects compiled before
version 455. 

When using tiled icons, there are some important
things to note:
-   You need to use extra atoms or overlays to show any icon bigger than
    a single tile, where each atom/overlay shows an individual
    tile-sized piece of the big icon.
-   The icon_state names of each tile are always the original name
    followed by a space, followed by x,y tile coordinates such as 0,0 or
    2,1, so the northeast corner of `"flag"` might for instance be
    `"flag 3,2"`. If the original icon_state had no name, the space is
    left out and only the x,y coordinates are used.
-   Every icon\'s size is a multiple of world.icon_size. If an icon of
    an incompatible size is used, it will be padded to the nearest full
    tile size.
-   `Crop()` and `Scale()` always pad their results to the nearest full
    tile size.
-   `icon.Insert()` can insert a single-tile icon into a multi-tiled big
    icon using the appropriate icon_state; e.g., inserting into
    `"door 0,0"` will replace the southwest corner of the `"door"`
    state.
-   Using the `icon()` proc, you can extract a single tile from a
    multi-tiled big icon.


This example shows a big icon being applied to an atom in tiled
mode, as overlays:
### Example:

```
 // icon is 3 tiles wide by 2 high icon_state = \"0,0\" // A
temporary object used for the overlays var/obj/O = new O.icon = icon
O.layer = FLOAT_LAYER for(var/tile_y=0, tile_y\<2, ++tile_y)
for(var/tile_x=0, tile_x\<3, ++tile_x) if(tile_x && tile_y) O.pixel_x =
tile_x \* 32 O.pixel_y = tile_y \* 32 O.icon_state =
\"\[tile_x\],\[tile_y\]\" overlays += O 
```
