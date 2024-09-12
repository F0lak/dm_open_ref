## bound_pixloc proc 
###### BYOND Version 516
**See also:**
+   [pixloc](/ref/pixloc.md) 
+   [pixloc var (atom)](/ref/atom/var/pixloc.md) 
+   [pixloc proc](/ref/proc/pixloc.md) 
+   [bound_width var (movable atom)](/ref/atom/movable/var/bound_width.md) 
+   [bound_height var (movable atom)](/ref/atom/movable/var/bound_height.md) <!-- -->
**Format:**
+   bound_pixloc(Atom, Dir)
<!-- -->
**Returns:**
+   A `pixloc` object representing a corner, side, or center of atom
    bounds.
<!-- -->
**Args:**
+   Atom+ An atom.
+   Dir+ The side or corner to use, or 0 for center.


Creates a new `pixloc` object based on an existing object\'s
bounds. If either `bound_x` or `bound_y` (both deprecated) are nonzero,
then `bound_pixloc(atom, SOUTHWEST)` will differ from `atom.pixloc`.


If the atom is not directly on the map, this value is null.
### Example:

```
 mob/verb/DistanceTo(atom/A) var/my_center = bound_pixloc(src,
0) var/A_center = bound_pixloc(A, 0) var/vector/V = A_center - my_center
return length(V) 
```
