## MouseDrag proc (client)
**See also:**
*   [Click proc (client)](/client/proc/Click)
*   [DblClick proc (client)](/client/proc/DblClick)
*   [MouseDown proc (client)](/client/proc/MouseDown)
*   [MouseDrag proc (atom)](/atom/proc/MouseDrag)
*   [MouseDrop proc (client)](/client/proc/MouseDrop)
*   [MouseEntered proc (client)](/client/proc/MouseEntered)
*   [MouseExited proc (client)](/client/proc/MouseExited)
*   [MouseMove proc (client)](/client/proc/MouseMove)
*   [MouseUp proc (client)](/client/proc/MouseUp)
*   [MouseWheel proc (client)](/client/proc/MouseWheel)
*   [mouse_pointer_icon var (client)](/client/var/mouse_pointer_icon)
*   [show_popup_menus var (client)](/client/var/show_popup_menus)
<!-- -->
**Format:**
*   MouseDrag(src_object,over_object,src_location,over_location,src_control,over_control,params)
<!-- -->
**Args:**
*   src_object* the object being dragged
*   over_object* the object under the mouse pointer
*   src_location* the turf, stat panel, grid cell, etc. from where the
    src object was dragged
*   over_location* the turf, stat panel, grid cell, etc. containing the
    object under the mouse pointer
*   src_control* The id of the skin control the object was dragged from
*   over_control* The id of the skin control the object was dragged over
*   params* other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/DM/mouse)
<!-- -->
**Default action:**
*   Call
    object.MouseDrag(over_object,src_location,over_location,src_control,over_control,params).


This is called while dragging an object by pressing and holding
the left mouse button over the object and moving the mouse. The
over_object may be null if dragging over a stat panel or over other
empty space. 

Don\'t define this unless you need it, because it
generates extra communication that is otherwise avoided. Most operations
can be done through Click(), DblClick(), and MouseDrop(). The other
procedures are simply available for completeness. 

The argument
format for this verb is* 
```
 MouseDrag(src_object as null\|atom
in usr.client,\\ over_object as null\|atom in usr.client,\\ src_location
as null\|turf\|text in usr.client,\\ over_location as null\|turf\|text
in usr.client,\\ src_control as text, over_control as text, params as
text) 
```
