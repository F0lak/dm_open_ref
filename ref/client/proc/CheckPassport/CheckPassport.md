[]{#/client/proc/CheckPassport}
## CheckPassport proc (client)
**See also:**
:   [IsSubscribed proc (world)](#/world/proc/IsSubscribed)
:   [IsByondMember proc (client)](#/client/proc/IsByondMember)
:   [GetAPI proc (client)](#/client/proc/GetAPI)
:   [SetAPI proc (client)](#/client/proc/SetAPI)
<!-- -->
**Format:**
:   CheckPassport(passport_identifier)
<!-- -->
**Args:**
:   passport_identifier: a text string assigned to you by the BYOND hub
    (or an ID/token for a different API; see below).
This built-in procedure checks to see if the user is subscribed to a
particular BYOND hub entry. If the user is subscribed, the result is the
number of days left (rounded up) on their subscription, or -1 for
lifetime subscribers.
### Example:
world hub = \"My.Hub\" //change this to your own hub entry mob/var
full_access mob/Login() if(client.CheckPassport(\"0123456789abcdef\"))
full_access = 1 else src \<\< \"For full access,
[subscribe](\){'http:="" www.byond.com="" hub="" [world.hub]'=""}!\"
return ..()
Note that in general the value of world.hub has nothing to do with the
passport you happen to check. This example assumes the passport number
belongs to world.hub just for the purpose of forwarding the user to the
appropriate subscription page.
### Other APIs {#other-apis byondver="514"}
You can use this with other APIs that are supported by BYOND, which
currently only applies to Steam and only if the game is specially built
for Steam support.
To check ownership of a Steam game or DLC (must be the current game\'s
ID or one of its DLCs), use `"steam:`*`NNNNNN`*`"` for the passport
string, where *NNNNNN* is a Steam app ID. Note that the user must be
logged into Steam for this to work.