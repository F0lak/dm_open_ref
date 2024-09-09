[]{#/obj}    
## obj    
**See also:**    
:   [atom](ref/atom)    
:   [movable atoms](ref/atom/movable)    
:   [procs (obj)](ref/obj/proc)    
:   [vars (obj)](ref/obj/var)    
There are two types of movable atoms: objs and mobs. The difference    
between them is that a mob can be attached to a human player, and is    
also typically used for NPCs and creatures. The obj type is a little bit    
simpler and is typically used for objects in the environment, items in    
inventory, etc.    
Objects are derived from `/obj`, which derives from `/atom/movable`.    
The following example defines the obj type `/obj/scooper`.    
### Example:    
obj scooper desc = \"Super pooper scooper.\"  