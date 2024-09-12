## MouseEntered proc (atom)
**See also:**
+   [Click proc (atom)](/ref/atom/proc/Click.md) 
+   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) 
+   [MouseDown proc (atom)](/ref/atom/proc/MouseDown.md) 
+   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) 
+   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) 
+   [MouseEntered proc (client)](/ref/client/proc/MouseEntered.md) 
+   [MouseExited proc (atom)](/ref/atom/proc/MouseExited.md) 
+   [MouseMove proc (atom)](/ref/atom/proc/MouseMove.md) 
+   [MouseUp proc (atom)](/ref/atom/proc/MouseUp.md) 
+   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel.md) 
+   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer.md) 
+   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) 
+   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) 
+   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) 
+   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) 
<!-- -->
**Format:**
+   MouseEntered(location,control,params)
<!-- -->
**Args:**
+   location+ the turf, stat panel, grid cell, etc. containing the
    object
+   control+ the name of the skin control involved
+   params+ other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) 

This is called when the mouse moves onto the object with no
buttons pressed. 

Don\'t define this unless you need it, because
it generates extra communication that is otherwise avoided. Defining it
on only the objects that require it reduces overhead.