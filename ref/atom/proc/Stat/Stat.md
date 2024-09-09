[]{#/atom/proc/Stat}    
## Stat proc (atom)    
**See also:**    
:   [Stat proc (client)](/ref/client/proc/Stat)    
:   [stat proc](/ref/proc/stat)    
:   [Info control (skin)](/ref/%7Bskin%7D/control/info)    
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