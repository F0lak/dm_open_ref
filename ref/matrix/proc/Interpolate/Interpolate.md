[]{#/matrix/proc/Interpolate}    
## Interpolate proc (matrix)    
**See also:**    
:   [matrix](ref/matrix)    
:   [matrix operators](ref/matrix/operators)    
:   [matrix procs](ref/matrix/proc)    
<!-- -->    
**Format:**    
:   Interpolate(Matrix2, t)    
<!-- -->    
**Args:**    
:   Matrix2: Another matrix    
:   t: The interpolation factor: from 0 (src) to 1 (Matrix2). Usually    
    this is a value between 0 and 1.    
Calculates and returns a new matrix between src and Matrix2. If t is    
0.5, then the result will be exactly halfway between both matrices.    
There are many ways to interpolate matrices. Whenever possible, DM will    
interpolate by doing scaling and/or shearing first, then rotation, then    
translation. This is done by trying to find the angle of rotation of    
each matrix first; a rotation of 180° is counted as a flip rather than a    
rotation.    
It is not strictly necessary for t to be between 0 and 1. Using a value    
out of bounds will extrapolate a matrix, continuing the change as far as    
t.  