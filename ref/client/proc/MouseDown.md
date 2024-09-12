## MouseDown proc (client)
**See also:**
+   [Click proc (client)](/ref/client/proc/Click.md) 
+   [DblClick proc (client)](/ref/client/proc/DblClick.md) 
+   [MouseDown proc (atom)](/ref/atom/proc/MouseDown.md) 
+   [MouseDrag proc (client)](/ref/client/proc/MouseDrag.md) 
+   [MouseDrop proc (client)](/ref/client/proc/MouseDrop.md) 
+   [MouseEntered proc (client)](/ref/client/proc/MouseEntered.md) 
+   [MouseExited proc (client)](/ref/client/proc/MouseExited.md) 
+   [MouseMove proc (client)](/ref/client/proc/MouseMove.md) 
+   [MouseUp proc (client)](/ref/client/proc/MouseUp.md) 
+   [MouseWheel proc (client)](/ref/client/proc/MouseWheel.md) 
+   [mouse_opacity var (atom)](/ref/atom/var/mouse_opacity.md) 
+   [mouse_pointer_icon var (client)](/ref/client/var/mouse_pointer_icon.md) 
+   [show_popup_menus var (client)](/ref/client/var/show_popup_menus.md) 
<!-- -->
**Format:**
+   MouseDown(object,location,control,params)
<!-- -->
**Args:**
+   object+ the object under the mouse pointer
+   location+ the turf, stat panel, grid cell, etc. containing the
    object where it was clicked
+   control+ the name of the skin control involved
+   params+ other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](/ref/DM/mouse.md) <!-- -->
**Default action:**
+   Call object.MouseDown(location,control,params).


This is called when the a mouse button is pressed while
pointing to the object. Note that MouseUp() will always be called after
MouseDown() is called, even if over empty space. That means
`object`{.variable} and `location`{.variable} may be null.


Don\'t define this unless you need it, because it generates
extra communication that is otherwise avoided. Most operations can be
done through `Click()`, `DblClick()`, and `MouseDrop()`. The other
procedures are simply available for completeness. 

The argument
format for this verb is+ 
```
 MouseDown(object as null\|atom in
usr.client,\\ location as null\|turf\|text in usr.client,\\ control as
text, params as text) 
```

Note+ In BYOND 3.5 this procedure took three different arguments:
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have
been replaced, old code will need to be modified. Games compiled before
this change will still work normally.