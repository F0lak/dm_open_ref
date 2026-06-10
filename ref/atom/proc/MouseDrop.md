
## MouseDrop (proc)

**Format:**
+   MouseDrop(over_object,src_location,over_location,src_control,over_control,params)

**Arguments:**
+   over_object: the object under the mouse pointer
+   src_location: the turf, stat panel, grid cell, etc. from where the src object was dragged
+   over_location: the turf, stat panel, grid cell, etc. containing the object under the mouse pointer
+   src_control: The id of the skin control the object was dragged from
+   over_control: The id of the skin control the object was dropped onto
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)
***
This is called when the a mouse button is released after dragging this object. The over_object may be null if dropping over a stat panel or over other empty space.
***
**Related Pages:**
+    [Click](/ref/atom/proc/Click)
+    [DblClick](/ref/atom/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop proc (client)](/ref/client/proc/MouseDrop)
+    [MouseEntered](/ref/atom/proc/MouseEntered)
+    [MouseExited](/ref/atom/proc/MouseExited)
+    [MouseMove](/ref/atom/proc/MouseMove)
+    [MouseUp](/ref/atom/proc/MouseUp)
+    [MouseWheel](/ref/atom/proc/MouseWheel)
+    [mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer)
+    [mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer)
+    [mouse_drop_zone var](/ref/atom/var/mouse_drop_zone)
+    [mouse_opacity var](/ref/atom/var/mouse_opacity)
+    [mouse_over_pointer](/ref/atom/var/mouse_over_pointer)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
