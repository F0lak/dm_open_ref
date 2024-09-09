[]{#/client/proc/MouseUp}    
## MouseUp proc (client)    
**See also:**    
:   [Click proc (client)](/ref/client/proc/Click/Click.md)    
:   [DblClick proc (client)](/ref/client/proc/DblClick/DblClick.md)    
:   [MouseDown proc (client)](/ref/client/proc/MouseDown/MouseDown.md)    
:   [MouseDrag proc (client)](/ref/client/proc/MouseDrag/MouseDrag.md)    
:   [MouseDrop proc (client)](/ref/client/proc/MouseDrop/MouseDrop.md)    
:   [MouseEntered proc (client)](/ref/client/proc/MouseEntered/MouseEntered.md)    
:   [MouseExited proc (client)](/ref/client/proc/MouseExited/MouseExited.md)    
:   [MouseMove proc (client)](/ref/client/proc/MouseMove/MouseMove.md)    
:   [MouseUp proc (atom)](/ref/atom/proc/MouseUp/MouseUp.md)    
:   [MouseWheel proc (client)](/ref/client/proc/MouseWheel/MouseWheel.md)    
:   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity/mouse_opacity.md)    
:   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon/mouse_pointer_icon.md)    
:   [show_popup_menus var (client)](/ref/client/var/show_popup_menus/show_popup_menus.md)    
<!-- -->    
**Format:**    
:   MouseUp(object,location,control,params)    
<!-- -->    
**Args:**    
:   object: the object under the mouse pointer    
:   location: the turf, stat panel, grid cell, etc. containing the    
    object where it was clicked    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/ref/DM/mouse/mouse.md)    
<!-- -->    
**Default action:**    
:   Call object.MouseUp(location,control,params).    
This is called when a mouse button is released while pointing to an    
object.    
Don\'t define this unless you need it, because it generates extra    
communication that is otherwise avoided. Most operations can be done    
through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures    
are simply available for completeness.    
The argument format for this verb is: MouseUp(object as null\|atom in    
usr.client,\\ location as null\|turf\|text in usr.client,\\ control as    
text, params as text)    
Note: In BYOND 3.5 this procedure took three different arguments:    
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have    
been replaced, old code will need to be modified. Games compiled before    
this change will still work normally.  