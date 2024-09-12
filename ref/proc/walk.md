## walk proc

**Format:**
+   walk(Ref,Dir,Lag=0,Speed=0)
<!-- -->
**Args:**
+   Ref: A mob or obj.
+   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST,
    SOUTHEAST, SOUTHWEST, or 0 to halt.
+   Lag: Delay in world ticks between movement.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.


Move Ref in the direction Dir continuously. Each step will be
preceded by Lag time of inactivity. 

A call to a walking
function aborts any previous walking function called on Ref. To halt
walking, call walk(Ref,0). 

This function returns immediately,
but continues to process in the background.

**See also:**
+   [get_step proc](/ref/proc/get_step.md) 
+   [step proc](/ref/proc/step.md) 
+   [step_size var (movable atom)](/ref/atom/movable/var/step_size.md) <!-- -->