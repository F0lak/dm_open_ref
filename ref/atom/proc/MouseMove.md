
## MouseMove (proc)

**Format:**
+   MouseMove(location,control,params)

**Arguments:**
+   location: the turf, stat panel, grid cell, etc. containing the object
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)
***
This is called when the mouse moves over the object with no buttons pressed. When the mouse moves over for the first time, MouseEntered() is called instead.

Don't define this unless you need it, because it generates extra communication that is otherwise avoided. Defining it on only the objects that require it reduces overhead.
***
**Related Pages:**
+    [Click](/ref/atom/proc/Click)
+    [DblClick](/ref/atom/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop](/ref/atom/proc/MouseDrop)
+    [MouseEntered](/ref/atom/proc/MouseEntered)
+    [MouseExited](/ref/atom/proc/MouseExited)
+    [MouseMove proc (client)](/ref/client/proc/MouseMove)
+    [MouseUp](/ref/atom/proc/MouseUp)
+    [MouseWheel](/ref/atom/proc/MouseWheel)
+    [mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer)
+    [mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer)
+    [mouse_opacity var](/ref/atom/var/mouse_opacity)
+    [mouse_over_pointer](/ref/atom/var/mouse_over_pointer)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
