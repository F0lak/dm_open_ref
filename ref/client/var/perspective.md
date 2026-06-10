
## perspective (var)

**Default Value:**
+   MOB_PERSPECTIVE
***
This controls the eye's apparent center and what can be seen by the client.

EYE_PERSPECTIVE determines how visibility calculations are performed when <code>client.eye</code> and <code>client.mob</code> are different. Normally, visibility is done from the position of the mob, rather than from the eye (which is actually just the center of the map view). The alternative flag is MOB_PERSPECTIVE, the default.

EDGE_PERSPECTIVE limits scrolling to the bounds of the map (1,1 to world.maxx,world.maxy), and does not keep the mob centered if it strays near the edge.

The above values can be used together via the | operator.
***
**Related Pages:**
+    [eye var (client)](/ref/client/var/eye)
+    [mob var (client)](/ref/client/var/mob)
