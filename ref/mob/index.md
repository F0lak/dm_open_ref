
## mob (info)
***
Mobs are "mobile objects" derived from `/mob`, which derives from `/atom/movable`. Human players are associated with a mob when they log on. Mobs are typically used for other "creature" types as well such as NPCs. This type is slightly more complex than objs since it can be attached to a client.

This example defines the mob type `/mob/guzzler`.


```dm

mob
  guzzler
    desc = "Mean, mad, and wicked bad."

```

***
**Related Pages:**
+    [atom](/ref/atom)
+    [atom/movable](/ref/atom/movable)
+    [procs (mob)](/ref/mob/proc)
+    [vars (mob)](/ref/mob/var)
+    [client](/ref/client)
