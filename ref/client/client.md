[]{#/client.md}    
## client.md    
**See also:**    
:   [client.md var (mob)]/mob/var/client.md    
:   [key var (mob)]/mob/var/key    
:   [procs (client.md)]/client.md/proc    
:   [vars (client.md)]/client.md/var    
Each connected player has a corresponding client.md object. It has    
variables and procedures which control aspects of player input/output.    
This object is also responsible for linking the player up to a mob.    
The client.md can be reassigned from its original mob M to a new mob N by    
setting N.client.md = M.client.md. This process disconnects the player from M    
(calling M.Logout()) and connects the player to N (calling N.Login()).    
Setting the mob\'s key has the same effect.    
Additional vars, procs, and verbs may be added to the client.md in order to    
give the player properties that are independent of the mob.  