[]{#/world/proc/Topic}
## Topic proc (world)
**See also:**
:   [Del proc (world)](#/world/proc/Del)
:   [Export proc (world)](#/world/proc/Export)
:   [Import proc (client)](#/client/proc/Import)
:   [Import proc (world)](#/world/proc/Import)
:   [Reboot proc (world)](#/world/proc/Reboot)
<!-- -->
**Format:**
:   Topic(T,Addr,Master,Keys)
<!-- -->
**When:**
:   Called when a message is received from another server by using
    world.Export(). If a file is expected, world.Import() may be called
    to get it. The return value of Topic() will be passed back to the
    remote server.
<!-- -->
**Args:**
:   T: The topic text string specified by the remote server (everything
    following ? in the URL).
:   Addr: The address of the remote server.
:   Master: 1 if remote server is the server which started this one.
:   Keys: List of keys belonging to users who are logged in on the
    remote server
<!-- -->
**Default action:**
:   The topic \"ping\" returns a true value (number of players plus
    one), which may be useful for telling if a server is alive. The
    topics \"Reboot\" and \"Del\" will call world.Reboot() and
    world.Del() respectively if the message was sent by the master
    server.
### Example:
world/Topic(T) if(findtext(T,\"shout:\") == 1) world \<\< copytext(T,7)
This example allows other servers to send this server topic text of the
form \"shout:msg\" and will broadcast the message to all the players in
this world.
The Keys argument is either null, or a list of user keys. Any keys in
the list are logged in to the remote server.
Always validate the input in `Topic()` calls to make sure it\'s correct
and the query you\'re recieving is legitimate.