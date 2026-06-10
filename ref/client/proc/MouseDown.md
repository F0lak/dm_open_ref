
## MouseDown (proc)

**Format:**
+   MouseDown(object,location,control,params)

**Arguments:**
+   object: the object under the mouse pointer
+   location: the turf, stat panel, grid cell, etc. containing the object where it was clicked
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)

**Default Action:**
+   Call object.MouseDown(location,control,params).
***
This is called when the a mouse button is pressed while pointing to the object. Note that MouseUp() will always be called after MouseDown() is called, even if over empty space. That means `object` and `location` may be null.

Don't define this unless you need it, because it generates extra communication that is otherwise avoided. Most operations can be done through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures are simply available for completeness.

The argument format for this verb is:


```dm

MouseDown(object as null|atom in usr.client,\
          location as null|turf|text in usr.client,\
          control as text, params as text)

```



> [!TIP]
> Note: In BYOND 3.5 this procedure took three different arguments: `location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have been replaced, old code will need to be modified. Games compiled before this change will still work normally.
***
**Related Pages:**
+    [Click proc (client)](/ref/client/proc/Click)
+    [DblClick proc (client)](/ref/client/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag proc (client)](/ref/client/proc/MouseDrag)
+    [MouseDrop proc (client)](/ref/client/proc/MouseDrop)
+    [MouseEntered proc (client)](/ref/client/proc/MouseEntered)
+    [MouseExited proc (client)](/ref/client/proc/MouseExited)
+    [MouseMove proc (client)](/ref/client/proc/MouseMove)
+    [MouseUp proc (client)](/ref/client/proc/MouseUp)
+    [MouseWheel proc (client)](/ref/client/proc/MouseWheel)
+    [mouse_opacity var](/ref/atom/var/mouse_opacity)
+    [mouse_pointer_icon](/ref/client/var/mouse_pointer_icon)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
