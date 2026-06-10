
## Logout (proc)

**Format:**
+   Logout()

**Called When:**
+   Called when a player's client has disconnected from a mob.  This happens
    in client.Del() when the player logs out of the world.  It may also
    happen when the player switches from one mob to another.

**Default Action:**
+   None.
***
One may wish to distinguish between a player who has disconnected from the game and one who is simply switching from one mob to another. In the case of a player switching to another mob, by the time <code>Logout()</code> is called, the original mob's key will be null, whereas the key will still be non-null in the case of a player disconnecting from the game.
***
**Related Pages:**
+    [Login proc (mob)](/ref/mob/proc/Login)
+    [client](/ref/mob/var/client)
+    [key var (mob)](/ref/mob/var/key)
