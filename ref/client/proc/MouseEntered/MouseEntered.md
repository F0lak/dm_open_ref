[]{#/client/proc/MouseEntered}
  ## MouseEntered proc (client)
  **See also:**
  :   [Click proc (client)](ref/client/proc/Click)
  :   [DblClick proc (client)](ref/client/proc/DblClick)
  :   [MouseDrag proc (client)](ref/client/proc/MouseDrag)
  :   [MouseDrop proc (client)](ref/client/proc/MouseDrop)
  :   [MouseEntered proc (atom)](ref/atom/proc/MouseEntered)
  :   [MouseExited proc (client)](ref/client/proc/MouseExited)
  :   [MouseMove proc (client)](ref/client/proc/MouseMove)
  :   [MouseUp proc (client)](ref/client/proc/MouseUp)
  :   [MouseWheel proc (client)](ref/client/proc/MouseWheel)
  :   [mouse_opacity var (atom)](ref/atom/var/mouse_opacity)
  :   [mouse_pointer_icon var (client)](ref/client/var/mouse_pointer_icon)
  :   [show_popup_menus var (client)](ref/client/var/show_popup_menus)
  <!-- -->
  **Format:**
  :   MouseEntered(object,location,control,params)
  <!-- -->
  **Args:**
  :   object: the object under the mouse pointer
  :   location: the turf, stat panel, grid cell, etc. containing the
      object where it was clicked
  :   control: the name of the skin control involved
  :   params: other parameters including mouse/keyboard flags, icon
      offsets, etc.; see [mouse handling](ref/DM/mouse)
  <!-- -->
  **Default action:**
  :   Call object.MouseEntered(location,control,params).
  This is called when no mouse buttons are pressed while pointing to the
  object.
  Don\'t define this unless you need it, because it generates extra
  communication that is otherwise avoided. Defining it on only the objects
  that require it reduces overhead.
  The argument format for this verb is: MouseEntered(object as null\|atom
  in usr.client,\\ location as null\|turf\|text in usr.client,\\ control
  as text, params as text)