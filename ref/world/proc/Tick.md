[]{#/Tick proc (world).md}    
## Tick proc (world) {#tick-proc-world byondver="515"}    
**See also:**    
:   [cpu var (world)]/world/var/cpu    
:   [map_cpu var (world)]/world/var/map_cpu    
:   [tick_usage var (world)]/world/var/tick_usage    
<!-- -->    
**Format:**    
:   Tick()    
<!-- -->    
**When:**    
:   Called during the server tick, after sleeping procs and queued    
    commands, just before map information is sent to the clients.    
<!-- -->    
**Default action:**    
:   None.    
This proc allows you to do any updates just before map info is sent out.    
One possible use for this is to run a movement loop, or sync up any user    
interface input that might have arrived and deal with it all at once.    
### Example:    
world/Tick() for(var/client/C) if(C.mob?.move_dir) try step(C.mob,    
move_dir) catch // empty catch, just so a failed step won\'t break the    
loop    
Note: The tick will not wait if this proc sleeps. It effectively has    
[set waitfor=0]/proc/set/waitfor{.code} already built in. It\'s a    
good idea not to sleep in this proc or any of its callees at all, since    
it will keep getting called every tick.  