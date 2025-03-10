## Export proc (client)


**Format:**
+   client.Export(file)

**Args:**
+   file: file to send to client


This stores the file on the user\'s computer in a special
location unique to each registered [world.hub](/ref/world/var/hub.md) setting.
This is most useful for writing a client-side savefile, but any type of
file may be stored. The purpose of this is to exchange information
between different worlds running under the same hub path. 

> [!TIP]
> This file can be found in the BYOND Documents folder on the users machine under the following path:
> `..\Documents\BYOND\KeyInfo\ckey\<worldid>.sav`

When
a file is exported to the player\'s computer, it replaces any previous
file stored by a game with the same `world.hub` value. This should not
be used for anything requiring high security, because any other world
could make use of the same hub path and access the file. It is also
possible for the user to tinker with the file, since it resides on their
computer. 

To delete the client-side file completely, call
`client.Export()` with no argument at all.
### Example:

```dm
mob/verb/save()
   var/savefile/F = new()
   F << usr     //write the player's mob
   usr.client.Export(F)

client/New()
   var/client_file = Import()
   if(client_file)
      var/savefile/F = new(client_file) //open it as a savefile
      F >> usr  //read the player's mob
   return ..()
```


> [!TIP] 
> **See also:**
> +   [Import proc (client)](/ref/client/proc/Import.md) 
> +   [New proc (client)](/ref/client/proc/New.md) 
> +   [hub var (world)](/ref/world/var/hub.md) 
> +   [savefile](/ref/savefile.md) 
