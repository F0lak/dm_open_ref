
## vis_locs (var)

**Default Value:**
+   Empty list.
***
This list is the opposite of the <code>vis_contents</code> list. If this atom is in any other atoms' visual contents, those parent atoms will appear in this list.

Because only turfs, objs, and mobs can be in visual contents, this var belongs only to those types.

Being in a visual locs list does not count as a <a href="#/DM/garbage">reference</a>, the same way that being a movable's loc does not count as a reference. If an object in this list otherwise runs out of references, it will be garbage collected and therefore removed from this list.
***
**Related Pages:**
+    [vis_contents](/ref/atom/var/vis_contents)
+    [vis_flags](/ref/atom/var/vis_flags)
+    [image objects](/ref/image)
+    [HUD / screen objects](/ref/{notes}/HUD)
