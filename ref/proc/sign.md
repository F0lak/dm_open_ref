
## sign (proc)

**Format:**
+   sign(A)

**Arguments:**
+   A: A number or a . [vector](/ref/vector)

**Returns:**
+   1 if A > 0, -1 if A < 0, 0 if A == 0
***
Returns the sign of A. If used with a vector, a new vector is returned where `sign()` has been applied to each component.


```dm

usr << sign(20) // outputs 1
usr << sign(0)  // outputs 0
usr << sign(-3) // outputs -1

```

***
**Related Pages:**
+    [floor proc](/ref/proc/floor)
+    [ceil proc](/ref/proc/ceil)
+    [round proc](/ref/proc/round)
+    [trunc proc](/ref/proc/trunc)
+    [fract proc](/ref/proc/fract)
