[]{#/atom/proc/MouseWheel}    
## MouseWheel proc (atom) {#mousewheel-proc-atom byondver="508"}    
**See also:**    
:   [Click proc (atom)](/ref/atom/proc/Click)    
:   [DblClick proc (atom)](/ref/atom/proc/DblClick)    
:   [MouseDown proc (atom)](/ref/atom/proc/MouseDown)    
:   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag)    
:   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop)    
:   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered)    
:   [MouseExited proc (atom)](/ref/atom/proc/MouseExited)    
:   [MouseMove proc (atom)](/ref/atom/proc/MouseMove)    
:   [MouseUp proc (atom)](/ref/atom/proc/MouseUp)    
:   [MouseWheel proc (client)](/ref/client/proc/MouseWheel)    
:   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer)    
:   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer)    
:   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity)    
:   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer)    
<!-- -->    
**Format:**    
:   MouseWheel(delta_x,delta_y,location,control,params)    
<!-- -->    
**Args:**    
:   delta_x,delta_y: amount of wheel movement    
:   location: the turf, stat panel, grid cell, etc. containing the    
    object    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/ref/DM/mouse)    
This is called when the mouse wheel is moved while over an object.    
Positive values of delta_x and delta_y refer to scrolling right or up,    
respectively. Negative values are left and down, respectively.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. Defining it on only the objects    
that require it reduces overhead.  