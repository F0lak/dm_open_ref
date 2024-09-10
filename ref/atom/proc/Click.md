[]{#/Click proc (atom).md}    
## Click proc (atom)    
**See also:**    
:   [Click proc (client)](/client/proc/Click)    
:   [DblClick proc (atom)](/atom/proc/DblClick)    
:   [MouseDown proc (atom)](/atom/proc/MouseDown)    
:   [MouseDrag proc (atom)](/atom/proc/MouseDrag)    
:   [MouseDrop proc (atom)](/atom/proc/MouseDrop)    
:   [MouseEntered proc (atom)](/atom/proc/MouseEntered)    
:   [MouseExited proc (atom)](/atom/proc/MouseExited)    
:   [MouseMove proc (atom)](/atom/proc/MouseMove)    
:   [MouseUp proc (atom)](/atom/proc/MouseUp)    
:   [MouseWheel proc (atom)](/atom/proc/MouseWheel)    
:   [show_popup_menus var (client)](/client/var/show_popup_menus)    
<!-- -->    
**Format:**    
:   Click(location,control,params)    
<!-- -->    
**When:**    
:   Called when the object is clicked.    
<!-- -->    
**Args:**    
:   location: the turf, stat panel, grid cell, etc. in which the object    
    was clicked    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling](/DM/mouse)    
This proc is called by the default client.Click() procedure.    
The following example allows the player to walk to a position by    
clicking it.    
### Example:    
turf/Click() walk_to(usr,src)  