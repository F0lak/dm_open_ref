
## bound_pixloc (proc)

**Format:**
+   bound_pixloc(Atom, Dir)

**Arguments:**
+   Atom: An atom.
+   Dir: The side or corner to use, or 0 for center.

**Returns:**
+   A  object representing a corner, side, or center of atom bounds.
***
Creates a new `pixloc` object based on an existing object's bounds. If either `bound_x` or `bound_y` are nonzero, then `bound_pixloc(atom, SOUTHWEST)` will differ from `atom.pixloc`.

If the atom is not directly on the map, this value is null.


```dm

mob/verb/DistanceTo(atom/A)
    var/my_center = bound_pixloc(src, 0)
    var/A_center = bound_pixloc(A, 0)
    var/vector/V = A_center - my_center
    return length(V)

```

***
**Related Pages:**
+    [pixloc](/ref/pixloc)
+    [pixloc](/ref/atom/var/pixloc)
+    [pixloc proc](/ref/proc/pixloc)
+    [bound_width var (movable atom)](/ref/atom/movable/var/bound_width)
+    [bound_height var (movable atom)](/ref/atom/movable/var/bound_height)
