[]{#/client/proc/Move}    
## Move proc (client)    
**See also:**    
:   [East proc (client)](/ref/client/proc/East)    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move)    
:   [North proc (client)](/ref/client/proc/North)    
:   [Northeast proc (client)](/ref/client/proc/Northeast)    
:   [Northwest proc (client)](/ref/client/proc/Northwest)    
:   [South proc (client)](/ref/client/proc/South)    
:   [Southeast proc (client)](/ref/client/proc/Southeast)    
:   [Southwest proc (client)](/ref/client/proc/Southwest)    
:   [West proc (client)](/ref/client/proc/West)    
<!-- -->    
**Format:**    
:   Move(loc,dir)    
<!-- -->    
**Returns:**    
:   1 on success; 0 on failure    
<!-- -->    
**When:**    
:   Called by the direction procs.    
<!-- -->    
**Default action:**    
:   Calls src.mob.Move(). Also cancels any automated movement by calling    
    walk(usr,0).  