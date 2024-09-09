[]{#/world/proc/SetScores}    
## SetScores proc (world)    
**See also:**    
:   [GetScores proc (world)](/ref/world/proc/GetScores)    
:   [GetMedal proc (world)](/ref/world/proc/GetMedal)    
:   [SetMedal proc (world)](/ref/world/proc/SetMedal)    
:   [ClearMedal proc (world)](/ref/world/proc/ClearMedal)    
<!-- -->    
**Format:**    
:   SetScores(key, fields)    
<!-- -->    
**Returns:**    
:   The key, if the scores were successfully updated; null otherwise.    
<!-- -->    
**Args:**    
:   key: the name of the player, character, etc. for which scores should    
    be set    
:   fields: The data fields to set    
Updates scores that are kept on the BYOND hub.    
The key is an arbitrary text value. Usually a player\'s key is a good    
choice, but you can also use the name of their character, or anything    
else you like, as long as it is unique. The key is case-insensitive.    
Scores and stats use data fields, which might be things like \"Score\",    
\"Level\", \"Class\", etc. Use list2params() to set the fields that you    
want to change. Fields that you do not include in the list will not be    
changed. A field with a blank value will be deleted.    
Sending an empty text string for the fields will erase the scores for    
that key.    
This proc will return null if there was no way to reach the hub. Use    
isnull() to check for a null value. Contacting the hub may take a few    
moments, so it is a good idea to use spawn() to avoid holding up the    
rest of the game.    
### Example:    
var/params // Change the Score and Pet fields params =    
list(\"Score\"=123, \"Pet\"=\"Dog\") world.SetScores(\"Tom\",    
list2params(params)) // Delete the Pet field params = list(\"Pet\"=\"\")    
world.SetScores(\"Tom\", list2params(params)) // Delete Tom\'s scores    
entirely world.SetScores(\"Tom\", \"\")    
Note: You can specify a different hub path and hub_password by adding    
these as extra arguments, but this is not recommended for security    
reasons. If you use this feature, it should only be on games that cannot    
be downloaded by the public.  