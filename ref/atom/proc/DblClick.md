
## DblClick (proc)

**Format:**
+   DblClick(location,control,params)

**Arguments:**
+   location: the turf, stat panel, grid cell, etc. in which the object was double-clicked
+   control: the name of the skin control involved
+   params: other parameters including mouse/keyboard flags, icon offsets, etc.; see [mouse handling](/ref/DM/mouse)

**Called When:**
+   Called when the object is double-clicked.
***
This proc is called by the default client.DblClick() procedure.

This example allows the player to teleport to a position by double clicking it.


```dm

turf/DblClick()
  usr.Move(src)

```

***
**Related Pages:**
+    [Click](/ref/atom/proc/Click)
+    [DblClick proc (client)](/ref/client/proc/DblClick)
+    [MouseDown](/ref/atom/proc/MouseDown)
+    [MouseDrag](/ref/atom/proc/MouseDrag)
+    [MouseDrop](/ref/atom/proc/MouseDrop)
+    [MouseEntered](/ref/atom/proc/MouseEntered)
+    [MouseExited](/ref/atom/proc/MouseExited)
+    [MouseMove](/ref/atom/proc/MouseMove)
+    [MouseUp](/ref/atom/proc/MouseUp)
+    [MouseWheel](/ref/atom/proc/MouseWheel)
+    [show_popup_menus var](/ref/client/var/show_popup_menus)
