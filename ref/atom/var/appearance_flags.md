## appearance_flags var (atom) 
###### BYOND Version 509
**See also:**
+   [vars (atom)](/ref/atom/var.md) 
+   [alpha var (atom)](/ref/atom/var/alpha.md) 
+   [color var (atom)](/ref/atom/var/color.md) 
+   [transform var (atom)](/ref/atom/var/transform.md) 
+   [color var (client)](/ref/client/var/color.md) 
+   [Gliding](/ref/%7Bnotes%7D/gliding.md) 
+   [movement_mode var (world)](/ref/world/var/movement_mode.md) 
+   [Understanding the renderer](/ref/%7Bnotes%7D/renderer.md) 
<!-- -->
**Default value:**
+   0
<!-- -->
**Possible values:**
+   Any combination of:
+   **LONG_GLIDE**: Diagonal glides take as long as cardinal ones
+   **RESET_COLOR**: If this is an overlay/image/etc., ignore the
    parent\'s color
+   **RESET_ALPHA**: If this is an overlay/image/etc., ignore the
    parent\'s alpha value
+   **RESET_TRANSFORM**: If this is an overlay/image/etc., ignore the
    parent\'s transform
+   **NO_CLIENT_COLOR**: Ignore client.color
+   **KEEP_TOGETHER**: Draw this icon along with its overlays and
    underlays, as one unit
+   **KEEP_APART**: Detach from a parent icon that uses `KEEP_TOGETHER`
+   **PLANE_MASTER**: Groups all other icons in the same plane
+   **TILE_BOUND**: Avoids more accurate visibility calculations
+   **PIXEL_SCALE**: Use point sampling when transforming this icon
+   **PASS_MOUSE**: If this icon has a `render_source`, pass mouse any
    hits to the render source
+   **TILE_MOVER**: This atom is always locked to the grid


The appearance_flags value controls miscellaneous behavior of
an atom or appearance that doesn\'t make sense to handle in any other
var. 

These values are bitflags, and can be combined with the
`+` or `|` operator.
### LONG_GLIDE


Gliding is normally done by Euclidean (straight-line) distance,
so diagonal gliding across a square tile takes about 41% longer, since
the distance is multiplied by sqrt(2). With `LONG_GLIDE`, the dominant X
or Y direction of the glide is used to adjust the glide size so it takes
just as long as if the object were gliding in a cardinal direction.
### RESET_COLOR, RESET_ALPHA, RESET_TRANSFORM


These flags cause this overlay not to inherit aspects of its
parent object. Ordinarily, transforms on a parent get applied to
overlays too, as does color. 

All of these flags are ignored if
`KEEP_TOGETHER` is used on the parent (and this object does not override
with `KEEP_APART`), since then the parent icon along with all of its
overlays get drawn to a single surface and color, transform, etc. are
applied afterward.
### NO_CLIENT_COLOR


The value of [client.color](/ref/client/var/color.md) {.code} is
normally applied to all icons. This flag says that the icon is an
exception. Generally `client.color` has been superseded by the use of
plane masters anyway. 

The `NO_CLIENT_COLOR` flag is inherited
by overlays and images automatically unless they have the `RESET_COLOR`
flag. It is also basically meaningless when used on an overlay that\'s
inside of a `KEEP_TOGETHER` group, since the client\'s color is applied
to the entire group.
### KEEP_TOGETHER {#keep_together byondver="510"}


This flag is used to force the overlays and underlays of this
icon (its \"children\") to be drawn with it all at once, not each icon
individually. One reason you might want to do this is if your player\'s
icon uses overlays for hair and equipment, and you want to change the
alpha value to make them fade out. With regular drawing, changing the
parent icon\'s alpha means that each individual icon becomes
translucent; with `KEEP_TOGETHER`, the whole combination fades as one
unit. Because this incurs some small overhead, it should be avoided for
atoms that do not need it. 

Any child appearances underneath
`KEEP_TOGETHER` use `NO_CLIENT_COLOR` automatically, and `RESET_COLOR`,
`RESET_ALPHA`, and `RESET_TRANSFORM` become meaningless. Use
`KEEP_APART` with them if you want to use those flags. 

Icons
that are in a different plane from the parent icon will automatically
have `KEEP_APART` set and therefore won\'t be included.
### KEEP_APART {#keep_apart byondver="510"}


If this appearance is a child of something that uses
`KEEP_TOGETHER`, it will be separated out from the main icon and drawn
separately. This may be useful for things such as health meters, for
instance. 

This flag is automatically applied to icons that are
on a different plane from their parents.
### PLANE_MASTER {#plane_master byondver="510"}


Use this flag to group all icons in the same plane and draw
them on a temporary surface the size of the whole screen, and then that
image is drawn over the existing scene. This is useful for
post-processing effects, like lighting. The plane master\'s icon is not
drawn, but its color, transform, and blend_mode are all taken into
account when drawing.
### Example

```
 obj/lighting_plane screen_loc = \"1,1\" plane = 2 blend_mode
= BLEND_MULTIPLY appearance_flags = PLANE_MASTER \| NO_CLIENT_COLOR //
use 20% ambient lighting; be sure to add full alpha color =
list(null,null,null,null,\"#333f\") mouse_opacity = 0 // nothing on this
plane is mouse-visible image/spotlight plane = 2 blend_mode = BLEND_ADD
icon = \'spotlight.dmi\' // a 96x96 white circle pixel_x = -32 pixel_y =
-32 mob/Login() ..() client.screen += new/obj/lighting_plane overlays +=
/image/spotlight 
```
 

In the example, all objects in
plane 2 are lights. They\'re added together, and then the whole image is
put through the color matrix, then multiplied over the rest of the scene
below. This will darken everything that doesn\'t have a spotlight
overlay, but anywhere a spotlight exists will have a circle of light.


The example also makes a point of adding full alpha to the
plane, because a plane is fully transparent by default. However, it\'s
usually a better idea not to mess with the alpha color, and instead use
another icon, scaled to the appropriate size, as a backdrop.


The [mouse_opacity](/ref/atom/var/mouse_opacity.md) {.code} set by the
plane master will determine how the mouse interacts with objects on the
plane. A value of 0 will mean everything in the plane is invisible to
the mouse; 1 means the plane is mouse-invisible but the objects in it
use their own `mouse_opacity`. 2 is the same except the plane itself is
mouse-visible.
### TILE_BOUND {#tile_bound byondver="510"}


There are many ways an object may be shifted out of the normal
bounds of the tile it\'s on: a large icon, pixel offsets, step offsets,
and transform. Ordinarily it\'s desirable to be able to see the object
if it touches any visible turf. However, in some cases it\'s more
desirable to only show the object if its actual loc is in view. The
`TILE_BOUND` flag will accomplish that. This flag is inherited by images
and overlays.
### PIXEL_SCALE {#pixel_scale byondver="511"}


Normally if an icon is transformed via atom.transform, it uses
bilinear texture sampling which produces a nice smooth effect. If you
want a granular pixel-art effect instead, `PIXEL_SCALE` will do that for
you by using nearest-neighbor sampling.
### PASS_MOUSE {#pass_mouse byondver="513"}


If this object has a `render_source` it will take on the
rendered appearance of another object (source). This is just a visual
copy, so the mouse still interacts with this object, not the source. The
`PASS_MOUSE` flag causes any mouse interaction to happen with the source
instead of this object.
### TILE_MOVER {#tile_mover byondver="514"}


This flag indicates this atom is locked to the tile grid as it
would be in [TILE_MOVEMENT_MODE](/ref/world/var/movement_mode.md),
regardless of the setting of `world.movement_mode`. In this way, pixel
movers and tile movers can coexist.