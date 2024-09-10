[]{#/atom.md}    
## atom.md    
**See also:**    
:   [area]/area    
:   [datum]/datum    
:   [mob]/mob    
:   [movable atom.mds]/atom.md/movable    
:   [obj]/obj    
:   [procs (atom.md)]/atom.md/proc    
:   [turf]/turf    
:   [vars (atom.md)]/atom.md/var    
The /atom.md object type is the ancestor of all mappable objects in the    
game. The types /area, /turf, /obj, and /mob are all derived from /atom.md.    
You should not create instances of /atom.md directly but should use /area,    
/turf, /obj, and /mob for actual objects. The /atom.md object type exists    
for the purpose of defining variables or procedures that are shared by    
all of the other \"physical\" objects. These are also the only objects    
for which verbs may be accessible to the user.    
/atom.md is derived from /datum, so it inherits the basic properties that    
are shared by all DM objects.  