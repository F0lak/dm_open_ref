[]{#/pixloc}
## pixloc {#pixloc byondver="516"}
**See also:**
:   [vars (pixloc)](#/pixloc/var)
:   [pixloc var (atom)](#/atom/var/pixloc)
:   [pixloc proc](#/proc/pixloc)
:   [bound_pixloc proc](#/proc/bound_pixloc)
A primitive type that encapsulates position information for an atom,
with pixel movement included. I.e., it contains a turf (loc) and step_x
and step_y offsets. Pixlocs can also be built from absolute world
coordinates.
The pixloc of an atom is taken from its loc and step_x/y vars only. If
you want the pixloc of its bounds edges or its center, use the
[`bound_pixloc()` proc](#/proc/bound_pixloc) for that.
Pixlocs support some math operations. A [vector](#/vector) can be added
or subtracted to a pixloc, and subtracting one pixloc from another will
produce a vector. The [%](#/operator/%){.code} and
[%%](#/operator/%%){.code} operators are supported, returning a vector.
Other supported procs for pixlocs include:
[min()](#/proc/min){.code}
[max()](#/proc/max){.code}
[clamp()](#/proc/clamp){.code}
[round()](#/proc/round){.code}
[floor()](#/proc/floor){.code}
[ceil()](#/proc/ceil){.code}
[trunc()](#/proc/trunc){.code}
[fract()](#/proc/fract){.code} (returns a vector)