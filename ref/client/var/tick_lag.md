## tick_lag var (client) 
###### BYOND Version 511
**See also:**
*   [tick_lag var (world)](/ref/world/var/tick_lag.md) -m
*   [fps var (client)](/ref/client/var/fps.md) -m
*   [Pixel movement](/ref/%7Bnotes%7D/pixel-movement.md) -m<!-- -->
**Default value:**
*   0 (uses world.tick_lag value)


This is a client version of world.tick_lag, so that the client
can run at a faster speed for animations. For example, setting
client.tick_lag to 0.25 while world.tick_lag is the default 1 will mean
that all animations and glides are smoothed out and displayed at 40 FPS,
even though the server still runs at 10 FPS. The result is a
nicer-looking game with no additional impact on the server.


When this value is 0, the client and server tick at the same
rate.