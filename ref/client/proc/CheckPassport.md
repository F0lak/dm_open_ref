## CheckPassport proc (client)

**Format:**
+   CheckPassport(passport_identifier)
**Args:**
+	passport_identifier

a text string assigned to you by the BYOND hub (or an ID/token for a different API; see below).
This built-in procedure checks to see if the user is subscribed to a particular BYOND hub entry. If the user is subscribed, the result is the number of days left (rounded up) on their subscription, or -1 for lifetime subscribers.

Example:
```dm
world
   hub = "My.Hub"  //change this to your own hub entry

mob/var
   full_access

mob/Login()
   if(client.CheckPassport("0123456789abcdef"))
      full_access = 1
   else
      src << "For full access, <a href=\
              'http://www.byond.com/hub/[world.hub]' >subscribe</a>!"
   return ..()
```
Note that in general the value of world.hub has nothing to do with the passport you happen to check. This example assumes the passport number belongs to world.hub just for the purpose of forwarding the user to the appropriate subscription page.

Other APIs 514
You can use this with other APIs that are supported by BYOND, which currently only applies to Steam and only if the game is specially built for Steam support.

To check ownership of a Steam game or DLC (must be the current game's ID or one of its DLCs), use "steam:NNNNNN" for the passport string, where NNNNNN is a Steam app ID. Note that the user must be logged into Steam for this to work.

> [!TIP]
> + See also:
> + [IsSubscribed proc (world)](ref/client/proc/IsSubscribed.md)
> + [IsByondMember proc (client)](ref/client/proc/IsBYONDMember.md)
> + [GetAPI proc (client)](ref/client/proc/GetAPU.md)
> + [SetAPI proc (client)](ref/client/proc/SetAPI.md)