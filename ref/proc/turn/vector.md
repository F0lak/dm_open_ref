## turn proc (applied to a vector) 
###### BYOND Version 516
**See also:**
*   [vector](/vector)
*   [vector proc](/proc/vector)
*   [Turn proc (vector)](/vector/proc/Turn)
<!-- -->
**Format:**
*   turn(vector/A, angle)
*   turn(vector/A, vector/B)
<!-- -->
**Returns:**
*   A new rotated vector.
<!-- -->
**Args:**
*   A* The vector to rotate.
*   angle* An angle to turn a vector counter-clockwise in 2D.
*   B* A vector to rotate around (left-hand rule).


All angles are in degrees. 

When the argument is an
angle, the result is a copy of vector A, rotated in 2 dimensions
counter-clockwise. 

When the argument is a vector, the result is
rotated in 3 dimensions around vector B using the left-hand rule (thumb
pointed in the direction of B, rotation following curled fingers). The
angle of rotation is the length of B, in degrees.