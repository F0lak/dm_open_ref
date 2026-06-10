
## get_dist (proc)

**Format:**
+   get_dist(Loc1, Loc2)

**Arguments:**
+   Loc1: An object on the map.
+   Loc2: An object on the map.

**Returns:**
+   The distance between  and , in tiles.  This is
the number of full-tile movements (disregarding any obstacles and allowing
diagonal moves ) required to go from one to
the other.  You can think of it as the max of their x, y, and z distances.
***
For a distance in pixels, use `bounds_dist()`.

`get_dist()` will return -1 when `Loc1` and `Loc2` are the same object. If one or both of them is not on the map, an infinite value is returned.

Note: Prior to BYOND 515, `get_dist()` never returned a value greater than 127, which it counted as "infinite".
***
**Related Pages:**
+    [bounds_dist proc](/ref/proc/bounds_dist)
