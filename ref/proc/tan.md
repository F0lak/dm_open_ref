
## tan (proc)

**Format:**
+   tan(X)

**Returns:**
+   The tangent of X, where X is in degrees.
***

```dm

mob/verb/test()
   usr << tan(0)  // 0
   usr << tan(45) // 1
   usr << tan(90) // infinity (or close enough)

```

***
**Related Pages:**
+    [arctan proc](/ref/proc/arctan)
+    [cos proc](/ref/proc/cos)
+    [sin proc](/ref/proc/sin)
+    [turn proc](/ref/proc/turn)
