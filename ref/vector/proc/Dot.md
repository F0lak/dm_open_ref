## Dot proc (vector) 
###### BYOND Version 516
**See also:**
+   [vector](/ref/vector.md) 
+   [vector proc](/ref/proc/vector.md) 
+   [vars (vector)](/ref/vector/var.md) <!-- -->
**Format:**
+   A.Dot(B)
<!-- -->
**Args:**
+   B: The other vector.
<!-- -->
**Returns:**
+   The dot product of the two vectors.


The dot product of two vectors is determined by multiplying
each component in the first vector by its matching component in the
second, and adding those multiples together. For instance in a 2D
vector, the dot product of A and B is: 
```
dot = A.x \* B.x +
A.y + B.y
```
 

The dot product is equal to the product of
the magnitude of the two vectors and the cosine of the angle between
them. 
```
dot = A.size \* B.size \* cos(angle)
```
