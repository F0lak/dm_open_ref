## SetMedal proc (world)

**Format:**
+   SetMedal(medal, player)
<!-- -->
**Returns:**
+   1 if the medal was awarded successfully, 0 or null otherwise.
<!-- -->
**Args:**
+   medal: name of the medal being awarded
+   player: a mob, client, key, or ckey


Awards a medal to a player. The proc will return 1 if it is
successful, or 0 if the medal was already awarded. If the world already
knows this medal was earned before, the hub will not be contacted.


This proc will return null if there was no way to reach the
hub. Use isnull() to check for a null value. Contacting the hub may take
a few moments, so it is a good idea to use spawn() to avoid holding up
the rest of the game.
### Example:

``` dm
 mob/monster/dragon Die(mob/killer) // assume Die() is a
proc all mobs have spawn() if(ismob(killer) && killer.key)
world.SetMedal("Dragon slayer", killer) 
```

Note: You can specify a different hub path and hub_password by adding
these as extra arguments, but this is not recommended for security
reasons. If you use this feature, it should only be on games that cannot
be downloaded by the public.

> [!TIP] 
> **See also:**
> +   [GetMedal proc (world)](/ref/world/proc/GetMedal.md) 
> +   [ClearMedal proc (world)](/ref/world/proc/ClearMedal.md) 
> +   [GetScores proc (world)](/ref/world/proc/GetScores.md) 
> +   [SetScores proc (world)](/ref/world/proc/SetScores.md) <!-- -->