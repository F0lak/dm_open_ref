## mouse_drop_pointer var (atom)
**See also:**
+   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) 
+   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) 
+   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer.md) 
+   [mouse_drop_zone var (atom)](/ref/atom/var/mouse_drop_zone.md) 
+   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) 
+   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) 
+   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon.md) 
<!-- -->
**Default value:**
+   MOUSE_ACTIVE_POINTER (1)


This defines how the mouse looks when dragging this object over
another object that has `mouse_drop_zone`{.variable} set. The default
value enables the addition of a standard \"droppable\" indicator to
whatever `mouse_drag_pointer`{.variable} is (unless
`mouse_drag_pointer`{.variable} is turned off). 

This variable
may also be set to any of the other [built-in mouse
pointers](/ref/DM/mouse/pointers.md)  or a custom icon or icon state. If an
icon state is specified, this is applied against the object\'s main icon
to find a custom pointer. 

Note that all mouse pointers are
purely visual indicators. They do not effect what objects may actually
be manipulated with the mouse. You control all of the real behavior in
the associated procedures.