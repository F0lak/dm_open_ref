[]{#/pixloc}    
## pixloc {#pixloc byondver="516"}    
**See also:**    
:   [vars (pixloc)](/ref/pixloc/var.md)    
:   [pixloc var (atom)](/ref/atom/var/pixloc.md)    
:   [pixloc proc](/ref/proc/pixloc.md)    
:   [bound_pixloc proc](/ref/proc/bound_pixloc.md)    
A primitive type that encapsulates position information for an atom,    
with pixel movement included. I.e., it contains a turf (loc) and step_x    
and step_y offsets. Pixlocs can also be built from absolute world    
coordinates.    
The pixloc of an atom is taken from its loc and step_x/y vars only. If    
you want the pixloc of its bounds edges or its center, use the    
[`bound_pixloc()` proc](/ref/proc/bound_pixloc.md) for that.    
Pixlocs support some math operations. A [vector](/ref/vector.md) can be added    
or subtracted to a pixloc, and subtracting one pixloc from another will    
produce a vector. The [%](/ref/operator/%.md){.code} and    
[%%](/ref/operator/%%.md){.code} operators are supported, returning a vector.    
Other supported procs for pixlocs include:    
[min()](/ref/proc/min.md){.code}    
[max()](/ref/proc/max.md){.code}    
[clamp()](/ref/proc/clamp.md){.code}    
[round()](/ref/proc/round.md){.code}    
[floor()](/ref/proc/floor.md){.code}    
[ceil()](/ref/proc/ceil.md){.code}    
[trunc()](/ref/proc/trunc.md){.code}    
[fract()](/ref/proc/fract.md){.code} (returns a vector)  