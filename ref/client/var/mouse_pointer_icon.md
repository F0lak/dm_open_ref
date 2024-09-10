[]{#/mouse_pointer_icon var (client).md}    
## mouse_pointer_icon var (client)    
**See also:**    
:   [Click proc (client)]/client/proc/Click    
:   [MouseDown proc (client)]/client/proc/MouseDown    
:   [MouseDrag proc (client)]/client/proc/MouseDrag    
:   [MouseDrag proc (client)]/client/proc/MouseDrag    
:   [MouseUp proc (client)]/client/proc/MouseUp    
:   [mouse_drag_pointer var (atom)]/atom/var/mouse_drag_pointer    
:   [mouse_drag_pointer var (atom)]/atom/var/mouse_drag_pointer    
:   [mouse_drop_zone var (atom)]/atom/var/mouse_drop_zone    
:   [mouse_over_pointer var (atom)]/atom/var/mouse_over_pointer    
<!-- -->    
**Default value:**    
:   null    
This is an icon file (.dmi) containing custom mouse cursors to use in    
place of the standard ones. The different possible mouse states are    
distinguished by special icon state names:    
\"\"    
:   Activated when over empty space or an object with mouse_over_pointer    
    = MOUSE_INACTIVE_POINTER.    
\"over\"    
:   Activated when over an object with mouse_over_pointer =    
    MOUSE_ACTIVE_POINTER.    
\"drag\"    
:   Activated when dragging an object with mouse_drag_pointer =    
    MOUSE_ACTIVE_POINTER.    
\"drop\"    
:   Activated when dragging an object over with mouse_drop_pointer =    
    MOUSE_ACTIVE_POINTER and the object underneath has mouse_drop_zone    
    set.    
\"all\"    
:   Always activated, no matter what the state of the mouse.  