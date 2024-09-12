## obounds proc
**See also:**
+   [bounds proc](/ref/proc/bounds.md) <!-- -->
**Format:**
+   obounds(Ref, Dist=0)
+   obounds(Ref, x_offset, y_offset, extra_width=0, extra_height=0)
<!-- -->
**Returns:**
+   A list of atoms (except areas) within Ref\'s bounding box, excluding
    Ref.
<!-- -->
**Args:**
+   Ref+ A turf, obj, or mob.
+   Dist+ A number (distance in pixels).
+   x_offset, y_offset+ Shifts bounding box position
+   extra_width, extra_height+ Adjusts bounding box size


The results from obounds() are identical to bounds(), but
obounds() leaves Ref out of the results.