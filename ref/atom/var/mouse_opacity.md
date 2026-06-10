
## mouse_opacity (var)

**Default Value:**
+   1
***
This may be used to control how mouse operations on an object are interpreted. A click or mouse movement over an object's icon normally applies to that object only if it is the topmost object that is not transparent at the position of the mouse. Setting `mouse_opacity` to 0 would cause the object to be ignored completely, and setting it to 2 causes it to always be chosen over any lower-level objects, regardless of the transparency of its icon.

Note that overlays and underlays are not distinct objects, so their `mouse_opacity` is completely ignored in favor of the object they're attached to. The same applies to <a href="#/image">image objects</a>, which act like special overlays as well. <a href="#/atom/var/vis_contents">Visual contents</a>, on the other hand, are separate objects that can act like overlays in some ways, but because they're separate their `mouse_opacity` *is* taken into account.

When this is applied to a `PLANE_MASTER` object (see <a href="#/atom/var/appearance_flags">appearance_flags</a>), a value of 0 means everything on the plane is mouse-transparent. 1 means everything on the plane is mouse-visible (using the objects' normal mouse_opacity), but the plane master itself is not. 2 means everything on the plane is mouse-visible, and so is the plane master.
***
**Related Pages:**
+    [mouse handling](/ref/DM/mouse)
+    [overlays](/ref/atom/var/overlays)
+    [underlays](/ref/atom/var/underlays)
+    [vis_contents](/ref/atom/var/vis_contents)
+    [render_source](/ref/atom/var/render_source)
