
## Click (proc)

**Format:**
+   Click(location,control,params)

**Arguments:**
+   location: the turf, stat panel, grid cell, etc. in which the object was clicked
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)

**Called When:**
+   Called when the object is clicked.
***
This proc is called by the default client.Click() procedure.

The following example allows the player to walk to a position by clicking it.


```dm

turf/Click()
  walk_to(usr,src)

```

***
**Related Pages:**
+    [Click proc (client)](/ref/client/proc/Click)
+    [DblClick](/ref/atom/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop](/ref/atom/proc/MouseDrop)
+    [MouseEntered](/ref/atom/proc/MouseEntered)
+    [MouseExited](/ref/atom/proc/MouseExited)
+    [MouseMove](/ref/atom/proc/MouseMove)
+    [MouseUp](/ref/atom/proc/MouseUp)
+    [MouseWheel](/ref/atom/proc/MouseWheel)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
