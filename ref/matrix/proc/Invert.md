[]{#/Invert proc (matrix).md}    
## Invert proc (matrix)    
**See also:**    
:   [matrix]/matrix    
:   [matrix operators]/matrix/operators    
:   [matrix procs]/matrix/proc    
:   [\~ operator]/operator/~    
<!-- -->    
**Format:**    
:   Invert()    
<!-- -->    
**Returns:**    
:   src    
This inverts the current matrix, if possible.    
Not all matrices can be inverted. If it\'s not possible, the matrix is    
said to be degenerate. This happens if, for example, all of the values    
in the matrix are zero. A degenerate matrix will not be changed by this    
proc.  