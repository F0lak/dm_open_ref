[]{#/{notes}/BACKGROUND_LAYER}
## BACKGROUND_LAYER
**See also:**
:   [layer var (atom)](#/atom/var/layer)
:   [plane var (atom)](#/atom/var/plane)
:   [map_format var (world)](#/world/var/map_format)
:   [EFFECTS_LAYER](#/%7Bnotes%7D/EFFECTS_LAYER)
:   [TOPDOWN_LAYER](#/%7Bnotes%7D/TOPDOWN_LAYER)
:   [stddef.dm file](#/%7B%7Bappendix%7D%7D/stddef%2edm)
:   [Understanding the renderer](#/%7Bnotes%7D/renderer)
This is mostly no longer needed. A negative value for plane is the
preferred way to do show objects in the background. It can still be used
however when you want to rearrange objects in the same plane when using
[PLANE_MASTER](#/atom/var/appearance_flags){.code} for visual effects.
`BACKGROUND_LAYER` is a special high value that can be added to the
regular layer of any atom.
The purpose of this value is to make an atom appear below any regular
atoms, even if they share the same plane. In an isometric map for
instance, HUD objects will always appear above the map, but makeing a
HUD object appear behind the map was basically impossible without this
feature until `plane` was implemented.
When using this special layer, it should be added to the layer an atom
normally uses. For instance an obj should have a layer of
`BACKGROUND_LAYER + OBJ_LAYER`.
This can be mixed with `TOPDOWN_LAYER` and `EFFECTS_LAYER`, but it will
take precedence over both. Anything with `BACKGROUND_LAYER` will always
appear below anything without it on the same plane.
Images or overlays with `FLOAT_LAYER` can be left alone. They will
automatically have the same layer as whatever atom they are attached to.