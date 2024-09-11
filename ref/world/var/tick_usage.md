## tick_usage var (world) 
###### BYOND Version 510
**See also:**
*   [cpu var (world)](/ref/world/var/cpu.md) -m
*   [tick_lag var (world)](/ref/world/var/tick_lag.md) -m
*   [Tick proc (world)](/ref/world/proc/Tick.md) -m

This is the approximate percentage of the server tick that has
been used already. A value under 100 means there\'s time to do more
calculations, which can include any pending procs that are still waiting
to run on this tick. When the value is over 100, the tick is running
long and your world will experience lag. 

Keep in mind that
sending maps to clients is the last thing that happens during a tick,
except for handling any events such as player commands that might arrive
before the next tick begins. Therefore in a verb, `tick_usage` might
have a higher value than you would expect to see in a proc that loops
and sleeps.