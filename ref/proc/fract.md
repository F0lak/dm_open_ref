
## fract (proc)

**Format:**
+   fract(A)

**Arguments:**
+   A: A number, pixloc, or vector.

**Returns:**
+   fractional part of A
***
Returns the fractional part of the number A, with the same sign. This is everything after the decimal point.


```dm

usr << fract(1.45) // outputs 0.45

usr << fract(-1.45) // outputs -0.45

```


If A is a pixloc, it will be treated as a vector with just its x and y parts, and the result will be a vector.
***
**Related Pages:**
+    [trunc proc](/ref/proc/trunc)
+    [floor proc](/ref/proc/floor)
+    [ceil proc](/ref/proc/ceil)
+    [round proc](/ref/proc/round)
+    [sign proc](/ref/proc/sign)
