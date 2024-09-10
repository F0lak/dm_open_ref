[]{#/turf.md}    
## turf.md    
**See also:**    
:   [atom](/atom)    
:   [procs (turf.md)](/turf.md/proc)    
:   [vars (turf.md)](/turf.md/var)    
:   [Map](/map)    
Turfs cover the surface of the map. They are derived from `/turf.md` which    
derives from `/atom`.    
This example defines the turf.md prototype `/turf.md/floor` and `/turf.md/wall`.    
### Example:    
turf.md floor desc = \"A wood plank floor.\" wall desc = \"A stone wall.\"    
density = 1    
Turfs cannot be moved. They can only be created or destroyed by changing    
`world.maxx`, `world.maxy`, or `world.maxz`. When you create a new turf.md    
with `new()`, it always replaces the old one.    
### Example:    
// replace old_turf.md with a wall var/turf.md/wall/T = new(old_turf.md)  