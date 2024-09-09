[]{#/proc/walk_towards}
  ## walk_towards proc
  **See also:**
  :   [get_step_towards proc](ref/proc/get_step_towards)
  :   [step_towards proc](ref/proc/step_towards)
  :   [step_size var (movable atom)](ref/atom/movable/var/step_size)
  <!-- -->
  **Format:**
  :   walk_towards(Ref,Trg,Lag=0,Speed=0)
  <!-- -->
  **Args:**
  :   Ref: A mob or obj.
  :   Trg: An object on the map.
  :   Lag: Delay in world ticks between movement.
  :   Speed: Speed to move, in pixels. 0 uses Ref.step_size.
  Move Ref in the direction of Trg continuously. Each step will be
  preceded by Lag time of inactivity.
  A call to a walking function aborts any previous walking function called
  on Ref. To halt walking, call walk(Ref,0).
  This function returns immediately, but continues to process in the
  background.