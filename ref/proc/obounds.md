
## obounds (proc)

**Format:**
+   obounds(Ref, Dist=0)
+   obounds(Ref, x_offset, y_offset, extra_width=0, extra_height=0)

**Arguments:**
+   Ref:    A turf, obj, or mob.
+   Dist:   A number (distance in pixels).
+   x_offset, y_offset: Shifts bounding box position
+   extra_width, extra_height: Adjusts bounding box size

**Returns:**
+   A list of atoms (except areas) within Ref's bounding box, excluding Ref.
***
The results from obounds() are identical to bounds(), but obounds() leaves Ref out of the results.
***
**Related Pages:**
+    [bounds proc](/ref/proc/bounds)
