
## Click (proc)

**Format:**
+   Click(object,location,control,params)

**Arguments:**
+   object: the object clicked
+   location: the client stat panel, location (turf) of object on map, grid cell, or other control-specific info
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)

**Called When:**
+   Called when the player clicks on the map or in the stat panels.

**Default Action:**
+   Call object.Click(location,control,params).
***

```dm

client
  Click(O)
    usr << "You clicked [O]"
    ..() // do default action

```


Note that due to network lag, it is possible when clicking on moving objects for the location of those objects to have changed by the time the Click() proc is executed. That is the reason for the location argument. It tells you where the click originally took place.

The argument format for this verb is:


```dm

Click(object as null|atom in usr.client,\
      location as null|turf|text in usr.client,\
      control as text, params as text)

```

***
**Related Pages:**
+    [Click](/ref/atom/proc/Click)
+    [DblClick proc (client)](/ref/client/proc/DblClick)
+    [MouseDown proc (client)](/ref/client/proc/MouseDown)
+    [MouseDrag proc (client)](/ref/client/proc/MouseDrag)
+    [MouseDrop proc (client)](/ref/client/proc/MouseDrop)
+    [MouseEntered proc (client)](/ref/client/proc/MouseEntered)
+    [MouseExited proc (client)](/ref/client/proc/MouseExited)
+    [MouseMove proc (client)](/ref/client/proc/MouseMove)
+    [MouseUp proc (client)](/ref/client/proc/MouseUp)
+    [MouseWheel proc (client)](/ref/client/proc/MouseWheel)
+    [mouse_opacity var](/ref/atom/var/mouse_opacity)
+    [mouse_over_pointer](/ref/atom/var/mouse_over_pointer)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
