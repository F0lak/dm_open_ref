## Topdown maps

By default, BYOND displays all maps in top-down format, so
`world.map_format` is set to `TOPDOWN_MAP` unless you say otherwise.
This view means players are looking down on the map, and "north"
corresponds to the top of their screen. (This can be changed by setting
`client.dir`.) 

A related map_format, used by older games, is
`TILED_ICON_MAP`. This is also topdown but it handles icons differently.

In this form, the `layer` var behaves exactly as you would
expect: Icons with a lower layer are drawn beneath icons with a higher
layer. The only exception is when you use [big
icons](/ref/notes/big-icons.md)  which will be drawn above any other
icons on the same layer. Also an atom\'s underlays will be drawn behind
it unless their layer is changed, and its overlays will draw in front of
it unless otherwise stated. 

Topdown mode also guarantees that
`world.view` or `client.view` will set the exact screen size used by the
HUD, except for HUD objects that appear outside of the normal bounds.

Screen objects (also called the HUD) cannot be intermixed with
topdown icons. They will appear on top of other icons, unless using a
lower plane or a special layer like `BACKGROUND_LAYER`.

> [!TIP] 
> **See also:**
> +   [map_format var (world)](/ref/world/var/map_format.md) 
> +   [icon_size var (world)](/ref/world/var/icon_size.md) 
> +   [dir var (client)](/ref/client/var/dir.md) 
> +   [layer var (atom)](/ref/atom/var/layer.md) 
> +   [plane var (atom)](/ref/atom/var/plane.md) 
> +   [screen_loc var (movable atoms)](/ref/atom/movable/var/screen_loc.md) 
> +   [Big icons](/ref/notes/big-icons.md) 
> +   [HUD](/ref/notes/HUD.md) 
> +   [Isometric maps](/ref/notes/isometric.md) 
> +   [Side-view maps](/ref/notes/side.md) 
> +   [Understanding the renderer](/ref/notes/renderer.md) 