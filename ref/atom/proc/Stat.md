
## Stat (proc)

**Format:**
+   Stat()

**Called When:**
+   Called periodically by the client to update the stat window.

**Default Action:**
+   none.
***
The following code could be used to display a player's current status.


```dm

mob/var
   health = 100
mob/Stat()
   stat("health",health)
   statpanel("Inventory",contents)

```

***
**Related Pages:**
+    [Stat proc (client)](/ref/client/proc/Stat)
+    [stat proc](/ref/proc/stat)
+    [Info](/ref/{skin}/control/info)
