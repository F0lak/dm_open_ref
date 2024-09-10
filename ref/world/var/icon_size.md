[]{#/icon_size var (world).md}    
## icon_size var (world)    
**See also:**    
:   [map_format var (world)](/world/var/map_format)    
:   [step_size var (movable atoms)](/atom/movable/var/step_size)    
:   [Gliding](/%7Bnotes%7D/gliding)    
:   [Pixel movement](/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Default value:**    
:   32    
This is the tile size that will be used as a default for icons in the    
world. It can be set to a single number that represents both the width    
and height, or you can use a format like \"\[width\]x\[height\]\" (such    
as \"16x48\") to specify width and height separately.    
This value affects several calculations, including icon operations and    
gliding between turfs.    
Note: If you do not use a square icon size and you are using a topdown    
map format, you may experience display issues if setting `client.dir` to    
`EAST` or `WEST`. A non-square tile with a topdown map format will also    
interfere with pixel movement. For this reason, square sizes are    
recommended when using any topdown-view map format.  