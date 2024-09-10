[]{#/Del proc (client).md}    
## Del proc (client)    
**See also:**    
:   [Logout proc (mob)](/mob/proc/Logout)    
<!-- -->    
**Format:**    
:   Del()    
<!-- -->    
**When:**    
:   Called when the player disconnects from the world.    
<!-- -->    
**Default action:**    
:   If the player is connected to a mob, call mob.Logout() to    
    disconnect. If the player\'s connection to the world is still not    
    dead, kill it.    
Note that this does not automatically delete the player\'s mob. If you    
want to do that, you could do so in mob.Logout().  