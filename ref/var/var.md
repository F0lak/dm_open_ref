[]{#/vars.md}    
## vars.mds    
**See also:**    
:   [path operators]/operator/path    
:   [vars.mds (atom)]/atom/vars.md    
:   [vars.mds (client)]/client/vars.md    
:   [vars.mds (datum)]/datum/vars.md    
:   [vars.mds (mob)]/mob/vars.md    
Variables are derived from vars.md.    
**Variable Declaration Format:**    
:   vars.md/Type/Name = Value    
:   vars.md Type/Name = Value    
Value defaults to null.    
The hard-coded types are:    
:   [datum]/datum (ancestor of all objects)    
:   [atom]/atom (all mappable objects)    
:   [atom/movable]/atom/movable (objs and mobs)    
:   [obj]/obj    
:   [mob]/mob    
:   [turf]/turf    
:   [area]/area    
:   [savefile]/savefile    
:   [client]/client    
:   [list]/list    
:   [world]/world    
<!-- -->    
Type modifiers:    
:   [global]/vars.md/global    
:   [const]/vars.md/const    
:   [tmp]/vars.md/tmp    
:   [final]/vars.md/final    
User types may be derived from anything except for `/world`, `/list`,    
`/client`, and `/savefile`.  