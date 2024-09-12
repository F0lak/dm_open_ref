## Side-view maps 
###### BYOND Version 482



The side-view map format is used for 3/4 perspective, where the
map is basically similar to a top-down view but is usually
foreshortened. Just like with isometric projection, tiles that are
closer to the bottom of the screen are considered to be closer to the
viewer. This is a form of pseudo-3D in which the 2D icons used by BYOND
can be arranged in a way to give the appearance of three dimensions.


It is important to remember that this is an illusion of 3D, not
real 3D. 

The `layer` var behaves much the same way it does in
`ISOMETRIC_MAP` mode.See [isometric maps](/ref/%7Bnotes%7D/isometric.md) for
more information. 

When using this mode you may want to use a
foreshortened `world.icon_size`, like a 32x24 format instead of 32x32
for example, and use taller icons for any vertical structures like walls
or buildings. If you set `world.icon_size` to use foreshortening, then
`pixel_y` (or `pixel_x`, depending on the orientation of client.dir)
will be adjusted for you; the same applies to `step_x` and `step_y`. For
example, with `world.icon_size` set to `"64x32"`, the *physical*
tile---what you would see if you were to look at it straight down from
above--- is considered to be 64x64, so you would need `pixel_y=64` or
`step_y=64` to offset by a whole tile. This adjustment does not apply to
screen objects, `pixel_w`, or `pixel_z`.

**See also:**
+   [map_format var (world)](/ref/world/var/map_format.md) 
+   [icon_size var (world)](/ref/world/var/icon_size.md) 
+   [dir var (client)](/ref/client/var/dir.md) 
+   [pixel_w var (atom)](/ref/atom/var/pixel_w.md) 
+   [pixel_z var (atom)](/ref/atom/var/pixel_z.md) 
+   [screen_loc var (movable atoms)](/ref/atom/movable/var/screen_loc.md) 
+   [Big icons](/ref/%7Bnotes%7D/big-icons.md) 
+   [Isometric maps](/ref/%7Bnotes%7D/isometric.md) 
+   [Topdown maps](/ref/%7Bnotes%7D/topdown.md) 
+   [HUD](/ref/%7Bnotes%7D/HUD.md) 
+   [BACKGROUND_LAYER](/ref/%7Bnotes%7D/BACKGROUND_LAYER.md) 
+   [EFFECTS_LAYER](/ref/%7Bnotes%7D/EFFECTS_LAYER.md) 
+   [TOPDOWN_LAYER](/ref/%7Bnotes%7D/topdown_layer.md) 