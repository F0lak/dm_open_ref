
## Del (proc)

**Format:**
+   Del()

**Called When:**
+   Called when the player disconnects from the world.

**Default Action:**
+   If the player is connected to a mob, call mob.Logout() to disconnect.
If the player's connection to the world is still not dead, kill it.
***
Note that this does not automatically delete the player's mob. If you want to do that, you could do so in mob.Logout().
***
**Related Pages:**
+    [Logout proc (mob)](/ref/mob/proc/Logout)
