
## statpanel (proc)

**Format:**
+   statpanel(Panel,Name,Value)

**Arguments:**
+   Panel: the name of the stat panel
+   Name: the name of the stat line
+   Value: the data to be displayed

**Returns:**
+   If called with just a Panel argument, 1 is returned if the player is
    looking at the panel and 0 is returned if not.  This may be useful to
    avoid the needless overhead of generating output to a panel that is not
    visible.
***
This is used in a Stat() proc to change the default panel (for subsequent stat lines) or to send one line to the specified panel. Name and Value are both optional. If neither is specified, this simply changes the default panel. Otherwise, the default panel is unchanged and a stat line is appended to Panel.


```dm

mob/Stat()
   stat("description",src.desc)
   if(src == usr) statpanel("inventory",src.contents)

```


This example displays the mob's description in one panel and inventory in another. Only the mob may see his own inventory, but you don't have to worry about that unless you change client.statobj to something other than one's own mob.
***
**Related Pages:**
+    [Stat](/ref/atom/proc/Stat)
+    [Stat proc (client)](/ref/client/proc/Stat)
+    [stat proc](/ref/proc/stat)
+    [Info](/ref/{skin}/control/info)
