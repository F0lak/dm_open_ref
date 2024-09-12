## Click proc (atom)
**See also:**
+   [Click proc (client)](/ref/client/proc/Click.md) 
+   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) 
+   [MouseDown proc (atom)](/ref/atom/proc/MouseDown.md) 
+   [MouseDrag proc (atom)](/ref/atom/proc/MouseDrag.md) 
+   [MouseDrop proc (atom)](/ref/atom/proc/MouseDrop.md) 
+   [MouseEntered proc (atom)](/ref/atom/proc/MouseEntered.md) 
+   [MouseExited proc (atom)](/ref/atom/proc/MouseExited.md) 
+   [MouseMove proc (atom)](/ref/atom/proc/MouseMove.md) 
+   [MouseUp proc (atom)](/ref/atom/proc/MouseUp.md) 
+   [MouseWheel proc (atom)](/ref/atom/proc/MouseWheel.md) 
+   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) 
<!-- -->
**Format:**
+   Click(location,control,params)
<!-- -->
**When:**
+   Called when the object is clicked.
<!-- -->
**Args:**
+   location+ the turf, stat panel, grid cell, etc. in which the object
    was clicked
+   control+ the name of the skin control involved
+   params+ other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) 

This proc is called by the default client.Click() procedure.


The following example allows the player to walk to a position
by clicking it.
### Example:

```
 turf/Click() walk_to(usr,src) 
```
