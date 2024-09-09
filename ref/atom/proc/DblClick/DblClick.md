[]{#/atom/proc/DblClick}
  ## DblClick proc (atom)
  **See also:**
  :   [Click proc (atom)](ref/atom/proc/Click)
  :   [DblClick proc (client)](ref/client/proc/DblClick)
  :   [MouseDown proc (atom)](ref/atom/proc/MouseDown)
  :   [MouseDrag proc (atom)](ref/atom/proc/MouseDrag)
  :   [MouseDrop proc (atom)](ref/atom/proc/MouseDrop)
  :   [MouseEntered proc (atom)](ref/atom/proc/MouseEntered)
  :   [MouseExited proc (atom)](ref/atom/proc/MouseExited)
  :   [MouseMove proc (atom)](ref/atom/proc/MouseMove)
  :   [MouseUp proc (atom)](ref/atom/proc/MouseUp)
  :   [MouseWheel proc (atom)](ref/atom/proc/MouseWheel)
  :   [show_popup_menus var (client)](ref/client/var/show_popup_menus)
  <!-- -->
  **Format:**
  :   DblClick(location,control,params)
  <!-- -->
  **When:**
  :   Called when the object is double-clicked.
  <!-- -->
  **Args:**
  :   location: the turf, stat panel, grid cell, etc. in which the object
      was double-clicked
  :   control: the name of the skin control involved
  :   params: other parameters including mouse/keyboard flags, icon
      offsets, etc.; see [mouse handling](ref/DM/mouse)
  This proc is called by the default client.DblClick() procedure.
  This example allows the player to teleport to a position by double
  clicking it.
  ### Example:
  turf/DblClick() usr.Move(src)