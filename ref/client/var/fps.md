
## fps (var)

**Default Value:**
+   0 (uses world.fps value)
***
This is a client version of world.fps, so that the client can run at a faster speed for animations. For example, setting client.fps to 40 while world.fps is the default 10 will mean that all animations and glides are smoothed out and displayed at 40 FPS, even though the server still runs at 10 FPS. The result is a nicer-looking game with no additional impact on the server.

When this value is 0, the client and server tick at the same rate.
***
**Related Pages:**
+    [fps var (world)](/ref/world/var/fps)
+    [tick_lag var (client)](/ref/client/var/tick_lag)
+    [Pixel movement](/ref/{notes}/pixel-movement)
