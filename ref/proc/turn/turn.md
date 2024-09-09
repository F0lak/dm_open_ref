[]{#/proc/turn}    
## turn proc    
**See also:**    
:   [Turn proc (icon)](/ref/icon/proc/Turn/Turn.md)    
:   [dir var (atom)](/ref/atom/var/dir/dir.md)    
:   [Turn proc (vector)](/ref/vector/proc/Turn/Turn.md)    
<!-- -->    
**Format:**    
:   turn(Dir, Angle)    
<!-- -->    
**Args:**    
:   Dir: One of NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST,    
    SOUTHEAST, SOUTHWEST.    
:   Angle: An angle in degrees (counterclockwise rotation).    
<!-- -->    
**Returns:**    
:   The rotated direction.    
This proc can also be applied to an [icon](/ref/proc/turn/icon/icon.md), a    
[matrix](/ref/proc/turn/matrix/matrix.md), or a [vector](/ref/proc/turn/vector/vector.md).    
### Example:    
var/dir dir = turn(NORTH, 90) // dir = west dir = turn(dir, -90) // dir    
= north dir = turn(dir, 45) // dir = northwest    
Only multiples of 45 are allowed for angles. If an invalid angle is    
used, it will be treated as the closest multiple of 45 to 0.    
If the supplied Dir is invalid, such as 0, or something like UP or DOWN,    
the result is a random direction unless the angle is also 0.  