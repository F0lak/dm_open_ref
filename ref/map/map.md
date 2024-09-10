[]{#/map.md}    
## map.md    
**See also:**    
:   [#include directive](/DM/preprocessor/include)    
:   [area var (world)](/world/var/area)    
:   [maxx var (world)](/world/var/maxx)    
:   [turf var (world)](/world/var/turf)    
<!-- -->    
**Format:**    
:   #include \"map.mdname.dmm\"    
One or more map.md files may be loaded into the world\'s map.md. These are    
loaded into successive z-levels. If no map.md files are specified, the    
default project map.md file will be used. This file has the same name as    
the project but has the extension .dmm.    
If no map.md files are loaded, the world\'s map.md size is determined by the    
world variables maxx, maxy, and maxz. The default content of this map.md is    
determined by the world variables turf and area.    
### Example:    
#include \"level1.dmm\" #include \"level2.dmm\" #include \"level3.dmm\"  