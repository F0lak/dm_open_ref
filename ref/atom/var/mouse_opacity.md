## mouse_opacity var (atom)
**See also:**
*   [mouse handling](/ref/DM/mouse.md) -m
*   [overlays var (atom)](/ref/atom/var/overlays.md) -m
*   [underlays var (atom)](/ref/atom/var/underlays.md) -m
*   [vis_contents var (atom)](/ref/atom/var/vis_contents.md) -m
*   [render_source var (atom)](/ref/atom/var/render_source.md) -m
<!-- -->
**Default value:**
*   1
<!-- -->
**Possible values:**
*   0 // transparent to mouse
*   1 // mouse-opaque where icon is also opaque
*   2 // completely mouse-opaque


This may be used to control how mouse operations on an object
are interpreted. A click or mouse movement over an object\'s icon
normally applies to that object only if it is the topmost object that is
not transparent at the position of the mouse. Setting `mouse_opacity` to
0 would cause the object to be ignored completely, and setting it to 2
causes it to always be chosen over any lower-level objects, regardless
of the transparency of its icon. 

Note that overlays and
underlays are not distinct objects, so their `mouse_opacity` is
completely ignored in favor of the object they\'re attached to. The same
applies to [image objects](/ref/image.md) -m, which act like special overlays as
well. [Visual contents](/ref/atom/var/vis_contents.md) -m, on the other hand, are
separate objects that can act like overlays in some ways, but because
they\'re separate their `mouse_opacity` *is* taken into account.


When this is applied to a `PLANE_MASTER` object (see
[appearance_flags](/ref/atom/var/appearance_flags.md) -m, a value of 0 means
everything on the plane is mouse-transparent. 1 means everything on the
plane is mouse-visible (using the objects\' normal mouse_opacity), but
the plane master itself is not. 2 means everything on the plane is
mouse-visible, and so is the plane master.