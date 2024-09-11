## MouseDown proc (atom)
**See also:**
*   [Click proc (atom)](/ref/atom/proc/Click.md) -m
*   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) -m
*   [MouseDown proc (client)](/ref/client/proc/MouseDown.md) -m
*   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) -m
*   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) -m
*   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered.md) -m
*   [MouseExited proc (atom)](/ref/atom/proc/MouseExited.md) -m
*   [MouseMove proc (atom)](/ref/atom/proc/MouseMove.md) -m
*   [MouseUp proc (atom)](/ref/atom/proc/MouseUp.md) -m
*   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel.md) -m
*   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) -m
*   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) -m
*   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) -m
*   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) -m
*   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) -m
<!-- -->
**Format:**
*   MouseDown(location,control,params)
<!-- -->
**Args:**
*   location* the turf, stat panel, grid cell, etc. in which the object
    was clicked
*   control* the name of the skin control involved
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) -m

This is called when a mouse button is pressed while pointing to
this object. 

Don\'t define this unless you need it, because it
generates extra communication that is otherwise avoided. Most operations
can be done through `Click()`, `DblClick()`, and `MouseDrop()`. The
other procedures are simply available for completeness.
Note* In BYOND 3.5 this procedure took three different arguments:
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have
been replaced, old code will need to be modified. Games compiled before
this change will still work normally.