[]{#/mob/proc/Login}
## Login proc (mob)
**See also:**
:   [Logout proc (mob)](#/mob/proc/Logout)
:   [client var (mob)](#/mob/var/client)
<!-- -->
**Format:**
:   Login()
<!-- -->
**When:**
:   Called when a player\'s client tries to connect to a mob. This is
    called by default from client.New(), when the player logs into the
    world.
<!-- -->
**Default action:**
:   If the mob has no location, place it near (1,1,1) if possible.
    Change the player\'s stat object (client.statobj) to the mob.
One can typically tell if a player is connecting to a fresh mob versus
reconnecting to an existing one by testing if the mob\'s location is
null.