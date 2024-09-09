[]{#/matrix/proc/Scale}    
## Scale proc (matrix)    
**See also:**    
:   [matrix](/ref/matrix)    
:   [matrix operators](/ref/matrix/operators)    
:   [matrix procs](/ref/matrix/proc)    
<!-- -->    
**Format:**    
:   Scale(x,y)    
<!-- -->    
**Args:**    
:   x: The amount of scaling to do in the x direction    
:   y: The amount of scaling to do in the y direction    
<!-- -->    
**Returns:**    
:   src    
The matrix is scaled by the appropriate amounts.    
If y is omitted, x is used for both. E.g., Scale(2) is equivalent to    
Scale(2,2).  