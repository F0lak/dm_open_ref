## mouse_pointer_icon var (client)

**Default value:**
+   null


This is an icon file (.dmi) containing custom mouse cursors to
use in place of the standard ones. The different possible mouse states
are distinguished by special icon state names:
""
+   Activated when over empty space or an object with mouse_over_pointer
    = MOUSE_INACTIVE_POINTER.
"over"
+   Activated when over an object with mouse_over_pointer =
    MOUSE_ACTIVE_POINTER.
"drag"
+   Activated when dragging an object with mouse_drag_pointer =
    MOUSE_ACTIVE_POINTER.
"drop"
+   Activated when dragging an object over with mouse_drop_pointer =
    MOUSE_ACTIVE_POINTER and the object underneath has mouse_drop_zone
    set.
"all"
+   Always activated, no matter what the state of the mouse.

> [!TIP] 
> **See also:**
> +   [Click proc (client)](/ref/client/proc/Click.md) 
> +   [MouseDown proc (client)](/ref/client/proc/MouseDown.md) 
> +   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) 
> +   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) 
> +   [MouseUp proc (client)](/ref/client/proc/MouseUp.md) 
> +   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) 
> +   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) 
> +   [mouse_drop_zone var (atom)](/ref/atom/var/mouse_drop_zone.md) 
> +   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) <!-- -->