[]{#/mob}    
## mob    
**See also:**    
:   [atom](/ref/atom/atom.md)    
:   [movable atoms](/ref/atom/movable/movable.md)    
:   [procs (mob)](/ref/mob/proc/proc.md)    
:   [vars (mob)](/ref/mob/var/var.md)    
:   [client](/ref/client/client.md)    
Mobs are \"mobile objects\" derived from `/mob`, which derives from    
`/atom/movable`. Human players are associated with a mob when they log    
on. Mobs are typically used for other \"creature\" types as well such as    
NPCs. This type is slightly more complex than objs since it can be    
attached to a client.    
This example defines the mob type `/mob/guzzler`.    
### Example:    
mob guzzler desc = \"Mean, mad, and wicked bad.\"  