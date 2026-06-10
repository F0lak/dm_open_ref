
## lerp (proc)

**Format:**
+   lerp(A, B, factor)

**Arguments:**
+   A: A number, matrix, vector, or turf/pixloc.
+   B: Another number, matrix, vector, or turf/pixloc.
+   factor: Interpolation factor, usually 0 to 1

**Returns:**
+   An interpolated value between A and B
***
Returns an interpolation or extrapolation from A to B. If factor is 0, A is returned; if factor is 1, B is returned. Otherwise an interpolated value between A and B is returned, based on the value of factor. The types of A and B must match, with few exceptions.

This is basically equivalent to returning `A + (B-A) * factor` for most things. When interpolating objects such as vectors, the returned value is always a new value, never a direct copy of A or B.


```dm

usr << lerp(1, 5, 0.25)   // outputs 2

```


Turfs can be treated like pixlocs in `lerp()`, so you can interpolate between turfs. Note that they must have the same Z coordinate.

Matrix interpolation behaves according to the rules in the matrix <a class="code" href="#/matrix/proc/Interpolate">Interpolate()</a> proc. For linear interpolation you need to use `A + (B-A) * factor` instead.
***
**Related Pages:**
+    [vector](/ref/vector)
+    [pixloc](/ref/pixloc)
+    [Interpolate proc (matrix)](/ref/matrix/proc/Interpolate)
