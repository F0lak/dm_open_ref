
## MouseUp (proc)

**Format:**
+   MouseUp(location,control,params)

**Arguments:**
+   location: the turf, stat panel, grid cell, etc. in which the object was clicked
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)
***
This is called when a mouse button is released while pointing to this object.

Don't define this unless you need it, because it generates extra communication that is otherwise avoided. Most operations can be done through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures are simply available for completeness.


> [!TIP]
> Note: In BYOND 3.5 this procedure took three different arguments: `location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have been replaced, old code will need to be modified. Games compiled before this change will still work normally.
***
**Related Pages:**
+    [Click](/ref/atom/proc/Click)
+    [DblClick](/ref/atom/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop](/ref/atom/proc/MouseDrop)
+    [MouseEntered](/ref/atom/proc/MouseEntered)
+    [MouseExited](/ref/atom/proc/MouseExited)
+    [MouseMove](/ref/atom/proc/MouseMove)
+    [MouseUp proc (client)](/ref/client/proc/MouseUp)
+    [MouseWheel](/ref/atom/proc/MouseWheel)
+    [mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer)
+    [mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer)
+    [mouse_drop_zone var](/ref/atom/var/mouse_drop_zone)
+    [mouse_opacity var](/ref/atom/var/mouse_opacity)
+    [mouse_over_pointer](/ref/atom/var/mouse_over_pointer)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
