## mob var (world)

**Default value:**
+   /mob.


When a player connects to the world, the world is searched for
a mob with the player\'s key. If one is found, the player is connected
to that mob. If none is found, a new mob of type world.mob is created
and the player is connected to this new mob. 

The default value
is /mob. Setting world.mob to 0 prevents the creation of default mobs.
### Example:

```
 world mob = /mob/newbie mob/newbie Login() src \<\<
\"Welcome, \[name\].\" ..() 
```
 

This example will
connect new players to mobs of type /mob/newbie. They are welcomed when
they connect.

> [!TIP] 
> **See also:**
> +   [New proc (client)](/ref/client/proc/New.md) <!-- -->