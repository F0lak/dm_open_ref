## orange proc

**Format:**
+   orange(Dist,Center=usr)
<!-- -->
**Returns:**
+   A list of objects within Dist tiles of Center, excluding Center.
<!-- -->
**Args:**
+   Dist: A number.
+   Center: An object on the map.


This instruction is identical to oview() except visibility is
ignored. All objects are included in the list whether they are visible
or not. The center object and its contents are excluded.

**See also:**
+   [\<\< output operator](/ref/operator/%3c%3c/output.md) 
+   [block](/ref/proc/block.md) 
+   [oview proc](/ref/proc/oview.md) 
+   [range proc](/ref/proc/range.md) <!-- -->