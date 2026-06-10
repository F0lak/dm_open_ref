
## matrix (proc)

**Format:**
+   turn(Matrix, Angle)

**Arguments:**
+   Matrix: a matrix to rotate
+   Angle: An angle in degrees (clockwise rotation).

**Returns:**
+   A new matrix which has been rotated.
***

```dm

mob/verb/drink()
   //this effect is very confusing!
   usr.transform = turn(usr.transform, 90)
   usr << "Woah!  That stuff is powerful!"
   sleep(200)
   usr.transform = null

```

***
**Related Pages:**
+    [turn proc](/ref/proc/turn)
+    [matrix](/ref/matrix)
