[]{#/atom/proc/Exited}
  ## Exited proc (atom)
  **See also:**
  :   [Enter proc (atom)](ref/atom/proc/Enter)
  :   [Entered proc (atom)](ref/atom/proc/Entered)
  :   [Exit proc (atom)](ref/atom/proc/Exit)
  :   [Cross proc (atom)](ref/atom/proc/Cross)
  :   [Crossed proc (atom)](ref/atom/proc/Crossed)
  :   [Uncross proc (atom)](ref/atom/proc/Uncross)
  :   [Uncrossed proc (atom)](ref/atom/proc/Uncrossed)
  :   [Move proc (movable atom)](ref/atom/movable/proc/Move)
  <!-- -->
  **Format:**
  :   Exited(atom/movable/Obj, atom/newloc)
  <!-- -->
  **When:**
  :   Called when an object has exited from the contents list through a
      call to Move(). Directly setting the object\'s loc or step_x/y vars
      does not result in a call to Exited() or any other movement
      side-effects. The same goes for deletion of an object.
  <!-- -->
  **Args:**
  :   Obj: the object that exited (a mob or obj).
  :   [newloc]{byondver="507"}: the object\'s new location.
  <!-- -->
  **Default action:**
  :   None for most atoms, but turfs will call Uncrossed().