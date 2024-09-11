## Click proc (client)
**See also:**
*   [Click proc (atom)](/atom/proc/Click)
*   [DblClick proc (client)](/client/proc/DblClick)
*   [MouseDown proc (client)](/client/proc/MouseDown)
*   [MouseDrag proc (client)](/client/proc/MouseDrag)
*   [MouseDrop proc (client)](/client/proc/MouseDrop)
*   [MouseEntered proc (client)](/client/proc/MouseEntered)
*   [MouseExited proc (client)](/client/proc/MouseExited)
*   [MouseMove proc (client)](/client/proc/MouseMove)
*   [MouseUp proc (client)](/client/proc/MouseUp)
*   [MouseWheel proc (client)](/client/proc/MouseWheel)
*   [mouse_opacity var (atom)](/atom/var/mouse_opacity)
*   [mouse_over_pointer var (atom)](/atom/var/mouse_over_pointer)
*   [show_popup_menus var (client)](/client/var/show_popup_menus)
<!-- -->
**Format:**
*   Click(object,location,control,params)
<!-- -->
**When:**
*   Called when the player clicks on the map or in the stat panels.
<!-- -->
**Args:**
*   object* the object clicked
*   location* the client stat panel, location (turf) of object on map,
    grid cell, or other control-specific info
*   control* the name of the skin control involved
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/DM/mouse)
<!-- -->
**Default action:**
*   Call object.Click(location,control,params).
### Example:

```
 client Click(O) usr \<\< \"You clicked \[O\]\" ..() // do
default action 
```
 

Note that due to network lag, it is
possible when clicking on moving objects for the location of those
objects to have changed by the time the Click() proc is executed. That
is the reason for the location argument. It tells you where the click
originally took place. 

The argument format for this verb is:

```
 Click(object as null\|atom in usr.client,\\ location as
null\|turf\|text in usr.client,\\ control as text, params as text)

```
