## mouse pointers
**See also:**
*   [mouse handling](/ref/DM/mouse.md) -m
*   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) -m
*   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) -m
*   [mouse_drop_zone var (atom)](/ref/atom/var/mouse_drop_zone.md) -m
*   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) -m
*   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) -m
*   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon.md) -m

The following mouse pointers are built-in and may be assigned
to any of the mouse pointer variables. Of course, you can also define
your own custom mouse pointers using an icon file.
MOUSE_INACTIVE_POINTER (0)
MOUSE_ACTIVE_POINTER (1)
MOUSE_DRAG_POINTER
Same as mouse_drag_pointer = MOUSE_ACTIVE_POINTER.
MOUSE_DROP_POINTER
Same as mouse_drop_pointer = MOUSE_ACTIVE_POINTER.
MOUSE_ARROW_POINTER
Same as mouse_over_pointer = MOUSE_INACTIVE_POINTER.
MOUSE_CROSSHAIRS_POINTER
Same as mouse_over_pointer = MOUSE_ACTIVE_POINTER.
MOUSE_HAND_POINTER