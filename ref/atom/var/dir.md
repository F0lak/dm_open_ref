[]{#/dir var (atom).md}    
## dir var (atom)    
**See also:**    
:   [Move proc (movable atom)]/atom/movable/proc/Move    
:   [icon var (atom)]/atom/var/icon    
:   [turn proc]/proc/turn    
:   [stddef.dm file]/%7B%7Bappendix%7D%7D/stddef%2edm    
<!-- -->    
**Default value:**    
:   SOUTH    
<!-- -->    
**Possible values:**    
:   NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST    
This is the direction that the object is facing. This has little effect    
unless the object\'s icon is directional. In the case of a directional    
icon, this selects the corresponding orientation from the icon file.    
An icon file with only four (cardinal) directions makes the choice of    
orientation ambiguous when the true direction is a diagonal. In that    
case, of the two possibilities, the one closest to the previous    
orientation is displayed. Sounds complicated, but it\'s what one would    
naturally expect.  