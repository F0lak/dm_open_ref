## pixloc var (atom) 
###### BYOND Version 516



Returns a pixloc representing this atom\'s `loc`, `step_x`, and
`step_y` positions. This var is read-only for areas and turfs, but
writable for movable atoms. When changed, it will alter the related
vars. A movable\'s pixloc is null if it isn\'t located on a turf.


A pixloc can be used for calculating distances, or passed to
various procs such as [get_dir()](/ref/proc/get_dir.md) {.code} and
[Move()](/ref/atom/movable/proc/Move.md) {.code}. 

This pixloc does not
take bounds into account. See
[bound_pixloc()](/ref/proc/bound_pixloc.md) for getting the pixloc of
an atom\'s corners or center of bounds. 

The returned pixloc is
not tied to this atom, so changing its vars will not alter the atom\'s
pixloc. The only exception is when using operators such as `+=`, since
`a += b` is just a shortcut for `a = a + b`. 
```
 // does not
alter obj\'s position var/pixloc/p = obj.pixloc p.step_x += 12 // does
alter obj\'s position, since a += b is just a = a + b obj.pixloc +=
vector(12,0) 
```


**See also:**
+   [pixloc](/ref/pixloc.md) 
+   [loc var (atom)](/ref/atom/var/loc.md) 
+   [step_x var (movable atoms)](/ref/atom/movable/var/step_x.md) 
+   [step_y var (movable atoms)](/ref/atom/movable/var/step_y.md) 
+   [pixloc proc](/ref/proc/pixloc.md) 
+   [bound_pixloc proc](/ref/proc/bound_pixloc.md) 
+   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) 