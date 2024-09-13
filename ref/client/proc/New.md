## New proc (client)

<!-- -->
**Format:**
+   New(TopicData)
<!-- -->
**Returns:**
+   The newly connected mob, client.mob, or null to disallow the
    connection.
<!-- -->
**When:**
+   Called when the player first tries to connect to the world.
<!-- -->
**Args:**
+   usr: The mob in the world with the same key as the player, if it
    exists.
+   TopicData: If the player accessed the world with a \"connection
    topic\", this is the topic text. Otherwise it is null.
<!-- -->
**Default action:**
+   Look for an existing mob with the same key as the player. If found,
    connect the player to that mob (mob.Login()). Otherwise, look for a
    prototype mob with the same key as the player. If found, create a
    mob of that type and connect the player to it. Otherwise, create a
    mob of type world.mob, give it the same name and gender as the
    player\'s key, and connect the player to it. If TopicData is not
    null, call client.Topic(TopicData). Finally, the player\'s mob is
    returned.


This is a fairly low-level procedure that you would only want
to override if you cannot accomplish the same thing in `mob/Login()` or
`mob/New()`. One reason to override `client/New()` is if player mobs are
created from a savefile. In that case, you don\'t need a temporary mob
to be created first.
### Example:

``` dm
 client/New() if(usr) return ..() //reconnecting to
existing mob else var/player_sav = \"players/\[ckey\].sav\"
if(length(file(player_sav))) //if player savefile exists var/savefile/F
= new(player_sav) //open it F \>\> usr //create saved mob return ..()
//creates a new mob if necessary mob/Logout() var/player_sav =
\"players/\[ckey\].sav\" var/savefile/F = new(player_sav) F \<\< src del
src 
```
 

If you want to do any user-interaction before
loading the saved mob, you will have to create a temporary mob first in
order to interact with the player. In that case, you are better off
doing things in `mob/Login()`, rather than `client/New()`. 

Note
that for the above example to work, you **must** make proper use of the
[tmp](/ref/var/tmp.md) flag when defining new object variables. Otherwise,
this can end up sucking large portions of your world into each player
savefile, which can have all sorts of unexpected consequences!

> [!TIP] 
> **See also:**
> +   [Export proc (client)](/ref/client/proc/Export.md) 
> +   [Import proc (client)](/ref/client/proc/Import.md) 
> +   [Login proc (mob)](/ref/mob/proc/Login.md) 
> +   [New proc (datum)](/ref/datum/proc/New.md) 
> +   [Topic proc (client)](/ref/client/proc/Topic.md) 
> +   [mob var (world)](/ref/world/var/mob.md) 
> +   [savefile](/ref/savefile.md) 