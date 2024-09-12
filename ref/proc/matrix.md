## matrix proc 
###### BYOND Version 500

**Format:**
+   matrix()
+   matrix(Matrix)
+   matrix(a, b, c, d, e, f)
+   matrix(x, y, MATRIX_SCALE)
+   matrix(n, MATRIX_SCALE)
+   matrix(angle, MATRIX_ROTATE)
+   matrix(x, y, MATRIX_TRANSLATE)
<!-- -->
**Returns:**
+   A new matrix.
<!-- -->
**Args:**
+   Matrix: a matrix to copy
+   a - f: The individual matrix components (in column-major order)
+   x, y: Arguments affecting how the shortcut matrix format affects x
    and y
+   n: The same value used for x and y together
+   angle: Rotation angle in degrees, clockwise


If no arguments are provided, a new default (identity) matrix
is created. 

There are also several \"shortcut\" matrix calls
that can be made:
matrix(x, y, MATRIX_SCALE)\
matrix(n, MATRIX_SCALE)
+   A scaling matrix, scaling either x and y independently or both
    together
matrix(angle, MATRIX_ROTATE)
+   A matrix that rotates by the angle in degrees, clockwise
matrix(x, y, MATRIX_TRANSLATE)
+   A matrix that translates by x and y

**See also:**
+   [matrix](/ref/matrix.md) 
+   [transform var (atom)](/ref/atom/var/transform.md) <!-- -->