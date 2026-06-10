
## mouse_drag_pointer (var)

**Default Value:**
+   MOUSE_INACTIVE_POINTER (0)
***
This defines how the mouse looks when dragging this object. Assigning this to MOUSE_ACTIVE_POINTER (1) enables the default dragging indicator.

This variable may also be set to any of the other <a href="#/DM/mouse/pointers">built-in mouse pointers</a>, or a custom icon or icon state. If an icon state is specified, this is applied against the object's main icon to find a custom pointer.

Note that all mouse pointers are purely visual indicators. They do not effect what objects may actually be manipulated with the mouse. You control all of the real behavior in the associated procedures.
***
**Related Pages:**
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop](/ref/atom/proc/MouseDrop)
+    [mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer)
+    [mouse_drop_zone var](/ref/atom/var/mouse_drop_zone)
+    [mouse_over_pointer](/ref/atom/var/mouse_over_pointer)
+    [mouse_pointer_icon](/ref/client/var/mouse_pointer_icon)
