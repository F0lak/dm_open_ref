[]{#/vector/proc/Turn}    
## Turn proc (vector) {#turn-proc-vector byondver="516"}    
**See also:**    
:   [turn proc (applied to a vector)](/ref/proc/turn/vector.md)    
:   [vector](/ref/vector.md)    
:   [vector proc](/ref/proc/vector.md)    
:   [vars (vector)](/ref/vector/var.md)    
<!-- -->    
**Format:**    
:   A.Turn(angle)    
:   A.Turn(B)    
<!-- -->    
**Args:**    
:   angle: An angle to turn a vector clockwise in 2D.    
:   B: A vector to rotate around (right-hand rule).    
<!-- -->    
**Returns:**    
:   The vector A, after rotating it.    
This proc modifies the source vector. For legacy reasons, it rotates in    
the opposite direction of the built-in `turn()` proc.    
All angles are in degrees.    
When the argument is an angle, the source vector A is rotated in 2    
dimensions clockwise.    
When the argument is a vector, the source vector A is rotated in 3    
dimensions around vector B using the right-hand rule (thumb pointed in    
the direction of B, rotation following curled fingers). The angle of    
rotation is the length of B, in degrees.  