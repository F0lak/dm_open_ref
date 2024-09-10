[]{#/Dot proc (vector).md}    
## Dot proc (vector) {#dot-proc-vector byondver="516"}    
**See also:**    
:   [vector]/vector    
:   [vector proc]/proc/vector    
:   [vars (vector)]/vector/var    
<!-- -->    
**Format:**    
:   A.Dot(B)    
<!-- -->    
**Args:**    
:   B: The other vector.    
<!-- -->    
**Returns:**    
:   The dot product of the two vectors.    
The dot product of two vectors is determined by multiplying each    
component in the first vector by its matching component in the second,    
and adding those multiples together. For instance in a 2D vector, the    
dot product of A and B is: dot = A.x \* B.x + A.y + B.y    
The dot product is equal to the product of the magnitude of the two    
vectors and the cosine of the angle between them. dot = A.size \* B.size    
\* cos(angle)  