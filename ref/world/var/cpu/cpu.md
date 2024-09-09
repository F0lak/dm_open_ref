[]{#/world/var/cpu}    
## cpu var (world)    
**See also:**    
:   [map_cpu var (world)](/ref/world/var/map_cpu/map_cpu.md)    
:   [tick_lag var (world)](/ref/world/var/tick_lag/tick_lag.md)    
:   [tick_usage var (world)](/ref/world/var/tick_usage/tick_usage.md)    
:   [Tick proc (world)](/ref/world/proc/Tick/Tick.md)    
This is the percentage of a server tick that the server spends    
processing running procs and the work of sending map information to    
players. A value of 0 would indicate very little cpu usage. A value of    
100 would indicate full cpu usage, which could mean that the server    
cannot complete all the necessary computations during a tick to finish    
in time for the next tick. In this case, timed events (such as sleep)    
may take longer than requested.    
When deciding on a value for tick_lag, one could use this value to    
determine if the CPU is fast enough to tick at a higher rate.    
The `map_cpu` var is a subset of this, measuring only time used for    
sending map information.  