## pixloc.md {#pixloc.md byondver="516"}    
**See also:**    
:   [vars (pixloc.md)](/pixloc.md/var)    
:   [pixloc.md var (atom)](/atom/var/pixloc.md)    
:   [pixloc.md proc](/proc/pixloc.md)    
:   [bound_pixloc.md proc](/proc/bound_pixloc.md)    
A primitive type that encapsulates position information for an atom,    
with pixel movement included. I.e., it contains a turf (loc) and step_x    
and step_y offsets. Pixlocs can also be built from absolute world    
coordinates.    
The pixloc.md of an atom is taken from its loc and step_x/y vars only. If    
you want the pixloc.md of its bounds edges or its center, use the    
[`bound_pixloc.md()` proc](/proc/bound_pixloc.md) for that.    
Pixlocs support some math operations. A [vector](/vector) can be added    
or subtracted to a pixloc.md, and subtracting one pixloc.md from another will    
produce a vector. The [%](/operator/%){.code} and    
[%%](/operator/%%){.code} operators are supported, returning a vector.    
Other supported procs for pixloc.mds include:    
[min()](/proc/min){.code}    
[max()](/proc/max){.code}    
[clamp()](/proc/clamp){.code}    
[round()](/proc/round){.code}    
[floor()](/proc/floor){.code}    
[ceil()](/proc/ceil){.code}    
[trunc()](/proc/trunc){.code}    
[fract()](/proc/fract){.code} (returns a vector)  