## mouse_drop_zone var (atom)
**See also:**
*   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) -m
*   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) -m
*   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) -m
*   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) -m
*   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) -m
*   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) -m
*   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon.md) -m<!-- -->
**Default value:**
*   0


Setting this to 1 indicates that this object is a valid site on
which to drop other objects. While dragging,
`mouse_drop_cursor`{.variable} of the object being dragged will become
active in this case. Note that this is a purely visual effect. It does
not control what the user may do with the mouse. You control the real
behavior with the associated procedures.