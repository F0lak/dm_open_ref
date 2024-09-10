[]{#/maxx var (world).md}    
## maxx var (world)    
**See also:**    
:   [area var (world)](/world/var/area)    
:   [maxy var (world)](/world/var/maxy)    
:   [maxz var (world)](/world/var/maxz)    
:   [turf var (world)](/world/var/turf)    
:   [Map](/map)    
<!-- -->    
**Default value:**    
:   0    
The world map is a three-dimensional block of turfs with coordinates    
ranging from (1,1,1) to (maxx,maxy,maxz). If set at compile time, it    
provides a lower bound and will be increased as needed by the map files.    
The default value is 0, indicating no map. If any of the map dimensions    
are set to non-zero values at compile time, the others will default to    
1.    
New territory created by increasing the map boundaries is filled in with    
the default turf and area (world.turf, and world.area).  