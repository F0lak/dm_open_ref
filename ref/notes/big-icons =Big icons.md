[]{#/Big icons.md}/big-icons toc="Big icons"}    
## Big icons    
**See also:**    
:   [icon](/icon)    
:   [procs (icon)](/icon/proc)    
:   [Blend proc (icon)](/icon/proc/Blend)    
:   [map_format var (world)](/world/var/map_format)    
:   [icon_size var (world)](/world/var/icon_size)    
:   [Tiled icons](/%7Bnotes%7D/tiled-icons)    
:   [Isometric maps](/%7Bnotes%7D/isometric)    
:   [Side-view maps](/%7Bnotes%7D/side)    
BYOND allows you to use icons that are not the same size as the tile    
size defined in world.icon_size. These icons can be manipulated with the    
/icon datum using their raw, native size, and shown on the map in full    
size. To use the old behavior where an atom can display only an icon of    
the normal tile size, use the TILED_ICON_MAP value for map_format    
instead.    
When you use an icon of non-standard size on an atom, the icon is    
\"anchored\" to the southwest corner of the atom. If you are using a    
top-down view (world.map_format=TOPDOWN_MAP), the icon will appear to    
spread out further to the east and north. In an isometric map    
(world.map_format=ISOMETRIC_MAP), the icon will cover additional tiles    
north and east as well. The \"footprint\" of an isometric icon\--the    
actual map tiles it covers\--is always square, so if your tile size is    
64x64 and you use a 128x64 icon, the 128-pixel width means the icon will    
cover a 2x2 section of map tiles.    
It is important to remember that using a big icon is a visual effect    
*only*. It will not affect how the atom bumps into other atoms or    
vice-versa.    
Big icons will affect layering\--the order in which icons are drawn. In    
general, because a big icon is covering more than one tile of the map,    
it will try to draw above any other tiles in that space that are on the    
same layer. This way, you can set a turf to use a big icon without    
having to change the turfs to the north and east. If an atom has a big    
icon, any overlays and underlays attached to it will be pulled forward    
as well, so they will draw in front of anything on their same layer. In    
isometric mode this is about the same, except that the layer isn\'t that    
important\--anything in the way will just be moved back behind the big    
icon.    
Note: Big overlays will not \"pull forward\" on their own. If the main    
atom uses a single-tile icon, a big overlay attached to it will not try    
to draw in front of other icons on the same layer. This is so that name    
labels, health bar overlays, etc. will not cause any odd behavior. To be    
safe, you should always specify a layer when adding an overlay.    
In isometric mode, layering is affected by the \"distance\" between the    
atom and the viewer, so putting a regular-sized icon and part of a big    
icon on the same tile could cause layering oddities. Tiles that are    
covered by a big icon will tend to be drawn behind the big icon as    
mentioned above. For this reason, any atoms whose icons cover more than    
one tile (the extra height of an isometric icon doesn\'t count) should    
always be dense, and you should block movement onto any tile covered by    
them.    
When manipulating icons with the /icon datum, you can still use Blend()    
to combine icons of different sizes. By default, the icons will be lined    
up at their southwest corners. You can change the position at which the    
second icon is blended.  