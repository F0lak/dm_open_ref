
## pixloc (var)
***
Returns a pixloc representing this atom's physical position. The position is based on its `loc`, `step_x`, `step_y`, `bound_x`, and `bound_y`. This var is read-only for areas and turfs, but writable for movable atoms. When changed, it will alter the related vars. A movable's pixloc is null if it isn't located on a turf.

A pixloc can be used for calculating distances, or passed to various procs such as <a class="code" href="#/proc/get_dir">get_dir()</a> and <a class="code" href="#/atom/movable/proc/Move">Move()</a>.

This pixloc is equivalent to <a class="code" href="#/proc/bound_pixloc">bound_pixloc(src,SOUTHWEST)</a>. You can use the `bound_pixloc()` proc to get the pixloc of an atom's other corners or center of bounds.

The returned pixloc is not tied to this atom, so changing its vars will not alter the atom's pixloc. The only exception is when using operators such as `+=`, since `a += b` is just a shortcut for `a = a + b`.


```dm

// does not alter obj's position
var/pixloc/p = obj.pixloc
p.step_x += 12

// does alter obj's position, since a += b is just a = a + b
obj.pixloc += vector(12,0)

```

***
**Related Pages:**
+    [pixloc](/ref/pixloc)
+    [loc](/ref/atom/var/loc)
+    [step_x var (movable atom)](/ref/atom/movable/var/step_x)
+    [step_y var (movable atom)](/ref/atom/movable/var/step_y)
+    [pixloc proc](/ref/proc/pixloc)
+    [bound_pixloc proc](/ref/proc/bound_pixloc)
+    [Pixel movement](/ref/{notes}/pixel-movement)
