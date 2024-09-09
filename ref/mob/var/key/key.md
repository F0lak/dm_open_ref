[]{#/mob/var/key}    
## key var (mob)    
**See also:**    
:   [ckey var (mob)](/ref/mob/var/ckey)    
:   [client](/ref/client)    
:   [key var (client)](/ref/client/var/key)    
<!-- -->    
**Default value:**    
:   null    
For player mobs (PCs) this is the value of the player\'s key. For    
non-player mobs (NPCs), this is the value of the \"desired\" key. This    
means that if a player with that key logs into the world, he will be    
connected to that mob (as opposed to a new one of type world.mob).    
Setting the mob\'s key will cause a client with the same key to connect    
to the mob. Any other mob with the same key will lose it.    
Key values are always compared in canonical form (ie the form returned    
by ckey()) so setting a mob\'s key to \"Dan\", \"dan\" are equivalent as    
far as controlling player linkage.  