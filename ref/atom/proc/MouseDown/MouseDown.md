[]{#/atom/proc/MouseDown}    
## MouseDown proc (atom)    
**See also:**    
:   [Click proc (atom)](/ref/atom/proc/Click/Click.md)    
:   [DblClick proc (atom)](/ref/atom/proc/DblClick/DblClick.md)    
:   [MouseDown proc (client)](/ref/client/proc/MouseDown/MouseDown.md)    
:   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag/MouseDrag.md)    
:   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop/MouseDrop.md)    
:   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered/MouseEntered.md)    
:   [MouseExited proc (atom)](/ref/atom/proc/MouseExited/MouseExited.md)    
:   [MouseMove proc (atom)](/ref/atom/proc/MouseMove/MouseMove.md)    
:   [MouseUp proc (atom)](/ref/atom/proc/MouseUp/MouseUp.md)    
:   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel/MouseWheel.md)    
:   [mouse_drag_pointer var (atom)](/ref/atom/var/mouse_drag_pointer/mouse_drag_pointer.md)    
:   [mouse_drop_pointer var (atom)](/ref/atom/var/mouse_drop_pointer/mouse_drop_pointer.md)    
:   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity/mouse_opacity.md)    
:   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer/mouse_over_pointer.md)    
:   [show_popup_menus var (client)](/ref/client/var/show_popup_menus/show_popup_menus.md)    
<!-- -->    
**Format:**    
:   MouseDown(location,control,params)    
<!-- -->    
**Args:**    
:   location: the turf, stat panel, grid cell, etc. in which the object    
    was clicked    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/ref/DM/mouse/mouse.md)    
This is called when a mouse button is pressed while pointing to this    
object.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. Most operations can be done    
through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures    
are simply available for completeness.    
Note: In BYOND 3.5 this procedure took three different arguments:    
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have    
been replaced, old code will need to be modified. Games compiled before    
this change will still work normally.  