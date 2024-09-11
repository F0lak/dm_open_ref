## mouse_drop_pointer var (atom)
**See also:**
*   [MouseDrag proc (atom)](/atom/proc/MouseDrag)
*   [MouseDrop proc (atom)](/atom/proc/MouseDrop)
*   [mouse_drop_pointer var (atom)](/atom/var/mouse_drop_pointer)
*   [mouse_drop_zone var (atom)](/atom/var/mouse_drop_zone)
*   [mouse_opacity var (atom)](/atom/var/mouse_opacity)
*   [mouse_over_pointer var (atom)](/atom/var/mouse_over_pointer)
*   [mouse_pointer_icon var (client)](/client/var/mouse_pointer_icon)
<!-- -->
**Default value:**
*   MOUSE_ACTIVE_POINTER (1)


This defines how the mouse looks when dragging this object over
another object that has `mouse_drop_zone`{.variable} set. The default
value enables the addition of a standard \"droppable\" indicator to
whatever `mouse_drag_pointer`{.variable} is (unless
`mouse_drag_pointer`{.variable} is turned off). 

This variable
may also be set to any of the other [built-in mouse
pointers](/DM/mouse/pointers), or a custom icon or icon state. If an
icon state is specified, this is applied against the object\'s main icon
to find a custom pointer. 

Note that all mouse pointers are
purely visual indicators. They do not effect what objects may actually
be manipulated with the mouse. You control all of the real behavior in
the associated procedures.