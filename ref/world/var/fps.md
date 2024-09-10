[]{#/fps var (world).md}    
## fps var (world) {#fps-var-world byondver="490"}    
**See also:**    
:   [tick_lag var (world)](/world/var/tick_lag)    
:   [fps var (client)](/client/var/fps)    
:   [Pixel movement](/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Default value:**    
:   10    
The value of `world.fps` defines the speed of the world in frames    
(server ticks) per second. By default this is 10 fps, which is a good    
speed if all objects move in full tiles. Higher values yield smoother    
results, but at a cost to performance. Timing of many events may be    
limited by the system clock, so `fps` values beyond 40 or 50 may cause    
unwanted effects like jitter even for projects that are not very    
demanding in terms of performance.    
For projects making use of pixel movement, higher `fps` is usually    
desired. 40 seems to be a good value for general use, but in worlds that    
have a large number of players, you may wish to lower the value and give    
players a higher `step_size` per tick instead.    
This var exists for convenience; it is calculated by    
`10 / world.tick_lag`. The value of `world.tick_lag` is actually more    
accurate, but it is easier to think of world speed in terms of frames    
per second. The actual tick rate has a resolution of 1 ms.    
When reading `world.fps`, the result is always given as a whole number    
to gloss over rounding error.    
If you set `client.tick_lag` or `client.fps` to a value other than 0,    
you can make the client tick at a different (usually faster) rate.  