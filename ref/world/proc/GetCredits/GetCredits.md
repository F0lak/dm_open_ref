[]{#/world/proc/GetCredits}    
## GetCredits proc (world) {#getcredits-proc-world byondver="503"}    
**See also:**    
:   [AddCredits proc (world)](/ref/world/proc/AddCredits/AddCredits.md)    
:   [PayCredits proc (world)](/ref/world/proc/PayCredits/PayCredits.md)    
<!-- -->    
**Format:**    
:   GetCredits(player)    
<!-- -->    
**Returns:**    
:   Number of credits if hub contact was successful, null otherwise.    
<!-- -->    
**Args:**    
:   player: a mob, client, key, or ckey    
Retrieves the number of available credits in a player\'s account. This    
feature is intended for games that make use of the credit system, and    
for security all such games must use a hub password.    
This proc will return null if there was no way to reach the hub. Use    
isnull() to check for a null value. Contacting the hub may take a few    
moments, so it is a good idea to use spawn() to avoid holding up the    
rest of the game.    
The best time to call this proc is before a player does something that    
would allow them to spend credits, and/or just afterward, so they can    
see what is left in their account.    
Note: You can specify a different hub path and hub_password by adding    
these as extra arguments, but this is not recommended for security    
reasons. If you use this feature, it should only be on games that cannot    
be downloaded by the public.  