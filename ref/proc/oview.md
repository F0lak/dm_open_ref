
## oview (proc)

**Format:**
+   oview(Dist,Center=usr)

**Arguments:**
+   Dist:   A number.
+   Center: An object on the map.

**Returns:**
+   A list of visible objects within Dist tiles of Center, excluding Center.
***
This instruction is just like view() except it doesn't include Center or its contents in the list.


```dm

oview() << "to others in sight of [usr]"

```

***
**Related Pages:**
+    [<< output operator](/ref/operator/%3c%3c/output)
+    [orange proc](/ref/proc/orange)
+    [view proc](/ref/proc/view)
