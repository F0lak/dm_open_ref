[]{#/client/proc/MouseWheel}    
## MouseWheel proc (client) {#mousewheel-proc-client byondver="508"}    
**See also:**    
:   [Click proc (client)](/ref/client/proc/Click/Click.md)    
:   [DblClick proc (client)](/ref/client/proc/DblClick/DblClick.md)    
:   [MouseDown proc (client)](/ref/client/proc/MouseDown/MouseDown.md)    
:   [MouseDrag proc (client)](/ref/client/proc/MouseDrag/MouseDrag.md)    
:   [MouseDrop proc (client)](/ref/client/proc/MouseDrop/MouseDrop.md)    
:   [MouseEntered proc (client)](/ref/client/proc/MouseEntered/MouseEntered.md)    
:   [MouseExited proc (client)](/ref/client/proc/MouseExited/MouseExited.md)    
:   [MouseMove proc (client)](/ref/client/proc/MouseMove/MouseMove.md)    
:   [MouseUp proc (client)](/ref/client/proc/MouseUp/MouseUp.md)    
:   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel/MouseWheel.md)    
:   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity/mouse_opacity.md)    
:   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon/mouse_pointer_icon.md)    
<!-- -->    
**Format:**    
:   MouseWheel(object,delta_x,delta_y,location,control,params)    
<!-- -->    
**Args:**    
:   object: the object under the mouse pointer    
:   delta_x,delta_y: amount of wheel movement    
:   location: the turf, stat panel, grid cell, etc. containing the    
    object    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/ref/DM/mouse/mouse.md)    
<!-- -->    
**Default action:**    
:   Call object.MouseWheel(delta_x,delta_y,location,control,params).    
This is called when the mouse wheel is moved while over an object or    
control. It is NOT called if over a browser control, or any control that    
is currently scrollable.    
Positive values of delta_x and delta_y refer to scrolling right or up,    
respectively. Negative values are left and down, respectively.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. If you only need wheel support    
on specific objects, use atom.MouseWheel() instead which is more    
selective.    
The argument format for this verb is: MouseWheel(object as null\|atom in    
usr.client,\\ delta_x as num, delta_y as num,\\ location as    
null\|turf\|text in usr.client,\\ control as text, params as text)  