## DblClick proc (client)
**See also:**
*   [Click proc (client)](/ref/client/proc/Click.md) -m
*   [DblClick proc (atom)](/ref/atom/proc/DblClick.md) -m
*   [MouseDown proc (client)](/ref/client/proc/MouseDown.md) -m
*   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) -m
*   [MouseDrop proc (client)](/ref/client/proc/MouseDrop.md) -m
*   [MouseEntered proc (client)](/ref/client/proc/MouseEntered.md) -m
*   [MouseExited proc (client)](/ref/client/proc/MouseExited.md) -m
*   [MouseMove proc (client)](/ref/client/proc/MouseMove.md) -m
*   [MouseUp proc (client)](/ref/client/proc/MouseUp.md) -m
*   [MouseWheel proc (client)](/ref/client/proc/MouseWheel.md) -m
*   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) -m
*   [mouse_over_pointer var (atom)](/ref/atom/var/mouse_over_pointer.md) -m
*   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) -m
<!-- -->
**Format:**
*   DblClick(object,location,control,params)
<!-- -->
**When:**
*   Called when the player double-clicks on the map or in the stat
    panels.
<!-- -->
**Args:**
*   object* the object double-clicked
*   location* the client stat panel, location (turf) of object on map,
    grid cell, or other control-specific info
*   control* the name of the skin control involved
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) -m<!-- -->
**Default action:**
*   Call object.DblClick(location,control,params).
### Example:

```
 client DblClick(O) usr \<\< \"You double-clicked \[O\]\" ..()
// do default action 
```
 

Note that due to network lag,
it is possible when clicking on moving objects for the location of those
objects to have changed by the time the DblClick() proc is executed.
That is the reason for the location argument. It tells you where the
click originally took place. 
```
 DblClick(object as null\|atom in
usr.client,\\ location as null\|turf\|text in usr.client,\\ control as
text, params as text) 
```
