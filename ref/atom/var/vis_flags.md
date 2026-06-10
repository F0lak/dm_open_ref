
## vis_flags (var)

**Default Value:**
+   0
***
This is a set of flags that determine how this object will behave when it is in another object's visual contents.

Because only turfs, objs, and mobs can be in visual contents, this var belongs only to those types.

The `VIS_INHERIT_ID` flag effectively makes this object act like an ordinary overlay when in visual contents. This means its <a class="code" href="#/atom/var/mouse_opacity">mouse_opacity</a> will be meaningless, for example.

Sometimes it's desirable for an object not to show up in visual contents, so `VIS_HIDE` will prevent that. The flag applies even if this object appears indirectly, like if it's in the contents of a turf that is in the visual contents of something else.

Note: Using any of the the flags `VIS_INHERIT_ICON`, `VIS_INHERIT_ICON_STATE`, `VIS_INHERIT_DIR`, or `VIS_INHERIT_ID` will cause movable atoms to inherit the "moving" flag of their container that appears during gliding. E.g., if your mob is walking, anything in its visual contents that uses these flags will use a moving icon state instead of a non-moving icon state, when available.
***
**Related Pages:**
+    [vis_contents](/ref/atom/var/vis_contents)
+    [vis_locs](/ref/atom/var/vis_locs)
