
## Cross (proc)

**Format:**
+   A.Cross(vector/B)

**Returns:**
+   The cross product of the two vectors, which is another vector.
***
This proc treats both vectors as 3D.

The cross product of two 3D vectors is a third vector that is orthogonal to them both. The length is the product of the length of both vectors and the sine of the angle between them.

The cross product depends on the order of the two vectors. If you switch their order, you get the negative result.

Note: Rounding errors can mean that if you divide out the length of the two original vectors, the value you get for a sine can potentially be outside of the valid range of -1 to 1. Use `clamp()` if you need to pass the sine to `arcsin()`, so you can be sure it stays in range.
***
**Related Pages:**
+    [vector](/ref/vector)
+    [vector proc](/ref/proc/vector)
+    [vars (vector)](/ref/vector/var)
