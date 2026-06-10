
## Dot (proc)

**Format:**
+   A.Dot(B)

**Arguments:**
+   B: The other vector.

**Returns:**
+   The dot product of the two vectors.
***
The dot product of two vectors is determined by multiplying each component in the first vector by its matching component in the second, and adding those multiples together. For instance in a 2D vector, the dot product of A and B is:


```dm
dot = A.x * B.x + A.y * B.y
```


The dot product is equal to the product of the magnitude of the two vectors and the cosine of the angle between them.


```dm
dot = A.size * B.size * cos(angle)
```


Note: Rounding errors in the math can affect this result. For instance, if you take the dot product of two unit vectors pointing the same direction, you would expect a result of 1, since the angle between them is 0. But due to small rounding errors, you can get a value just over 1. Therefore an expression like `arccos(V1.Dot(V2))` can give a not-a-number value when you expected 0. To combat this, use `clamp()` to clamp the cosine between -1 and 1, as in `arccos(clamp(V1.Dot(V2), -1, 1))`.
***
**Related Pages:**
+    [vector](/ref/vector)
+    [vector proc](/ref/proc/vector)
+    [vars (vector)](/ref/vector/var)
