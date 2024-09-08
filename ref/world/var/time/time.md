[]{#/world/var/time}
## time var (world)
**See also:**
:   [realtime var (world)](#/world/var/realtime)
:   [tick_lag var (world)](#/world/var/tick_lag)
This gives the amount of time (in 1/10 seconds) that the world has been
running. In actual fact, it is the number of server ticks that have
passed multiplied by world.tick_lag. Therefore if the server sleeps
(when no players are connected) this time is not counted. Also, if the
server runs overtime during a tick (because procs take longer than
tick_lag to finish) this still only counts as one tick. This value is
therefore a measure of \"game time\" rather than real time.