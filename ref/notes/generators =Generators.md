## Generators 
###### BYOND Version 514
**See also:**
*   [Particle effects](/ref/%7Bnotes%7D/particles.md) -m
*   [generator proc](/ref/proc/generator.md) -m
*   [color var (atom)](/ref/atom/var/color.md) -m
*   [Color matrix](/ref/%7Bnotes%7D/color-matrix.md) -m

A generator is an object that can produce a random number,
vector (list of 3 numbers), color (as a text string), or color matrix
(list of 20 numbers) in a specified range according to rules you set
down. It is used primarily for particle effects, since it can run on the
client. 

There are several types of generators:
-   **Numbers:** Generate a random real number.
-   **Vectors:** Generate a random vector.
-   **Shapes:** Generate a random vector within a specific shaped
    region.
-   **Colors:** Generate a random color or color matrix.


Generators can also be chained together with math operators and
some procs. The second value can be a regular value instead of a
generator, so for instance you can multiply a vector by 2, or by a
matrix to transform it.
  Operators                  Action
  -------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \+ - \* /                  Arithmetic operators. You can multiply a 3D vector by a color matrix (where red,green,blue in the matrix correspond to x,y,z) to do a 3D transform, or by a 2D matrix for a 2D transform.
  \- (unary)                 Negate the value, same as multiplying by -1.
  turn(), generator.Turn()   Rotate a vector clockwise in the XY plane.