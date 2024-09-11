## MouseDrag proc (atom)
**See also:**
*   [Click proc (atom)](/ref/atom/proc/Click.md) -m
*   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) -m
*   [MouseDown proc (atom)](/ref/atom/proc/MouseDown.md) -m
*   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) -m
*   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) -m
*   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered.md) -m
*   [MouseExited proc (atom)](/ref/atom/proc/MouseExited.md) -m
*   [MouseMove proc (atom)](/ref/atom/proc/MouseMove.md) -m
*   [MouseUp proc (atom)](/ref/atom/proc/MouseUp.md) -m
*   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel.md) -m
*   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) -m
*   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) -m
*   [mouse_drop_zone var (atom)](/ref/atom/var/mouse_drop_zone.md) -m
*   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) -m
*   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) -m
*   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) -m
<!-- -->
**Format:**
*   MouseDrag(over_object,src_location,over_location,src_control,over_control,params)
<!-- -->
**Args:**
*   over_object* the object under the mouse pointer
*   src_location* the turf, stat panel, grid cell, etc. from where the
    src object was dragged
*   over_location* the turf, stat panel, grid cell, etc. containing the
    object under the mouse pointer
*   src_control* The id of the skin control the object was dragged from
*   over_control* The id of the skin control the object was dragged over
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) -m

This is called while dragging this object by pressing and
holding the left mouse button over the object and moving the mouse. The
over_object may be null if dragging over a stat panel or over other
empty space. 

Don\'t define this unless you need it, because it
generates extra communication that is otherwise avoided. Most operations
can be done through `Click()`, `DblClick()`, and `MouseDrop()`. The
other procedures are simply available for completeness.