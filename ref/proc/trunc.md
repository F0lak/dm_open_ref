## trunc proc 
###### BYOND Version 515
**See also:**
*   [fract proc](/proc/fract)
*   [floor proc](/proc/floor)
*   [ceil proc](/proc/ceil)
*   [round proc](/proc/round)
<!-- -->
**Format:**
*   trunc(A)
<!-- -->
**Returns:**
*   truncated A
<!-- -->
**Args:**
*   A* A number, pixloc, or vector.


Returns the integer part of the number A. That is, this rounds
toward 0 to an integer.
### Example:

```
 usr \<\< trunc(1.45) // outputs 1 usr \<\< trunc(-1.45) //
outputs -1 
```
