## MouseExited proc (client)
**See also:**
+   [Click proc (client)](/ref/client/proc/Click.md) 
+   [DblClick proc (client)](/ref/client/proc/DblClick.md) 
+   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) 
+   [MouseDrop proc (client)](/ref/client/proc/MouseDrop.md) 
+   [MouseEntered proc (client)](/ref/client/proc/MouseEntered.md) 
+   [MouseExited proc (atom)](/ref/atom/proc/MouseExited.md) 
+   [MouseMove proc (client)](/ref/client/proc/MouseMove.md) 
+   [MouseUp proc (client)](/ref/client/proc/MouseUp.md) 
+   [MouseWheel proc (client)](/ref/client/proc/MouseWheel.md) 
+   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) 
+   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon.md) 
+   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) 
<!-- -->
**Format:**
+   MouseExited(object,location,control,params)
<!-- -->
**Args:**
+   object: the object under the mouse pointer
+   location: the turf, stat panel, grid cell, etc. containing the
    object where it was clicked
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) <!-- -->
**Default action:**
+   Call object.MouseExited(location,control,params).


This is called when the mouse moves off of an object.


Don\'t define this unless you need it, because it generates
extra communication that is otherwise avoided. Defining it on only the
objects that require it reduces overhead. 

The argument format
for this verb is: 
```
 MouseExited(object as null\|atom in
usr.client,\\ location as null\|turf\|text in usr.client,\\ control as
text, params as text) 
```
