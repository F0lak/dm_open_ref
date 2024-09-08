[]{#/client/var/tick_lag}
## tick_lag var (client) {#tick_lag-var-client byondver="511"}
**See also:**
:   [tick_lag var (world)](#/world/var/tick_lag)
:   [fps var (client)](#/client/var/fps)
:   [Pixel movement](#/%7Bnotes%7D/pixel-movement)
<!-- -->
**Default value:**
:   0 (uses world.tick_lag value)
This is a client version of world.tick_lag, so that the client can run
at a faster speed for animations. For example, setting client.tick_lag
to 0.25 while world.tick_lag is the default 1 will mean that all
animations and glides are smoothed out and displayed at 40 FPS, even
though the server still runs at 10 FPS. The result is a nicer-looking
game with no additional impact on the server.
When this value is 0, the client and server tick at the same rate.