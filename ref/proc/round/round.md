[]{#/proc/round}    
## round proc    
**See also:**    
:   [floor proc](ref/proc/floor)    
:   [ceil proc](ref/proc/ceil)    
:   [trunc proc](ref/proc/trunc)    
:   [fract proc](ref/proc/fract)    
<!-- -->    
**Format:**    
:   round(A)    
:   round(A,B)    
<!-- -->    
**Returns:**    
:   rounded A    
<!-- -->    
**Args:**    
:   A: A number, pixloc, or vector.    
:   B: The nearest multiple to round A.    
The first format returns the floor of A (the largest integer less than    
or equal to A), and has been deprecated in favor of `floor(A)`. The    
second format rounds A to the nearest multiple of B.    
### Example:    
usr \<\< round(1.45) // outputs 1 usr \<\< round(-1.45) // outputs -2    
usr \<\< round(1.45,1.5) // outputs 1.5    
If A is a vector, B can also be a vector to round each component    
separately.    
If A is a pixloc, only the x and y portions will be considered. B may be    
a vector.  