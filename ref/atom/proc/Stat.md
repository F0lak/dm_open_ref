## Stat proc (atom)

**Format:**
+   Stat()
<!-- -->
**When:**
+   Called periodically by the client to update the stat window.
<!-- -->
**Default action:**
+   none.


The following code could be used to display a player\'s current
status.
### Example:

```
 mob/var health = 100 mob/Stat() stat(\"health\",health)
statpanel(\"Inventory\",contents) 
```


**See also:**
+   [Stat proc (client)](/ref/client/proc/Stat.md) 
+   [stat proc](/ref/proc/stat.md) 
+   [Info control (skin)](/ref/%7Bskin%7D/control/info.md) <!-- -->