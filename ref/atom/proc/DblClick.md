[]{#/DblClick proc (atom).md}    
## DblClick proc (atom)    
**See also:**    
:   [Click proc (atom)]/atom/proc/Click    
:   [DblClick proc (client)]/client/proc/DblClick    
:   [MouseDown proc (atom)]/atom/proc/MouseDown    
:   [MouseDrag proc (atom)]/atom/proc/MouseDrag    
:   [MouseDrop proc (atom)]/atom/proc/MouseDrop    
:   [MouseEntered proc (atom)]/atom/proc/MouseEntered    
:   [MouseExited proc (atom)]/atom/proc/MouseExited    
:   [MouseMove proc (atom)]/atom/proc/MouseMove    
:   [MouseUp proc (atom)]/atom/proc/MouseUp    
:   [MouseWheel proc (atom)]/atom/proc/MouseWheel    
:   [show_popup_menus var (client)]/client/var/show_popup_menus    
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
    offsets, etc.; see [mouse handling]/DM/mouse    
This proc is called by the default client.DblClick() procedure.    
This example allows the player to teleport to a position by double    
clicking it.    
### Example:    
turf/DblClick() usr.Move(src)  