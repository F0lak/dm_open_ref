[]{#/proc/step_towards}
  ## step_towards proc
  **See also:**
  :   [get_step_towards proc](ref/proc/get_step_towards)
  :   [walk_towards proc](ref/proc/walk_towards)
  :   [step_size var (movable atom)](ref/atom/movable/var/step_size)
  <!-- -->
  **Format:**
  :   step_towards(Ref,Trg,Speed)
  <!-- -->
  **Returns:**
  :   1 on success; 0 otherwise.
  <!-- -->
  **Args:**
  :   Ref: A mob or obj.
  :   Trg: An object on the map.
  :   Speed: Speed to move, in pixels. 0 uses Ref.step_size.
  Move Ref in the direction of the location Trg.