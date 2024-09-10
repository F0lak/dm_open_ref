[]{#/DblClick proc (client).md}    
## DblClick proc (client)    
**See also:**    
:   [Click proc (client)]/client/proc/Click    
:   [DblClick proc (atom)]/atom/proc/DblClick    
:   [MouseDown proc (client)]/client/proc/MouseDown    
:   [MouseDrag proc (client)]/client/proc/MouseDrag    
:   [MouseDrop proc (client)]/client/proc/MouseDrop    
:   [MouseEntered proc (client)]/client/proc/MouseEntered    
:   [MouseExited proc (client)]/client/proc/MouseExited    
:   [MouseMove proc (client)]/client/proc/MouseMove    
:   [MouseUp proc (client)]/client/proc/MouseUp    
:   [MouseWheel proc (client)]/client/proc/MouseWheel    
:   [mouse_opacity var (atom)]/atom/var/mouse_opacity    
:   [mouse_over_pointer var (atom)]/atom/var/mouse_over_pointer    
:   [show_popup_menus var (client)]/client/var/show_popup_menus    
<!-- -->    
**Format:**    
:   DblClick(object,location,control,params)    
<!-- -->    
**When:**    
:   Called when the player double-clicks on the map or in the stat    
    panels.    
<!-- -->    
**Args:**    
:   object: the object double-clicked    
:   location: the client stat panel, location (turf) of object on map,    
    grid cell, or other control-specific info    
:   control: the name of the skin control involved    
:   params: other parameters including mouse/keyboard flags, icon    
    offsets, etc.; see [mouse handling]/DM/mouse    
<!-- -->    
**Default action:**    
:   Call object.DblClick(location,control,params).    
### Example:    
client DblClick(O) usr \<\< \"You double-clicked \[O\]\" ..() // do    
default action    
Note that due to network lag, it is possible when clicking on moving    
objects for the location of those objects to have changed by the time    
the DblClick() proc is executed. That is the reason for the location    
argument. It tells you where the click originally took place.    
DblClick(object as null\|atom in usr.client,\\ location as    
null\|turf\|text in usr.client,\\ control as text, params as text)  