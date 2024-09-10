[]{#/layer var (atom).md}    
## layer var (atom)    
**See also:**    
:   [overlays var (atom)]/atom/var/overlays    
:   [plane var (atom)]/atom/var/plane    
:   [z var (atom)]/atom/var/z    
:   [map_format var (world)]/world/var/map_format    
:   [BACKGROUND_LAYER]/%7Bnotes%7D/BACKGROUND_LAYER    
:   [EFFECTS_LAYER]/%7Bnotes%7D/EFFECTS_LAYER    
:   [TOPDOWN_LAYER]/%7Bnotes%7D/TOPDOWN_LAYER    
:   [Understanding the renderer]/%7Bnotes%7D/renderer    
<!-- -->    
**Default value:**    
:   1 (AREA_LAYER)    
:   2 (TURF_LAYER)    
:   3 (OBJ_LAYER)    
:   4 (MOB_LAYER)    
This numerical value determines the layer in which the object is drawn    
on the map. By default, the order is area, turf, obj, mob, followed by    
missiles and images (in FLY_LAYER, which is 5).    
### Example:    
turf archway layer = MOB_LAYER+1 //overhead    
When making objects to be used as graphical overlays, you should also be    
aware of the special `FLOAT_LAYER` value. This causes the overlay (or    
underlay) to be in the same drawing layer as the base object, no matter    
how that layer changes after the addition of the overlay. Otherwise, the    
overlay object\'s own drawing layer is used.    
The actual drawing order of icons may change depending on    
world.map_format. An isometric map for instance has to display tiles    
that are \"closer\" to the viewer in front of tiles that are in the    
back, so the layer var takes a backseat to the needs of the map. If you    
use the `TOPDOWN_MAP` or `TILED_ICON_MAP` map formats, the layer is more    
important.    
If you are using a `world.map_format` that does not display topdown,    
such as `ISOMETRIC_MAP` or `SIDE_MAP`, then you can use a special layer    
for showing certain portions of the map in topdown mode. For those parts    
of the map, you can add `TOPDOWN_LAYER` to every atom\'s layer to make    
the atom appear in topdown mode. This is for special cases, like for    
instance a battle map in an RPG, where a regular topdown view is    
preferable to the special mapping used by the rest of the game. It is    
recommended that you use `TOPDOWN_LAYER` with every atom in that portion    
of the map, since topdown and isometric maps for instance don\'t mix. If    
you use `TOPDOWN_LAYER`, it is best to use a square size in    
`world.icon_size` if any of these atoms will be moving around.    
Another special layer, `EFFECTS_LAYER`, is also available. Icons that    
use this layer will display above icons that don\'t. `TOPDOWN_LAYER`    
will then display above that. This layer is useful for situations such    
as using a floating name or health meter overlay on a mob in isometric    
mode. When using `EFFECTS_LAYER`, other icons on the regular map won\'t    
cover the overlay. (It is preferable to use atom.plane for this, when    
possible.)    
Finally there is BACKGROUND_LAYER. Adding this to an atom\'s layer will    
make it appear below any atoms that do not use BACKGROUND_LAYER. (It is    
preferable to use atom.plane when possible.)    
The `atom.plane` var takes priority over layer. This is the preferred    
method of handling background and effects.  