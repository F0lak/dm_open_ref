[]{#/MouseExited proc (atom).md}    
## MouseExited proc (atom)    
**See also:**    
:   [Click proc (atom)]/atom/proc/Click    
:   [DblClick proc (atom)]/atom/proc/DblClick    
:   [MouseDown proc (atom)]/atom/proc/MouseDown    
:   [MouseDrag proc (atom)]/atom/proc/MouseDrag    
:   [MouseDrop proc (atom)]/atom/proc/MouseDrop    
:   [MouseEntered proc (atom)]/atom/proc/MouseEntered    
:   [MouseExited proc (client)]/client/proc/MouseExited    
:   [MouseMove proc (atom)]/atom/proc/MouseMove    
:   [MouseUp proc (atom)]/atom/proc/MouseUp    
:   [MouseWheel proc (atom)]/atom/proc/MouseWheel    
:   [mouse_drag_pointer var (atom)]/atom/var/mouse_drag_pointer    
:   [mouse_drop_pointer var (atom)]/atom/var/mouse_drop_pointer    
:   [mouse_opacity var (atom)]/atom/var/mouse_opacity    
:   [mouse_over_pointer var (atom)]/atom/var/mouse_over_pointer    
:   [show_popup_menus var (client)]/client/var/show_popup_menus    
<!-- -->    
**Format:**    
:   MouseExited(location,control,params)    
<!-- -->    
**Args:**    
:   location: the turf, stat panel, grid cell, etc. containing the    
    object    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling]/DM/mouse    
This is called when the mouse moves off of an object with no buttons    
pressed.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. Defining it on only the objects    
that require it reduces overhead.  