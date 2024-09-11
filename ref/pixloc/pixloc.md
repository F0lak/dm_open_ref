## pixloc 
###### BYOND Version 516
**See also:**
*   [vars (pixloc)](/ref/pixloc/var.md) -m
*   [pixloc var (atom)](/ref/atom/var/pixloc.md) -m
*   [pixloc proc](/ref/proc/pixloc.md) -m
*   [bound_pixloc proc](/ref/proc/bound_pixloc.md) -m


A primitive type that encapsulates position information for an
atom, with pixel movement included. I.e., it contains a turf (loc) and
step_x and step_y offsets. Pixlocs can also be built from absolute world
coordinates. 

The pixloc of an atom is taken from its loc and
step_x/y vars only. If you want the pixloc of its bounds edges or its
center, use the [`bound_pixloc()` proc](/ref/proc/bound_pixloc.md) -m for that.


Pixlocs support some math operations. A [vector](/ref/vector.md) -m can
be added or subtracted to a pixloc, and subtracting one pixloc from
another will produce a vector. The [%](/ref/operator/%.md) -m{.code} and
[%%](/ref/operator/%%.md) -m{.code} operators are supported, returning a vector.


Other supported procs for pixlocs include:
[min()](/ref/proc/min.md) -m{.code}
[max()](/ref/proc/max.md) -m{.code}
[clamp()](/ref/proc/clamp.md) -m{.code}
[round()](/ref/proc/round.md) -m{.code}
[floor()](/ref/proc/floor.md) -m{.code}
[ceil()](/ref/proc/ceil.md) -m{.code}
[trunc()](/ref/proc/trunc.md) -m{.code}
[fract()](/ref/proc/fract.md) -m.code} (returns a vector)