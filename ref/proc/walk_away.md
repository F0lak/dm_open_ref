## walk_away proc
**See also:**
*   [get_step_away proc](/ref/proc/get_step_away.md) -m
*   [step_away proc](/ref/proc/step_away.md) -m
*   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) -m<!-- -->
**Format:**
*   walk_away(Ref,Trg,Max=5,Lag=0,Speed=0)
<!-- -->
**Args:**
*   Ref* A mob or obj.
*   Trg* An object on the map.
*   Max* The maximum distance between Ref and Targ before movement
    halts.
*   Lag* Delay in world ticks between movement.
*   Speed* Speed to move, in pixels. 0 uses Ref.step_size.


Moves Ref on a path away from Trg continuously, taking
obstacles into account. Each step will be preceded by Lag time of
inactivity. If Ref is farther than Max steps from Trg, no action will be
taken. 

A call to a walking function aborts any previous walking
function called on Ref. To halt walking, call walk(Ref,0). 

This
function returns immediately, but continues to process in the
background.