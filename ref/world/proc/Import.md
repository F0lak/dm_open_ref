## Import proc (world)
**See also:**
*   [Export proc (world)](/ref/world/proc/Export.md) -m
*   [Import proc (client)](/ref/client/proc/Import.md) -m
*   [Topic proc (world)](/ref/world/proc/Topic.md) -m
*   [fcopy proc](/ref/proc/fcopy.md) -m<!-- -->
**Format:**
*   Import()
<!-- -->
**Returns:**
*   The file sent by the remote server. The file will be downloaded to
    the local server\'s resource cache. Note that this will cause the
    caller to sleep while waiting for the necessary data to be
    transfered.
<!-- -->
**When:**
*   Call this inside world.Topic() if you are expecting a file from the
    remote server.
### Example:

```
 //sending the file mob/proc/Export(Addr) var/savefile/F =
new() F.Write(src) world.Export(Addr,F) //receiving the file
world/Topic() var/savefile/F = new(world.Import()) F.Read() //read the
mob 
```
 

This example defines a mob proc called Export()
which writes the mob to a savefile and sends it to another server
(specified by Addr). The remote server opens it as a savefile and
creates the mob (if the same mob type is defined on both servers and
mob.Read() is compatible with the sending server\'s mob.Write()).


Note that another method of transferring player mobs is to use
the key savefile (accessed by client.Export() and client.Import()).
Direct server to server communication on the other hand could transfer
data (like non-players) without the need for player involvement at all.


Savefiles are the most common type of file to transfer, but
world.Import() simply returns a reference to an item in the world\'s
.rsc file, which could be any type of file. This particular example
demonstrates how to open such a file as a temporary savefile. (It gets
dumped from the cache into a separate temporary file, which is then
opened as a savefile.) Other types of files would be handled
differently. For example, you could use fcopy() to dump the cached item
to its own separate file.