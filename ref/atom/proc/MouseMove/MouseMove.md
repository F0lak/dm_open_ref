[]{#/atom/proc/MouseMove}
  ## MouseMove proc (atom) {#mousemove-proc-atom byondver="500"}
  **See also:**
  :   [Click proc (atom)](ref/atom/proc/Click)
  :   [DblClick proc (atom)](ref/atom/proc/DblClick)
  :   [MouseDown proc (atom)](ref/atom/proc/MouseDown)
  :   [MouseDrag proc (atom)](ref/atom/proc/MouseDrag)
  :   [MouseDrop proc (atom)](ref/atom/proc/MouseDrop)
  :   [MouseEntered proc (atom)](ref/atom/proc/MouseEntered)
  :   [MouseExited proc (atom)](ref/atom/proc/MouseExited)
  :   [MouseMove proc (client)](ref/client/proc/MouseMove)
  :   [MouseUp proc (atom)](ref/atom/proc/MouseUp)
  :   [MouseWheel proc (atom)](ref/atom/proc/MouseWheel)
  :   [mouse_drag_pointer var (atom)](ref/atom/var/mouse_drag_pointer)
  :   [mouse_drop_pointer var (atom)](ref/atom/var/mouse_drop_pointer)
  :   [mouse_opacity var (atom)](ref/atom/var/mouse_opacity)
  :   [mouse_over_pointer var (atom)](ref/atom/var/mouse_over_pointer)
  :   [show_popup_menus var (client)](ref/client/var/show_popup_menus)
  <!-- -->
  **Format:**
  :   MouseMove(location,control,params)
  <!-- -->
  **Args:**
  :   location: the turf, stat panel, grid cell, etc. containing the
      object
  :   control: the name of the skin control involved
  :   params: other parameters including mouse/keyboard flags, icon
      offsets, etc.; see [mouse handling](ref/DM/mouse)
  This is called when the mouse moves over the object with no buttons
  pressed. When the mouse moves over for the first time, MouseEntered() is
  called instead.
  Don\'t define this unless you need it, because it generates extra
  communication that is otherwise avoided. Defining it on only the objects
  that require it reduces overhead.