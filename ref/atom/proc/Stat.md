[]{#/Stat proc (atom).md}    
## Stat proc (atom)    
**See also:**    
:   [Stat proc (client)]/client/proc/Stat    
:   [stat proc]/proc/stat    
:   [Info control (skin)]/%7Bskin%7D/control/info    
<!-- -->    
**Format:**    
:   Stat()    
<!-- -->    
**When:**    
:   Called periodically by the client to update the stat window.    
<!-- -->    
**Default action:**    
:   none.    
The following code could be used to display a player\'s current status.    
### Example:    
mob/var health = 100 mob/Stat() stat(\"health\",health)    
statpanel(\"Inventory\",contents)  