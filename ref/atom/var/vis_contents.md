## vis_contents var (atom) 
###### BYOND Version 512

<!-- -->
**Default value:**
+   Empty list.


Turfs, movable atoms, and images can be given a list of atoms
(limited to turfs and movable atoms) that are attached to them visually,
like an overlay or image object, but act independently and have their
own identity. These are **visual contents**. The purpose of visual
contents is to provide an alternative system to overlays and images,
with a little more flexibility for various special effects. 

For
example, a mob with an obj in its visual contents will show the obj as
if it\'s following the mob around like an overlay, but clicking on the
obj will not---unlike an overlay or an image object---count as a click
on the mob. Likewise, the obj will retain its own separate
`mouse_opacity` setting, which is not true of regular overlays.


An atom that appears on the map normally can still be in the
visual contents of another atom. However it will not apply gliding and
step offsets here. Also, considerations like visibility will not apply.


If a turf is in an atom\'s visual contents, the turf and all of
that turf\'s contents will be displayed. (In the case of big atoms, or
movable atoms with step offsets, only atoms that actually have that turf
as their loc will appear. \"Overhangers\" will not.) Gliding and step
offsets *will* be applied to that turf\'s contents normally; but again
visibility, opacity, etc. will not be considered. (If you have one or
more turfs in visual contents, an object gliding to a new turf outside
of that list will not be shown because it\'s already technically on the
new turf.) 

If *multiple* turfs are present in visual contents,
they will be offset as needed (relative to the southwest-most turf) to
appear in the correct positions. That is, `pixel_x` and `pixel_y`
offsets will be applied automatically, so if you add an entire block to
visual contents (be aware this will impact performance), you don\'t have
to do anything else to make the block appear normal. 

You can
alter some aspects of how an object behaves when in visual contents by
changing its [vis_flags](/ref/atom/var/vis_flags.md) {.code} var. In particular
this is useful if you want an object to behave more like an overlay,
inheriting aspects of its parent object or even acting like a part of
that object instead of an independent one. Also this can make an object
act like an underlay instead of an overlay when using a floating layer.


Visual contents do not impact the results of `view()` or
`range()`, or verb availability, in any way. This is strictly a visual
effect. 

Being in a visual contents list counts as a
[reference](/ref/DM/garbage.md) for anything in the list, the same way that
being on the map or inside of a movable counts as a reference.

**See also:**
+   [vis_locs var (atom)](/ref/atom/var/vis_locs.md) 
+   [vis_flags var (atom)](/ref/atom/var/vis_flags.md) 
+   [image objects](/ref/image.md) 
+   [HUD / screen objects](/ref/%7Bnotes%7D/HUD.md) 