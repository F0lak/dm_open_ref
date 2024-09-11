## Normalize proc (vector) 
###### BYOND Version 516
**See also:**
*   [vector](/ref/vector.md) -m
*   [vector proc](/ref/proc/vector.md) -m
*   [size var (vector)](/ref/vector/var/size.md) -m<!-- -->
**Format:**
*   V.Normalize()
<!-- -->
**Returns:**
*   The same vector, after normalizing it to a unit vector.


Modifies the vector to make it a unit vector. This is the same
as setting its `size` var to 1. 

A degenerate vector such as
0,0,0 cannot be normalized; it will be unchanged by this call.