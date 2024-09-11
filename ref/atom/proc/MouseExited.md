## MouseExited proc (atom)
**See also:**
*   [Click proc (atom)](/ref/atom/proc/Click.md) -m
*   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) -m
*   [MouseDown proc (atom)](/ref/atom/proc/MouseDown.md) -m
*   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) -m
*   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) -m
*   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered.md) -m
*   [MouseExited proc (client)](/ref/client/proc/MouseExited.md) -m
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
*   MouseExited(location,control,params)
<!-- -->
**Args:**
*   location* the turf, stat panel, grid cell, etc. containing the
    object
*   control* the name of the skin control involved
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) -m

This is called when the mouse moves off of an object with no
buttons pressed. 

Don\'t define this unless you need it, because
it generates extra communication that is otherwise avoided. Defining it
on only the objects that require it reduces overhead.