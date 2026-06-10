
## Normalize (proc)

**Format:**
+   V.Normalize()

**Returns:**
+   The same vector, after normalizing it to a unit vector.
***
Modifies the vector to make it a unit vector. This is the same as setting its `size` var to 1.

A degenerate vector such as 0,0,0 cannot be normalized; it will be unchanged by this call.
***
**Related Pages:**
+    [vector](/ref/vector)
+    [vector proc](/ref/proc/vector)
+    [size](/ref/vector/var/size)
