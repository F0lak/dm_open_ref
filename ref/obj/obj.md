[]{#/obj.md}    
## obj.md    
**See also:**    
:   [atom]/atom    
:   [movable atoms]/atom/movable    
:   [procs (obj.md)]/obj.md/proc    
:   [vars (obj.md)]/obj.md/var    
There are two types of movable atoms: obj.mds and mobs. The difference    
between them is that a mob can be attached to a human player, and is    
also typically used for NPCs and creatures. The obj.md type is a little bit    
simpler and is typically used for obj.mdects in the environment, items in    
inventory, etc.    
Objects are derived from `/obj.md`, which derives from `/atom/movable`.    
The following example defines the obj.md type `/obj.md/scooper`.    
### Example:    
obj.md scooper desc = \"Super pooper scooper.\"  