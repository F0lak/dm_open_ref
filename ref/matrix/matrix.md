## matrix 
###### BYOND Version 500



To display rotation, scaling, and other transformations on
atoms, DM uses 2D matrices. The /matrix datum is a convenient way of
handling the numbers involved, as it can be easily manipulated. There
are six vars, a through f, laid out like so:
              a d 0
    x y 1  *  b e 0  =  x' y' 1
              c f 1


When an x,y point is multiplied by the matrix, it becomes the
new point x\',y\'. This is equivalent to:
    x' = a*x + b*y + c
    y' = d*x + e*y + f


The default matrix is:
    1 0 0
    0 1 0
    0 0 1


Matrices are created with the matrix() proc, or by calling
new/matrix(). (See the matrix() proc for examples.) They are also
created as needed whenever you read from atom.transform or use certain
operators. 

Manipulation of matrices can be done with operators,
or with procs. You can do the following with them:
-   **Multiply:** Multiplying two matrices together will chain together
    the transformations they represent. For instance, a scaling matrix
    multiplied by a rotation matrix says: Scale, then rotate.
    Multiplication of two matrices is sensitive to the order you use.
-   **Scale:** A simple scale matrix uses only the a and e values, to
    scale x and y by a certain amount.
-   **Rotate:** A rotation matrix can rotate an atom by whatever amount
    you like.
-   **Translate:** Translation is like a pixel offset, changing the
    atom\'s position.
-   **Interpolate:** You can calculate a matrix that lies somewhere
    between two other matrices, which can be helpful for animation.


When you\'ve built your matrix, you can assign it to
atom.transform to change the way that atom is displayed. 

The
matrices supported by this datum are **not** the same kind used to
transform colors, as in the atom.color var and icon.MapColors() proc.
For color matrices, see [color matrix](/ref/%7Bnotes%7D/color-matrix.md) 

> [!TIP] 
> **See also:**
> +   [matrix proc](/ref/proc/matrix.md) 
> +   [matrix operators](/ref/matrix/operators.md) 
> +   [matrix procs](/ref/matrix/proc.md) 
> +   [transform var (atom)](/ref/atom/var/transform.md) 
> +   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) 