
## matrix (proc)

**Format:**
+   matrix()
+   matrix(Matrix)
+   matrix(a, b, c, d, e, f)
+   matrix(x, y, MATRIX_SCALE)
+   matrix(n, MATRIX_SCALE)
+   matrix(angle, MATRIX_ROTATE)
+   matrix(x, y, MATRIX_TRANSLATE)

**Arguments:**
+   Matrix: a matrix to copy
+   a - f: The individual matrix components (in column-major order)
+   x, y: Arguments affecting how the shortcut matrix format affects x and y
+   n: The same value used for x and y together
+   angle: Rotation angle in degrees, clockwise

**Returns:**
+   A new matrix.
***
If no arguments are provided, a new default (identity) matrix is created.

There are also several "shortcut" matrix calls that can be made:
***
**Related Pages:**
+    [matrix](/ref/matrix)
+    [transform var (atom)](/ref/atom/var/transform)
