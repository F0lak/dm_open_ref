[]{#/Move proc (client).md}    
## Move proc (client)    
**See also:**    
:   [East proc (client)]/client/proc/East    
:   [Move proc (movable atom)]/atom/movable/proc/Move    
:   [North proc (client)]/client/proc/North    
:   [Northeast proc (client)]/client/proc/Northeast    
:   [Northwest proc (client)]/client/proc/Northwest    
:   [South proc (client)]/client/proc/South    
:   [Southeast proc (client)]/client/proc/Southeast    
:   [Southwest proc (client)]/client/proc/Southwest    
:   [West proc (client)]/client/proc/West    
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