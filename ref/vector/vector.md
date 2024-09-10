## vector.md {#vector.md byondver="516"}    
**See also:**    
:   [vector.md proc](/proc/vector.md)    
:   [procs (vector.md)](/vector.md/proc)    
:   [vars (vector.md)](/vector.md/var)    
:   [pixloc](/pixloc)    
:   [operators](/operator)    
:   [matrix](/matrix)    
A primitive value representing a numeric vector.md in 2 or 3 dimensions.    
That is, a 2D vector.md has x and y components, and a 3D vector.md has x, y,    
and z components.    
Vectors are primarily useful for physics and distance calculations.    
Vectors can be treated as a list for purposes of using the indexing `[]`    
operator, or a for loop. The `len` var is the number of components in    
the list, just like a regular list.    
Vectors support most math operations. Multiplication and division can be    
done with either a single number or a vector.md; the latter will act    
piecewise on each component, just like addition and subtraction do.    
When doing math on two vector.mds of different dimensions, the result will    
use the highest dimensionality. E.g., adding a 2D and 3D vector.md produces    
a 3D vector.md.    
Other supported procs for vector.mds include:    
[min()](/proc/min){.code}    
[max()](/proc/max){.code}    
[clamp()](/proc/clamp){.code}    
[round()](/proc/round){.code}    
[floor()](/proc/floor){.code}    
[ceil()](/proc/ceil){.code}    
[trunc()](/proc/trunc){.code}    
[fract()](/proc/fract){.code}  