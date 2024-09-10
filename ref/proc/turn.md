[]{#/turn proc.md}    
## turn proc    
**See also:**    
:   [Turn proc (icon)](/icon/proc/Turn)    
:   [dir var (atom)](/atom/var/dir)    
:   [Turn proc (vector)](/vector/proc/Turn)    
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
This proc can also be applied to an [icon](/turn proc.md/icon), a    
[matrix](/turn proc.md/matrix), or a [vector](/turn proc.md/vector).    
### Example:    
var/dir dir = turn(NORTH, 90) // dir = west dir = turn(dir, -90) // dir    
= north dir = turn(dir, 45) // dir = northwest    
Only multiples of 45 are allowed for angles. If an invalid angle is    
used, it will be treated as the closest multiple of 45 to 0.    
If the supplied Dir is invalid, such as 0, or something like UP or DOWN,    
the result is a random direction unless the angle is also 0.  