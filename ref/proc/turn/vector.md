
## vector (proc)

**Format:**
+   turn(vector/A, angle)
+   turn(vector/A, vector/B)

**Arguments:**
+   A: The vector to rotate.
+   angle: An angle to turn a vector counter-clockwise in 2D.
+   B: A vector to rotate around (left-hand rule).

**Returns:**
+   A new rotated vector.
***
All angles are in degrees.

When the argument is an angle, the result is a copy of vector A, rotated in 2 dimensions counter-clockwise.

When the argument is a vector, the result is rotated in 3 dimensions around vector B using the left-hand rule (thumb pointed in the direction of B, rotation following curled fingers). The angle of rotation is the length of B, in degrees.
***
**Related Pages:**
+    [vector](/ref/vector)
+    [vector proc](/ref/proc/vector)
+    [Turn](/ref/vector/proc/Turn)
