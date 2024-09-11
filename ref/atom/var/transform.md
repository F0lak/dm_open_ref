## transform var (atom) 
###### BYOND Version 500
**See also:**
*   [vars (atom)](/ref/atom/var.md) -m
*   [matrix](/ref/matrix.md) -m


An atom can be made to appear rotated, scaled, and/or
translated (moved) by using affine transforms. This takes a matrix and
multiplies the x and y positions of the icon\'s corners like so:
              a d 0
    x y 1  *  b e 0  =  x' y' 1
              c f 1


This is equivalent to:
    x' = a*x + b*y + c
    y' = d*x + e*y + f


You do not need to understand matrix math to use transforms,
because you can use the [matrix datum](/ref/matrix.md) -mto do this for you.


Transformations are relative to the center of the icon. They do
not apply to maptext.
### Examples:

```
 // Rotate the atom by 45° clockwise src.transform =
turn(src.transform, 45) // OR var/matrix/M = matrix() M.Turn(45)
src.transform = M // Scale the atom by 2x2 src.transform \*= 2 // OR
var/matrix/M = matrix() M.Scale(2,2) src.transform = M 
```



Whenever you read the atom.transform var, you will get a *copy*
of the atom\'s current transformation. Whenever you assign a value to
the var, you will update the transformation. 

Assigning null to
atom.transform will revert the atom to using no transformation at all.
It is also legal to assign a list with six values, which is equivalent
to using a matrix.