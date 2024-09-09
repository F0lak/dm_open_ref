[]{#/client/proc/Move}    
## Move proc (client)    
**See also:**    
:   [East proc (client)](/ref/client/proc/East/East.md)    
:   [Move proc (movable atom)](/ref/atom/movable/proc/Move/Move.md)    
:   [North proc (client)](/ref/client/proc/North/North.md)    
:   [Northeast proc (client)](/ref/client/proc/Northeast/Northeast.md)    
:   [Northwest proc (client)](/ref/client/proc/Northwest/Northwest.md)    
:   [South proc (client)](/ref/client/proc/South/South.md)    
:   [Southeast proc (client)](/ref/client/proc/Southeast/Southeast.md)    
:   [Southwest proc (client)](/ref/client/proc/Southwest/Southwest.md)    
:   [West proc (client)](/ref/client/proc/West/West.md)    
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