[]{#/atom/proc/DblClick}    
## DblClick proc (atom)    
**See also:**    
:   [Click proc (atom)](/ref/atom/proc/Click/Click.md)    
:   [DblClick proc (client)](/ref/client/proc/DblClick/DblClick.md)    
:   [MouseDown proc (atom)](/ref/atom/proc/MouseDown/MouseDown.md)    
:   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag/MouseDrag.md)    
:   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop/MouseDrop.md)    
:   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered/MouseEntered.md)    
:   [MouseExited proc (atom)](/ref/atom/proc/MouseExited/MouseExited.md)    
:   [MouseMove proc (atom)](/ref/atom/proc/MouseMove/MouseMove.md)    
:   [MouseUp proc (atom)](/ref/atom/proc/MouseUp/MouseUp.md)    
:   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel/MouseWheel.md)    
:   [show_popup_menus var (client)](/ref/client/var/show_popup_menus/show_popup_menus.md)    
<!-- -->    
**Format:**    
:   DblClick(location,control,params)    
<!-- -->    
**When:**    
:   Called when the object is double-clicked.    
<!-- -->    
**Args:**    
:   location: the turf, stat panel, grid cell, etc. in which the object    
    was double-clicked    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/ref/DM/mouse/mouse.md)    
This proc is called by the default client.DblClick() procedure.    
This example allows the player to teleport to a position by double    
clicking it.    
### Example:    
turf/DblClick() usr.Move(src)  