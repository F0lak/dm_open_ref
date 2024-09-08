[]{#/proc/step}
## step proc
**See also:**
:   [get_step proc](#/proc/get_step)
:   [walk proc](#/proc/walk)
:   [step_size var (movable atom)](#/atom/movable/var/step_size)
<!-- -->
**Format:**
:   step(Ref,Dir,Speed=0)
<!-- -->
**Returns:**
:   1 on success; 0 otherwise
<!-- -->
**Args:**
:   Ref: A mob or obj.
:   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST,
    SOUTHEAST, SOUTHWEST.
:   Speed: Speed to move, in pixels. 0 uses Ref.step_size.
Move Ref in the direction Dir.