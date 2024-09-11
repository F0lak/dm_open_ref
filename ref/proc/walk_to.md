## walk_to proc
**See also:**
*   [get_step_to proc](/ref/proc/get_step_to.md) -m
*   [step_to proc](/ref/proc/step_to.md) -m
*   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) -m<!-- -->
**Format:**
*   walk_to(Ref,Trg,Min=0,Lag=0,Speed=0)
<!-- -->
**Args:**
*   Ref* A mob or obj.
*   Trg* An object on the map.
*   Min* The minimum distance between Ref and Trg before movement halts.
*   Lag* Delay in world ticks between movement.
*   Speed* Speed to move, in pixels. 0 uses Ref.step_size.


Move Ref on a path to Trg continuously, taking obstacles into
account. Each step will be preceded by Lag time of inactivity. If Ref is
within Min steps of Trg, no action will be taken. This is also true if
the target is too far away (more than twice world.view steps).


A call to a walking function aborts any previous walking
function called on Ref. To halt walking, call walk(Ref,0). 

This
function returns immediately, but continues to process in the
background.