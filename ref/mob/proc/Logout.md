## Logout proc (mob)

**Format:**
+   Logout()
<!-- -->
**When:**
+   Called when a player\'s client has disconnected from a mob. This
    happens in client.Del() when the player logs out of the world. It
    may also happen when the player switches from one mob to another.
<!-- -->
**Default action:**
+   None.


One may wish to distinguish between a player who has
disconnected from the game and one who is simply switching from one mob
to another. In the case of a player switching to another mob, by the
time `Logout()` is called, the original mob\'s key will be null, whereas
the key will still be non-null in the case of a player disconnecting
from the game.

> [!TIP] 
> **See also:**
> +   [Login proc (mob)](/ref/mob/proc/Login.md) 
> +   [client var (mob)](/ref/mob/var/client.md) 
> +   [key var (mob)](/ref/mob/var/key.md) <!-- -->