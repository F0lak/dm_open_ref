## orange proc
**See also:**
*   [\<\< output operator](/ref/operator/%3c%3c/output.md) -m
*   [block](/ref/proc/block.md) -m
*   [oview proc](/ref/proc/oview.md) -m
*   [range proc](/ref/proc/range.md) -m<!-- -->
**Format:**
*   orange(Dist,Center=usr)
<!-- -->
**Returns:**
*   A list of objects within Dist tiles of Center, excluding Center.
<!-- -->
**Args:**
*   Dist* A number.
*   Center* An object on the map.


This instruction is identical to oview() except visibility is
ignored. All objects are included in the list whether they are visible
or not. The center object and its contents are excluded.