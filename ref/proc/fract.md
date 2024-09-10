[]{#/fract proc.md}    
## fract proc {#fract-proc byondver="515"}    
**See also:**    
:   [trunc proc]/proc/trunc    
:   [floor proc]/proc/floor    
:   [ceil proc]/proc/ceil    
:   [round proc]/proc/round    
<!-- -->    
**Format:**    
:   fract(A)    
<!-- -->    
**Returns:**    
:   fractional part of A    
<!-- -->    
**Args:**    
:   A: A number, pixloc, or vector.    
Returns the fractional part of the number A, with the same sign. This is    
everything after the decimal point.    
### Example:    
usr \<\< fract(1.45) // outputs 0.45 usr \<\< fract(-1.45) // outputs    
-0.45    
If A is a pixloc, it will be treated as a vector with just its x and y    
parts, and the result will be a vector.  