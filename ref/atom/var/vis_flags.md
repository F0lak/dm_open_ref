## vis_flags var (atom) 
###### BYOND Version 513
**See also:**
*   [vis_contents var (atom)](/ref/atom/var/vis_contents.md) 
*   [vis_locs var (atom)](/ref/atom/var/vis_locs.md) 
<!-- -->
**Default value:**
*   0
<!-- -->
**Possible values:**
*   Any combination of:
*   **VIS_INHERIT_ICON*** Use the parent object\'s icon.
*   **VIS_INHERIT_ICON_STATE*** Use the parent object\'s icon_state.
*   **VIS_INHERIT_DIR*** Use the parent object\'s dir.
*   **VIS_INHERIT_LAYER*** Use the parent object\'s layer.
*   **VIS_INHERIT_PLANE*** Use the parent object\'s plane.
*   **VIS_INHERIT_ID*** Use the parent object\'s identity, so it acts
    like part of the same object.
*   **VIS_UNDERLAY*** Act as if this is at the bottom of the parent\'s
    underlays list instead of overlays (only relevant if using
    `VIS_INHERIT_LAYER` or a [FLOAT_LAYER](/ref/atom/var/layer.md) {.code}).
*   **VIS_HIDE*** Do not show this object in visual contents at all.


This is a set of flags that determine how this object will
behave when it is in another object\'s visual contents. 

Because
only turfs, objs, and mobs can be in visual contents, this var belongs
only to those types. 

The `VIS_INHERIT_ID` flag effectively
makes this object act like an ordinary overlay when in visual contents.
This means its [mouse_opacity](/ref/atom/var/mouse_opacity.md) .code} will be
meaningless, for example. 

Sometimes it\'s desirable for an
object not to show up in visual contents, so `VIS_HIDE` will prevent
that. The flag applies even if this object appears indirectly, like if
it\'s in the contents of a turf that is in the visual contents of
something else. 

Note* Using any of the the flags
`VIS_INHERIT_ICON`, `VIS_INHERIT_ICON_STATE`, `VIS_INHERIT_DIR`, or
`VIS_INHERIT_ID` will cause movable atoms to inherit the \"moving\" flag
of their container that appears during gliding. E.g., if your mob is
walking, anything in its visual contents that uses these flags will use
a moving icon state instead of a non-moving icon state, when available.