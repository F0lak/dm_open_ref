## lerp proc 
###### BYOND Version 516

**Format:**
+   lerp(A, B, factor)

**Returns:**
+   The number that is factor% between A and B

**Args:**
+   A: A number, matrix, vector or turf/pixloc
+   B: A number, matrix, vector or turf/pixloc
+   factor: Interpolation Factor, usually between 0 and 1

Returns an interpolation or extrapolation from A to B. If factor is 0, A is returned; if factor is 1, B is returned. Otherwise an interpolated value between A and B is returned, based on the value of factor.

This is basically equivalent to returning A + (B-A) * factor for most things. When interpolating objects such as vectors, the returned value is always a new value, never a direct copy of A or B.

> [!IMPORTANT]
> The types of A and B must match, with few exceptions.

### Example:

```dm
world << lerp(0, 10, 0.25) // outputs 2.5
world << lerp(5, 10, 0.25) // outputs 7.5
world << lerp(1, 10, 2) // outputs 21
```
Turfs can be treated like pixlocs in lerp(), so you can interpolate between turfs. Note that they must have the same Z coordinate.

Matrix interpolation behaves according to the rules in the [matrix Interpolate proc](/ref/matrix/proc/Interpolate.md).

> [!TIP] 
> **See also:**
> +   [vector](/ref/vector/vector.md) 
> +   [pixloc](/ref/pixloc/pixloc.md) 
> +   [Interpolate proc (matrix)](/ref/matrix/proc/Interpolate.md) 