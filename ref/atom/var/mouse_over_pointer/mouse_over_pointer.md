[]{#/atom/var/mouse_over_pointer}    
## mouse_over_pointer var (atom)    
**See also:**    
:   [Click proc (atom)](/ref/atom/proc/Click/Click.md)    
:   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered/MouseEntered.md)    
:   [MouseExited proc (atom)](/ref/atom/proc/MouseExited/MouseExited.md)    
:   [MouseMove proc (atom)](/ref/atom/proc/MouseMove/MouseMove.md)    
:   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer/mouse_drag_pointer.md)    
:   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer/mouse_drop_pointer.md)    
:   [mouse_drop_zone var (atom)](/ref/atom/var/mouse_drop_zone/mouse_drop_zone.md)    
:   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity/mouse_opacity.md)    
:   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon/mouse_pointer_icon.md)    
<!-- -->    
**Default value:**    
:   MOUSE_INACTIVE_POINTER (0)    
This defines how the mouse looks when no buttons are pressed and it is    
held over this object. Assigning this to MOUSE_ACTIVE_POINTER (1)    
enables the default indicator that there is something special under the    
mouse (crosshairs).    
This variable may also be set to any of the other [built-in mouse    
pointers](/ref/DM/mouse/pointers/pointers.md), or a custom icon or icon state. If an    
icon state is specified, this is applied against the object\'s main icon    
to find a custom pointer.    
Note that all mouse pointers are purely visual indicators. They do not    
effect what objects may actually be manipulated with the mouse. You    
control all of the real behavior in the associated procedures.  