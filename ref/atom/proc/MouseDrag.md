## MouseDrag proc (atom)    
**See also:**    
:   [Click proc (atom)](/atom/proc/Click)    
:   [DblClick proc (atom)](/atom/proc/DblClick)    
:   [MouseDown proc (atom)](/atom/proc/MouseDown)    
:   [MouseDrag proc (client)](/client/proc/MouseDrag)    
:   [MouseDrop proc (atom)](/atom/proc/MouseDrop)    
:   [MouseEntered proc (atom)](/atom/proc/MouseEntered)    
:   [MouseExited proc (atom)](/atom/proc/MouseExited)    
:   [MouseMove proc (atom)](/atom/proc/MouseMove)    
:   [MouseUp proc (atom)](/atom/proc/MouseUp)    
:   [MouseWheel proc (atom)](/atom/proc/MouseWheel)    
:   [mouse_drag_pointer var (atom)](/atom/var/mouse_drag_pointer)    
:   [mouse_drop_pointer var (atom)](/atom/var/mouse_drop_pointer)    
:   [mouse_drop_zone var (atom)](/atom/var/mouse_drop_zone)    
:   [mouse_opacity var (atom)](/atom/var/mouse_opacity)    
:   [mouse_over_pointer var (atom)](/atom/var/mouse_over_pointer)    
:   [show_popup_menus var (client)](/client/var/show_popup_menus)    
<!-- -->    
**Format:**    
:   MouseDrag(over_object,src_location,over_location,src_control,over_control,params)    
<!-- -->    
**Args:**    
:   over_object: the object under the mouse pointer    
:   src_location: the turf, stat panel, grid cell, etc. from where the    
    src object was dragged    
:   over_location: the turf, stat panel, grid cell, etc. containing the    
    object under the mouse pointer    
:   src_control: The id of the skin control the object was dragged from    
:   over_control: The id of the skin control the object was dragged over    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/DM/mouse)    
This is called while dragging this object by pressing and holding the    
left mouse button over the object and moving the mouse. The over_object    
may be null if dragging over a stat panel or over other empty space.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. Most operations can be done    
through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures    
are simply available for completeness.  