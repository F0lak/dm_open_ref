[]{#/tick_lag var (world).md}    
## tick_lag var (world)    
**See also:**    
:   [fps var (world)]/world/var/fps    
:   [tick_lag var (client)]/client/var/tick_lag    
:   [tick_usage var (world)]/world/var/tick_usage    
:   [sleep proc]/proc/sleep    
<!-- -->    
**Default value:**    
:   1    
This is the smallest unit of time (one server tick) measured in 1/10    
seconds. The duration of events that take some finite amount of time    
(like sleep) will be rounded to a whole number of ticks.    
Players are limited to one command (including movements) per server    
tick, so this value can be used to adjust the responsiveness of the    
game. If the network is too slow to keep up with players, their commands    
will get queued up, which can be annoying when trying to move. In this    
case, tick_lag should be increased so that the stored up movement    
commands are discarded. On the other hand, if you have a very fast    
network, you may wish to decrease tick_lag to speed up the response time    
to player commands.    
Often it is more convenient to set world.fps instead of world.tick_lag,    
since fps (frames per second) is an easier way to think of server ticks.    
world.tick_lag is 10 / world.fps and vice-versa, so a tick_lag of 0.25    
is equal to 40 fps.    
If you set client.tick_lag or client.fps to a value other than 0, you    
can make the client tick at a different (usually faster) rate.  