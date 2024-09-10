[]{#/timeofday var (world).md}    
## timeofday var (world)    
**See also:**    
:   [realtime var (world)]/world/var/realtime    
:   [time var (world)]/world/var/time    
:   [time2text proc]/proc/time2text    
This is the time (in 1/10 seconds) since 00:00:00 GMT today. It is    
basically identical to `world.realtime` but doesn\'t include any    
information about the date. This is a much smaller number; hence it is    
more accurate.  