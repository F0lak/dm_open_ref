[]{#/matrix/proc/Invert}    
## Invert proc (matrix)    
**See also:**    
:   [matrix](/ref/matrix/matrix.md)    
:   [matrix operators](/ref/matrix/operators/operators.md)    
:   [matrix procs](/ref/matrix/proc/proc.md)    
:   [\~ operator](/ref/operator/~/~.md)    
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