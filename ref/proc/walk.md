
## walk (proc)

**Format:**
+   walk(Ref,Dir,Lag=0,Speed=0)
+   walk(Ref,Vector,Lag=0)

**Arguments:**
+   Ref: A mob or obj.
+   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST, SOUTHEAST,
     SOUTHWEST, or 0 to halt.
+   Lag: Delay in world ticks between movement.
+   Speed: Speed to move, in pixels. 0 uses Ref.step_size.
+   Vector: 2D vector to move by, in pixels.
***
Move Ref in the direction Dir continuously. Each step will be preceded by Lag time of inactivity.

A call to a walking function aborts any previous walking function called on Ref. To halt walking, call walk(Ref,0).

This function returns immediately, but continues to process in the background.

The vector version of this proc will make a copy of the vector, so changing the vector afterward won't have an effect on existing walking.
***
**Related Pages:**
+    [get_step proc](/ref/proc/get_step)
+    [step proc](/ref/proc/step)
+    [step_size var (movable atom)](/ref/atom/movable/var/step_size)
