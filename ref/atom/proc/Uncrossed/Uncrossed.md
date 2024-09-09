[]{#/atom/proc/Uncrossed}
  ## Uncrossed proc (atom) {#uncrossed-proc-atom byondver="490"}
  **See also:**
  :   [Enter proc (atom)](ref/atom/proc/Enter)
  :   [Entered proc (atom)](ref/atom/proc/Entered)
  :   [Exit proc (atom)](ref/atom/proc/Exit)
  :   [Exited proc (atom)](ref/atom/proc/Exited)
  :   [Cross proc (atom)](ref/atom/proc/Cross)
  :   [Crossed proc (atom)](ref/atom/proc/Crossed)
  :   [Uncross proc (atom)](ref/atom/proc/Uncross)
  :   [Move proc (movable atom)](ref/atom/movable/proc/Move)
  :   [group var (mob)](ref/mob/var/group)
  :   [Pixel movement](ref/%7Bnotes%7D/pixel-movement)
  <!-- -->
  **Format:**
  :   Uncrossed(atom/movable/O)
  <!-- -->
  **When:**
  :   Called when an object has stopped overlapping this one through a
      call to Move(). Directly setting the object\'s loc or step_x/y vars
      does not result in a call to Uncrossed() or any other movement
      side-effects. The same goes for deletion of an object.
  <!-- -->
  **Args:**
  :   O: the object that moved and is no longer overlapping.
  <!-- -->
  **Default action:**
  :   none
  ### Example:
  obj/pressure_plate Uncrossed(O) // if no other mobs are standing on
  it\... if(!(locate(/mob) in bounds())) // do something Release()