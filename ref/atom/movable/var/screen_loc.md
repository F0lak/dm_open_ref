## screen_loc var (movable atoms)
**See also:**
*   [HUD / screen objects](/ref/%7Bnotes%7D/HUD.md) 
*   [layer var (atom)](/ref/atom/var/layer.md) 
*   [screen var (client)](/ref/client/var/screen.md) 
*   [view var (client)](/ref/client/var/view.md) 
*   [map_format var (world)](/ref/world/var/map_format.md) 


This is a text string that controls where an object that is
listed in `client.screen`{.variable} will appear on the user\'s screen.
The format is* 
```
 \"x,y\" \"x:px,y:py\" \"x1,y1 to x2,y2\"

```
 

The bottom left corner of the map viewport
(southwest) is `"1,1"`. If the view is 11x11, then the top-right corner
(northeast) is `"11,11"`. (Changing
[world.map_format](/ref/world/var/map_format.md)  may change the range for
screen_loc.) 

A range of coordinates (the second format above)
causes a square region to be filled with the object at each position.
The southwest and northeast corners of the box are indicated in the
screen_loc value.
### Special keywords


The edges of the map may also be referenced by using
directions, such as `"3,NORTH"`. For convenience, the order of
coordinates is arbitrary when using directions, so one may specify
`y`{.variable} before `x`{.variable} as in `"NORTH,WEST"`. In
expressions such as the latter, you may also leave out the comma. Icon
size is not taken into account, so a big icon with a screen_loc of
`"SOUTHEAST"` will extend further to the right and may create a border
(see \"Outside the map\" below).
The `CENTER` keyword can also be used. This can be used alone to
completely center the object, or as either the x or y component. If the
map covers an even number of tiles in either direction, pixel offsets
will be applied automatically. Centering is relative to the regular map
edges, and it does not take the icon\'s size into account.
The `LEFT`, `RIGHT`, `TOP`, and `BOTTOM` keywords (also `TOPLEFT`,
`TOPRIGHT`, `BOTTOMLEFT`, `BOTTOMRIGHT`) can be used to anchor a screen
object to the edge of the map control if the map is zoomed in so that
some pixels are cut off. When you use these edge-alignment keywords, the
icon size *is* taken into account, and the alignment of the icon changes
to fit whichever edge you use. Because these keywords do not conform to
the normal tile-based structure of the HUD, they can\'t be used for a
range of tiles with the `"to"` format. 

Note:
[Letterboxing](/ref/%7Bskin%7D/param/letterbox.md) , the blank space to either
side of the map if it doesn\'t take up the whole map control, is not
considered usable space. HUD objects aligned to the control edge appear
inside any letterboxing, not on top of it.
### Outside the map


In addition to objects inside of the map view, one may create
border objects. Borders are automatically created when screen objects
are placed at coordinates outside of the inner map view. For example,
objects placed at y=0 fall on a border directly below the map and y=-1
is one tile below that. (The `CENTER` keyword is based on normal
viewport bounds and not any extra borders.) 

A big icon placed
towards the northeast end of the map, if it spills over the edge, will
create a border big enough for the whole icon to be shown. You can avoid
this by using the [`TILE_BOUND` appearance
flag](/ref/atom/var/appearance_flags.md) . Transforms on this atom are not
taken into account when determining whether to add a border.
### Offsets


Offsets may be applied to screen_loc coordinates. For example,
`"NORTH+1,WEST"` is in a border above the map. `"CENTER+2,CENTER-1"`
will appear 2 units right, 1 unit down from the center of the map.
Non-integer offsets like 1.5 are allowed; the fractional part will be
counted towards a pixel offset.
Offsets may be specified in percentages as well. These effectively
always count as pixel offsets and will never be used to determine if a
border should be added. `"WEST+100%"` and `"100%"` are basically
identical to `"EAST"` in most respects, and `"WEST+50%"` is basically
the same as `"CENTER"`. If you\'re using the edge keywords (`LEFT`,
`TOP`, etc.), this percentage is relative to the control edge and also
factors in the icon size, so `"LEFT+100%"` is equivalent to `"RIGHT"`.


It is also possible to specify a pixel offset. Screen objects
do not use `pixel_x` and `pixel_y` for this purpose, because it is
intended that an object could exist on the map and in the screen object
list simultaneously, so positioning must be independent. Pixel offsets
are specified after a colon like this* `"1:16,1:16"`. In this case the
object is shifted to the northeast by 16 pixels.
### Layering


Screen objects on a plane will appear above non-screen objects
on the same plane regardless of layer, except that `BACKGROUND_LAYER` or
`EFFECTS_LAYER` may be used to move the objects forward or back.
### Secondary map controls


You can use HUD objects in any additional [map
controls](/ref/%7Bskin%7D/control/map.md)  that might appear in game\'s skin
file. If you have a second map named `map2` for instance, then you can
use `"map2:1,1"` or something similar as a `screen_loc`. If the map
control is set to automatically scale to fit its contents, it will try
to show every object you put there. 

Note* For secondary-map HUD
items, you should not use the full `window.control` ID, just the
[id](/ref/%7Bskin%7D/param/id.md) .code} of the control itself. Map controls
should always have a unique `id`.