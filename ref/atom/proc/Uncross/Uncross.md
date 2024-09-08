[]{#/atom/proc/Uncross}
## Uncross proc (atom) {#uncross-proc-atom byondver="490"}
**See also:**
:   [Enter proc (atom)](#/atom/proc/Enter)
:   [Entered proc (atom)](#/atom/proc/Entered)
:   [Exit proc (atom)](#/atom/proc/Exit)
:   [Exited proc (atom)](#/atom/proc/Exited)
:   [Cross proc (atom)](#/atom/proc/Cross)
:   [Crossed proc (atom)](#/atom/proc/Crossed)
:   [Uncrossed proc (atom)](#/atom/proc/Uncrossed)
:   [Move proc (movable atom)](#/atom/movable/proc/Move)
:   [group var (mob)](#/mob/var/group)
:   [Pixel movement](#/%7Bnotes%7D/pixel-movement)
<!-- -->
**Format:**
:   Uncross(atom/movable/O)
<!-- -->
**Returns:**
:   1 to permit; 0 to deny.
<!-- -->
**When:**
:   Called when another object attempts to stop overlapping this one.
<!-- -->
**Args:**
:   O: the object attempting to get away.
<!-- -->
**Default action:**
:   Allow the object to get away (returning 1)