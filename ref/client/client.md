## client


Each connected player has a corresponding client object. It has
variables and procedures which control aspects of player input/output.
This object is also responsible for linking the player up to a mob.


The client can be reassigned from its original mob M to a new
mob N by setting N.client = M.client. This process disconnects the
player from M (calling M.Logout()) and connects the player to N (calling
N.Login()). Setting the mob\'s key has the same effect.


Additional vars, procs, and verbs may be added to the client in
order to give the player properties that are independent of the mob.

> [!TIP] 
> **See also:**
> +   [client var (mob)](/ref/mob/var/client.md) 
> +   [key var (mob)](/ref/mob/var/key.md) 
> +   [procs (client)](/ref/client/proc.md) 
> +   [vars (client)](/ref/client/var.md) 